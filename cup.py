from editor import Editor
import curses
import sys
import os

### create editor object, initialize with files to open, listen for keypresses
cup = Editor()
cup.initialize(sys.argv[1:])
cup.listen()
