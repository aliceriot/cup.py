import curses
import curses.textpad as textpad

class Editor():
    def __init__(self, filename=''):
        self.screen = curses.initscr()
        self.screen.refresh()
        self.buffers = {}
    
    def test_echo(self):
        self.screen.addnstr("test string", 80)
        self.screen.refresh()

    def add_buffer(self, filename):
        self.buffers[ filename ] = Buffer(filename)

class Buffer():
    def __init__(self, text=''):
        self.screen = curses.newwin(20,20)
        self.textbox = textpad.Textbox(self.screen)

    def edit_buffer(self):
        self.screen.refresh()
        self.textbox.edit()
