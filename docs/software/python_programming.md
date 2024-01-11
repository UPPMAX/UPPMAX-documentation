# Python programming

This page describes how to program in [Python](python.md)
on the [UPPMAX clusters](../cluster_guides/uppmax_cluster.md).

There are multiple ways to program in Python:

Description               |Features
--------------------------|------------------------------------------
Use a text editor         |Non-interactive, no help
Use the Python interpreter|Interactive, terminal-based, some help
Use IPython               |Interactive, terminal-based, more help and features
Use Jupyter               |Interactive, web-based
Use Visual Studio Code    |Interactive, install on local computer, use locally installed Python and Python packages

## Use a text editor

Using a text editor to program in Python 
is a simple way to write code: 
it is the same as writing any text file. 

Here we use the text editor GNU nano to write a Python script:

```
nano example_script.py
```

Within nano, write:

```
print('Hello, world!')
```

- To save, press `CTRL + O` (i.e. the letter), then enter to keep the same filename
- To quite, press `CTRL + Q`

You can run this Python script in the shell by:

```console
python example_script.py 
```

or, if you want to be explicitly use Python 3:

```console
python3 example_script.py 
```

Some features of this approach are:
- this is a simple way to write code: it is the same as writing any text file. 
- you get no help while writing code
- you can only run the script from start to finish, i.e. you cannot
  partially run the script

???- question "How to run a Python script line-by-line?"

    You can run a Python script line-by-line using a Python debugger, 
    such as `pdb`.

    On the terminal, for `python`, do:

    ```
    pdb example_script.py 
    ```

    or for `python3`:

    ```
    pdb3 example_script.py 
    ```

    See the official Python documentation of `pdb` [here](https://docs.python.org/3/library/pdb.html).

### Use the Python interpreter

You start the Python interpreter by typing:

```console
$ python
```

or (for explicit Python 3):

```console
$ python3
```

The Python prompt looks like this:

```python
>>>
```

Type, for example:

```
print('Hello, world!')
```

and the interpreter will run the statement.

Exit the Python interpreter with `<Ctrl-D>`, `quit()` or `exit()`.

Some features of this approach are:

- you get limited help while writing code

???- question "How do I get help?"

    As an example, writing this line of code in the Python interpreter ...

    ```
    s = 'Hello, world!'
    ```

    ... and press enter. Now a variable called `s` will hold some text.

    Now type ...

    ```
    s.
    ```

    and press Tab twice. You will see a list of things you can do with that string.
    
- you can only run the script from start to finish, i.e. you cannot
  partially run the script


## Use IPython               

Some features are:

- interactive
- terminal-based
- more help and features

## Use Jupyter               

Some features are:

- interactive
- web-based

## Use Visual Studio Code    

Some features are:

- interactive
- install on local computer
- use locally installed Python and Python packages

## Links

* [Official Python documentation](https://docs.python.org/3/)
* [Python forum](https://www.python.org/community/forums/)
* [Free online book: 'How to Think Like a Computer Scientist'](https://openbookproject.net/thinkcs/python/english3e/index.html)
* [UPPMAX TensorFlow guide](https://www.uppmax.uu.se/support/user-guides/tensorflow-user-guide/)
* [UPPMAX PyTorch guide](https://www.uppmax.uu.se/support/user-guides/nvidia-deep-learning-frameworks/)


