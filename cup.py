from editor import Editor
import curses
import sys
import os

### initialization, create editor object and initialize buffers
cup = Editor()

# this should be a method too...
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
cup.switch_buffer(cup.current_buffer)

# the listen method handles the rest!
cup.listen()
