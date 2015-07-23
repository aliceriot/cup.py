from editor import Editor
from curses import textpad
import curses
import sys
import os

### initialization, create editor object and initialize buffers
cup = Editor()
files_to_open = sys.argv[1:]
for to_open in files_to_open:
    if (os.path.isfile(to_open)):
        with open(to_open) as myfile:
            cup.add_buffer(to_open, myfile.read())
    else:
        cup.add_buffer(to_open, '')
    if cup.current_buffer == '':
        cup.current_buffer = to_open
cup.buffer_list(cup.current_buffer)


cup.switch_buffer(sys.argv[1])
# cup.add_buffer("bloop", "more trial text, just some stuff blah blah bloo bloo")
# cup.buffer_list()
# testtext = cup.switch_buffer("blah")
# # with open("test.txt", "w") as myfile:
# #     myfile.write(testtext)
# cup.switch_buffer("bloop")
# cup.switch_buffer("blah")
cup.close()

# print(testtext)
