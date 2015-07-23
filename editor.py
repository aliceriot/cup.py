import curses
from curses.textpad import Textbox, rectangle

def gather(textbox):
    """
    collect and return the contents of the window.
    modified from the gather provided by the standard library
    """
    result = ""
    for y in range(textbox.maxy+1):
        textbox.win.move(y, 0)
        stop = textbox._end_of_line(y)
        if stop == 0 and textbox.stripspaces:
            continue
        for x in range(textbox.maxx+1):
            if textbox.stripspaces and x > stop:
                break
            result = result + chr(curses.ascii.ascii(textbox.win.inch(y, x)))
        if textbox.maxy > 0:
            result = result + "\n"
    return result


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
        rectangle(self.screen, 0,0, 2, curses.COLS -1)
        self.screen.refresh()
        buflist = curses.newwin(1, curses.COLS-1, 1,1)
        buflist.refresh()
        bufferlist = []
        if (active == ''):
            bufferlist = ["new file"]
        bufferlist += list(self.buffers.keys())
        buflist.addstr("buffers:" + " | ".join(bufferlist))
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
        bufscreen = curses.newwin(curses.LINES-1, curses.COLS-1, 3,0)
        bufscreen.addstr(self.text)
        textbox = Textbox(bufscreen)
        textbox.stripspaces = False
        textbox.edit()
        # self.text = bufscreen.instr(0,0) + "\n\n now textbox!\n" + textbox.gather()
        self.text = gather(textbox)
        return gather(textbox)
        bufscreen.clear()
