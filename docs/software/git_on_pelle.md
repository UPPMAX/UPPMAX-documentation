# Using git on Pelle

Git is a version control tool made for code but equally useful with other text
format files, such as config files, scripts, notes and many input data file
formats. Version control is needed for reproducibility when the same files are
used in multiple versions, being updated and worked on over time. Therefore you
may already be using it for files that you want to use on Pelle.

Using `git push` and `git pull` can be a good way to transfer updates to files
to/from Pelle.

## Caveats

If your files are binary (not in a text format) or if your files are not being
updated, this is not the right tool for your file transfer needs.

Due to our storage setup limitations, git on Pelle can only be recommended for
relatively small sets of files.

If either of these caveats apply, we advise that you
[use rsync](pelle_file_transfer_using_rsync.md)
instead for keeping files on Pelle in sync with files elsewhere.


!!!- info "Other file transfer tools"

    See [the other ways to transfer data to/from Pelle](../cluster_guides/transfer_pelle.md)

!!!- warning "The risk of a large number of files"

    Git works by splitting the data into multiple small files and referencing
    them cleverly. For large repos and deep histories this results in a large
    number of small files. Our storage setup is not performant for such
    workloads, wherefore we have a quota not only on storage space but also on
    number of files.

    If git actions are slow it is an indicator that your repository is becoming
    too large for our storage system.

### No secrets on Pelle

!!!- warning "Pelle is not considered a secure system"

    It is not advisable to store any secrets, such as ssh keys or access tokens,
    on Pelle.

This means that you cannot push from Pelle to e.g. Github. Instead you can setup
Pelle as a remote to push to and pull from with your local computer, with no
keys stored on Pelle.

## Setting up a git repo on Pelle as a remote

Here is one good way to set up a copy of a git repository you have on your local
computer as a remote on Pelle:

### 1. Start a terminal on your local computer

Start a [terminal](../software/terminal.md) on your local computer.

### 2. Connect to Pelle with `ssh`

In the terminal, run `ssh` to connect to Pelle by doing:

```bash
ssh [username]@pelle.uppmax.uu.se
```

where `[username]` is your UPPMAX username, for example:

```bash
ssh sven@pelle.uppmax.uu.se
```

If asked, give your UPPMAX password and your second factor TOTP.

### 3. Create the folder to hold your repo on Pelle

```
mkdir myRepo
```

This example uses `~/myRepo` to keep it short. You can use any path in your home
folder or project storage. On project storage, you can use git for
collaborating.

### 4. Initialize and configure the git repo on Pelle

```
cd myRepo
git init
git config receive.denyCurrentBranch updateInstead
```

The command `git init` sets up the folder as a git repository.

This `git config` command sets it up so that you can push to it, but you can
also work with the files and git directly in this folder (as opposed to a
so-called bare repository, as is used on git servers).

### 5. Log out from Pelle (or open a second terminal)

Ctrl+D or `exit` or `logout`.

### 6. Set up the path on Pelle as a remote in your local repo

Navigate to the folder that holds the repository on your local computer. In that
folder, run:

```
git remote add pelle [username]@pelle.uppmax.uu.se:~/myRepo
```

This adds a remote named `pelle` referring to a URL specifying your user,
Pelle's full hostname and your chosen path on Pelle. Git automatically uses ssh
to set up the connection when the URL follows this pattern (instead of https if
it is an https URL).

Note that the path you give here needs to either start with `~` referring to
your home folder or `/` referring to the root of the system, i.e. it needs to be
a full path (there is no current directory on Pelle in this context to start a
relative path from).

To check the URL:s of all remotes you have set up (in this repo) use
`git remote -v`.

### 7. Push the current version of the repo to Pelle

```
git push
```

Done! Now you have this repo on Pelle as well.

You cannot push to anywhere from Pelle, but you can push to Pelle and pull from
Pelle with your local computer. And you can clone directly from Pelle if you
need to work with this repo from more computers.
