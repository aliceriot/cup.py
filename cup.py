from editor import Editor
from curses import textpad
import curses


cup = Editor()
cup.add_buffer("blah", "trial text, will it go in?")
cup.add_buffer("bloop", "more trial text, just some stuff blah blah bloo bloo")
cup.buffer_list()
testtext = cup.switch_buffer("blah")
cup.switch_buffer("bloop")
cup.switch_buffer("blah")
cup.close()

print(testtext)
