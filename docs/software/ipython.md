# IPython

`IPython` is a console program that extends
the regular [Python](python.md) interpreter:
among others, one can directly run scripts and re-use output.

???- question "Want to see a video?"

    Here are some videos on IPython:

    - [YouTube video on `python` versus `IPython`](https://youtu.be/lhi7s6RoIys?si=Z72gSIb6q3piucPH)
    - [YouTube video on `IPython`](https://www.youtube.com/watch?v=S9rgGJYAQ8o)

After loading a Python module, you also have the IPython Python command shell available.

???- question "Forgot how to load a Python module?"

    See the UPPMAX page about Python [here](python.md).

???- question "What is a Python command shell?"

    In computing, a shell is a a program around something,
    for example, Bash is a shell around a UNIX-like operating system.

    In computing, a command shell means that the shell
    is a command-line shell, i.e. text only.

    A Python command shell, hence, is a text-only program
    around Python.

Start the IPython command shell by typing:

```console
ipython
```

or (for explicit Python 3):

```console
ipython3
```

The `ipython3` prompt looks like this:

```python
[richel@rackham1 ~]$ ipython
Python 3.11.4 (main, Aug  7 2023, 16:05:58) [GCC 12.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.14.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

IPython allows one to write code interactively.

For example, in IPython, type:

```python
print('Hello, world!')
```

and IPython will show the result of that line of code.

IPython can interact with your file system.

???- question "How does IPython interact with the file system?"

    For example, within IPython, running ...

    ```python
    ls
    ````

    ... displays a list of files in your current working folder
    in the same way as Bash's `ls`.

    The Python interpreter will give an error if you do the same.

IPython has an auto-complete triggered by Tab.

???- question "How do I get auto-complete?"

    As an example, writing this line of code in IPython ...

    ```python
    s = 'Hello, world!'
    ```

    ... and press enter. Now a variable called `s` will hold some text.

    Now type ...

    ```python
    s.
    ```

    and press Tab. You will see a menu of things you can do with that string.
    Hold tab to scroll through the many options.

IPython can show graphics.

???- question "How do I get IPython to show graphics?"

    In IPython, run this code line-by-line:

    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4])
    plt.show()
    ```

    (or as a one-liner: `import matplotlib.pyplot as plt; plt.plot([1, 2, 3, 4]); plt.show()`)

    You will see a window appear:

    ![A window with the plot](img/ipython_matplotlib.png)

    You will only see a window appear, if you've logged in to Rackham with
    [SSH with X forwarding](../software/ssh_x_forwarding.md) enabled.

    Spoiler to login: `ssh -X sven@rackham.uppmax.uu.se`.

    Spoiler to confirm: run [`xeyes`](../software/xeyes.md).

IPython can directly run scripts.

???- question "How do I get IPython to directly run scripts?"

    In IPython, run:

    ```bash
    run [filename]
    ```

    where `[filename]` is the name of a file, for example:

    ```bash
    run my_script.py
    ```

    IPython will run the script and remember variables, functions and classes
    created in that script.
