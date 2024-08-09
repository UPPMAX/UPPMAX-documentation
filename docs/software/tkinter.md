# Tkinter

Tkinter is a package built with (every!) Python executable.

## Use Tkinter

Load a Python module:

```bash
module load python/3.12.1
```

Start Python:

```bash
python
```

Import `thkinter` in Python:

```bash
import tkinter
```

## History

In January 2024, there was a [Tkinter UPPMAX ticket](https://github.com/richelbilderbeek/ticket_286232).
and documentation how to load `tkinter`.

At that time, doing:

```bash
module load python/3.11.4
```

and then in Python:

```python
import turtle
```

results in:

```console
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/sw/comp/python3/3.11.4/rackham/lib/python3.11/turtle.py", line 107, in <module>
    import tkinter as TK
  File "/sw/comp/python3/3.11.4/rackham/lib/python3.11/tkinter/__init__.py", line 38, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
    ^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named '_tkinter'
```

With the application experts, we found out that `python` version `3.11.4`
did not have `tkinter` built in. That Python version was rebuilt.
Now all that is needed is to load a Python version and do a regular `pip install`.
That is, this solution should work:

## Links

* [Wikipedia page on Tkinter](https://en.wikipedia.org/wiki/Tkinter)
