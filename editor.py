import curses
from curses.textpad import Textbox, rectangle

class Editor():
    def __init__(self, filename=''):
        self.screen = curses.initscr()
        self.buffers = {}
        curses.cbreak()
        self.screen.keypad(1)
        curses.noecho()
        curses.start_color()
        self.screen.refresh()
    
    def test_echo(self):
        self.screen.addnstr("test string", 80)
        self.screen.refresh()

    def buffer_list(self, active=''):
        """
        puts a list of open buffers at the top
        """
        rectangle(self.screen, 0,0, 1, curses.COLS -1)
        self.screen.refresh()
        buflist = curses.newwin(1, curses.COLS-1, 0,0)
        buflist.refresh()
        if (active == ''):
            bufferlist = ["new file"]
        bufferlist += list(self.buffers.keys())
        buflist.addstr(" | ".join(bufferlist))
        buflist.refresh()

    def add_buffer(self, filename, text):
        self.buffers[filename] = Buffer(filename, text)

    def close(self):
        """
        unsets things to make curses friendly
        """
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()

    def switch_buffer(self, target):
        self.buffers[target].edit_buffer()

class Buffer():
    def __init__(self, filename, text=''):
        self.filename = filename
        self.text = text

    def edit_buffer(self):
        screen = curses.newwin(curses.LINES-1, curses.COLS-1, 1,0)
        screen.addstr(self.text)
        textbox = Textbox(screen)
        textbox.edit()
        self.text = textbox.gather()
