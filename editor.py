import curses

class Editor():
    def __init__(self, filename=''):
        self.screen = curses.initscr()
        self.filebuf = ''
        if filename != '':
            with open(filename, 'r') as myfile:
                self.filebuf = myfile.read()
        self.screen.addstr(self.filebuf)
        self.screen.refresh()
    
    def test_echo(self):
        self.screen.addnstr("test string", 80)
        self.screen.refresh()

