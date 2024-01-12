# Text editors

There are many editors that can be used on the UPPMAX clusters:

Editor type                                                 |Features
------------------------------------------------------------|-----------------------------------------------------
[Simple terminal editors](#simple-terminal-editors)         |Used in terminal, easy to learn, limited features
[Advanced terminal editors](#advanced-terminal-editors)     |Used in terminal, harder to learn, powerful features
[Simple graphical editors](#simple-graphical-editors)       |Graphical, needs X-forwarding, easy to learn, limited features
[Advanced graphical editors](#advanced-graphical-editors)   |Graphical, needs X-forwarding, harder to learn, powerful features

Try them out and pick one favorite editor!

!!! tip

    **These commands are useful in the command line when something is stuck or a program is limiting you to do further work.**

    - ``ctrl-C`` interrupts a program or a command that is "stuck"
    - ``ctrl-D`` quits some programs from the program environment in the terminal
    - ``ctrl-Z`` pauses a program, can be continued in background (`bg`) or  foreground (`fg`)

## Simple terminal editors

### nano 

`nano` is a simple terminal editor that is easy to learn.

Start `nano` on a terminal with:

```
nano
```


- keyboard shortcuts shown on-screen
- [Cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html) 
  - ^ = Ctrl, M = meta key)
    - Windows M = Alt
    - On Mac: in the Terminal.app go to Preferences -> Settings -> Keyboard and turn on "Use option as meta key": then M = Alt

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

- work on an UPPMAX cluster that allows X-forwarding
- login with X-forwarding enabled

See the 'How to login to Rackham' page [here](../getting_started/login_rackham.md)
how to do so.

???- question "And what about Bianca?"

    Bianca is an UPPMAX cluster that does not allow X-forwarding.

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
