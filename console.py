#!/usr/bin/python3
'''
console
'''
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    '''An Hbnbcommand console'''

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
