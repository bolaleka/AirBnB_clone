#!/usr/bin/python3
"""command interpreter to manage your AirBnB objects
"""
import cmd


class Console(cmd.Cmd):
    """Console class to maange object
    """

    intro = '\n   ###############################\n   \
            #\tWelcome to AirBnb Clone  #\n   \
            ###############################\n'
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exit"""
        return True

    def do_quit(self, line):
        """Quit"""
        return True

    def postloop(self):
        print


if __name__ == '__main__':
    Console().cmdloop()
