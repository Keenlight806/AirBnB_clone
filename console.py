#!/usr/bin/python3
'''
console
'''
import cmd
from models.base_model import BaseModel
import shlex
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    '''
    HBNBCommand
    '''
    prompt = "(hbnb) "
    valid_classes = {"BaseModel", "User"}

    def emptyline(self):
        '''do nothing'''
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

    def do_create(self, arg):
        '''To create'''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print ("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print ("** class doesn't exist **")
        else:
            new_ins = eval(f"{commands[0]}()")
            storage.save()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, arg):
        '''To show'''
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''To delete'''
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''print all'''
        commands = shlex.split(arg)
        objects = storage.all()
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        '''To update'''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) == 2:
                print("** attribute name missing **")
            elif len(commands) == 3:
                print("** value missing **")
            else:
                obj = objects[key]
                
                try:
                    commands[3] = eval(commands[3])
                except Exception:
                    pass
                setattr(obj, commands[2], commands[3])
                obj.save()
            



if __name__ == '__main__':
    HBNBCommand().cmdloop()
