" The entry point of the command interpreter "

import cmd

class HBNBCommand(cmd.Cmd):
    " The Command Interface class which inherits the Cmd class "

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        " Exits the Console"
        return True
    
    def do_EOF(self, line):
        " Exits the Console"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()