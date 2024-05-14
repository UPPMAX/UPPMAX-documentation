# Text editors

There are many editors that can be used on the UPPMAX clusters:

Editor type                                                 |Features
------------------------------------------------------------|-----------------------------------------------------
[Simple terminal editors](#simple-terminal-editors)         |Used in terminal, easy to learn, limited features
[Advanced terminal editors](#advanced-terminal-editors)     |Used in terminal, harder to learn, powerful features
[Simple graphical editors](#simple-graphical-editors)       |Graphical, needs [X forwarding](../software/ssh_x_forwarding.md), easy to learn, limited features
[Advanced graphical editors](#advanced-graphical-editors)   |Graphical, needs [X forwarding](../software/ssh_x_forwarding.md), harder to learn, powerful features

Try them out and pick one favorite editor!

!!! tip

    **These commands are useful in the command line when something is stuck or a program is limiting you to do further work.**

    - ``ctrl-C`` interrupts a program or a command that is "stuck"
    - ``ctrl-D`` quits some programs from the program environment in the terminal
    - ``ctrl-Z`` pauses a program, can be continued in background (`bg`) or  foreground (`fg`)

## Simple terminal editors

### GNU nano

???- question "Want to see a video?"

    You can find a video on using nano on Rackham [here](https://youtu.be/Ntg0sjBQA0E)

GNU nano is a simple terminal editor that is easy to learn.

Start nano on a terminal with:

```
nano
```

The keyboard shortcuts are shown on-screen,
where `^` denotes `Ctrl` and `M` the meta key.

- On Windows, `Alt` is the meta key
- On Mac: in the `Terminal.app`, go to 'Preferences -> Settings -> Keyboard'
  and turn on "Use option as meta key", after which `Alt` is the meta key

See a nano cheat sheet [here](https://www.nano-editor.org/dist/latest/cheatsheet.html).

## Advanced terminal editors

!!! warning

    - we suggest that you learn this tools before trying to work with them on UPPMAX
    - If you start one of these editors you may have difficulties to exit!

### vim

`vim` is an advanced terminal editor that is fast fast and powerful, once you learn it.

Start `vim` on a terminal with:

```
vi
```

Then:

- 1. Insert mode (type like normal text editor. Press ``i`` for insert mode)
- 2. Command mode (give commands to the editor to get things done . Press `<ESC>` for command mode)
- Cheat sheet: [https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started](https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started)

### emacs

`emacs` is an advanced terminal editor that is fast fast and powerful, once you learn it.

Start `emacs` on a terminal with:

```
emacs
```

Then:

- Cheat sheet: [https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf](https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf)
  - (C = `<Ctrl>`)
- also With GUI
  - ``emacs –nw``
    - keeps you in terminal window.

## Simple graphical editors

To use a graphical editors you will need to:

- work on an UPPMAX cluster that allows [SSH X forwarding](../software/ssh_x_forwarding.md)
- login with [SSH X forwarding](../software/ssh_x_forwarding.md) enabled

See the [SSH X forwarding page](../software/ssh_x_forwarding.md) how to do so.

???- question "And what about Bianca?"

    Bianca is an UPPMAX cluster that does not allow [X forwarding](../software/ssh_x_forwarding.md).

    See the 'How to login to Bianca' page [here](../getting_started/login_bianca.md)
    for more details.

### gedit

- graphical user interface — GUI, needs X-server
- Also graphical editor within MobaXterm

- When starting the graphical versions of an editor, add ``&`` to be able to use the command line while program is open.
  - Ex: `gedit &`
  - If not, you can `<Ctrl>+z` and type `bg` to send program to background.

## Advanced graphical editors

### gvim

- ``vim`` with a GUI, lots of features, very fast
