import curses
import curses.textpad as textpad

class Editor():
    def __init__(self, filename=''):
        self.screen = curses.initscr()
        self.screen.refresh()
        self.buffers = {}
        curses.cbreak()
        self.screen.keypad(1)
        curses.noecho()
        curses.start_color()
    
    def test_echo(self):
        self.screen.addnstr("test string", 80)
        self.screen.refresh()

    def add_buffer(self, filename):
        self.buffers[ filename ] = Buffer(filename)

    def close(self):
        """
        unsets things to make curses friendly
        """
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()

class Buffer():
    def __init__(self, filename, text=''):
        self.filename = filename
        self.text = text
        self.screen = curses.newwin(curses.LINES-1, curses.COLS-1, 1,0)
        self.textbox = textpad.Textbox(self.screen)

    def edit_buffer(self):
        self.screen.refresh()
        self.textbox.edit()
        self.contents = self.textbox.gather()
