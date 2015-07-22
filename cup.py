from editor import Editor
from curses import textpad
import curses


cup = Editor()
cup.add_buffer("blah", "trial text, will it go in?")
cup.buffer_list()
cup.buffers["blah"].edit_buffer()
cup.test_echo()
cup.close()


