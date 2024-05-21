#!/usr/bin/python3
'''
console
'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''
    HBNBCommand
    '''
    prompt = "(hbnb)"

    def emptyline(self):
        '''do nothing'''
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit



if __name__ == '__main__':
    HBNBCommand().cmdloop()
