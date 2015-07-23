#Cup

It's called Cup because it was going to be a Vim clone, so Python Vim ->
Pim, which made me think of Pim's cup. So it's Cup!

Anyway, do:

```
python3 cup.py myfile.txt
```

You can almost use this in a useful way! Kind of, there are many
limitations which I need to work out, like using a pad instead of a window
for the text field.

Cup supports editing multiple files, each lives in it's own buffer (sort
of like Vim). Cup also has command and edit modes. When you first open Cup
you'll be in edit mode - the key to get out is `C-g`, which will drop you
into command mode. From there you can press `i` to keep editing the
current buffer, you can press `q` to quit the application, or you can type
`b` to switch to another buffer. This will prompt you for the buffer name:
currently you need to type it exactly or it will crash.

Cool!

Cup is written in standard library Python, mostly using the
[curses](https://docs.python.org/3.4/library/curses.html) library.
