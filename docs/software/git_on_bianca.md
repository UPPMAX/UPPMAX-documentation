# Git on Bianca

NOTE: This guide assumes you know basic git commands and will not cover how to use git as a tool.

- One of the security features of Bianca is that there is no internet access from the cluster.
- This makes it a bit more complicated to use things like Git to collaborate on files.
- In this guide we will cover two use-cases:

    1. collaborate with other users within the same Bianca project, and
    1. collaborate with other users using Github.

## Within the same Bianca project

Usually an external service like GitHub is used to host a remote repository (repo) that everyone pushes and pulls from. Since we don’t have an internet connection on Bianca we have to push and pull from a location within your Bianca project. Luckily that is simple to setup with git.

To create your own remote repo that everyone will push and pull from, create an empty directory somewhere in your project folder, go into it and initialize the repo.

```console
# go to project dir
cd /proj/nobackup/sens2023999/

# create dir
mkdir my_repo.git

# go into dir
cd my_repo.git

# init repo
git init --bare --share=group
```

The name of the created directory doesn’t have to end with .git but it is good for us humans to indicate that this is a repo people will use to push and pull from, and not where you will manually edit files.

To start using this repo you will clone it just like you would clone a GitHub repo.

```console
# go to where you want to clone the repo, e.g. your home
cd ~/

# clone it
git clone /proj/nobackup/sens2023999/my_repo.git

# add a file and make the first commit
echo "# my_repo" >> README.md
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
```

Now you will have a new directory named my_repo that only has a README.md file, and you can start creating other files in there. From this point onwards git will work the same way as if you were using a GitHub hosted repo to collaborate. Once you have pushed your files the others in your project can clone the repo and start pushing and pulling their changes.

## Using Github (or any other git hosting service)

These instructions will work with any git hosting provider, like GitLab or Bitbucket, but we’ll use GitHub in the examples.

In the examples we use Rackham to mount the wharf directory. This is not the only way to do it. If you’d rather use a sftp client to transfer your files from the outside of Bianca to and from the wharf it will work just as well.

### Cloning and pulling only

If you only want to run someone else's software that they have stored in a GitHub repo, you only need to clone the repo to be able to use it. Since you are only a user of the software there is no need to be able to push to the repo. If there are any updates to the repo you only need to pull the repo to get them.

The way to do this on Bianca is to simply clone the repo on a computer with internet access, move it to the Bianca wharf, and then copy it to its final destination on Bianca. If there are any updates to the repo you want to get you move the repo back to the wharf, pull the updates to the mounted wharf directory on Rackham, then move the directory back to its final destination on Bianca.

```console
### on rackham ###

# set variables for readability
PROJ=sens2023999
UNAME=youruppmaxusername

# mount the wharf directory
mkdir -p ~/wharf_mnt
/proj/staff/dahlo/bin/sshfs $UNAME-$PROJ@bianca-sftp.uppmax.uu.se:$UNAME-$PROJ ~/wharf_mnt

# clone the repo to the wharf directory
cd ~/wharf_mnt
git clone git@github.com:example/example.git

### on Bianca ###

# move the directory to its final destination on Bianca

mv /proj/$PROJ/nobackup/wharf/$UNAME/$USER-$PROJ/example/ /proj/$PROJ/
```

If there are any updates to the software you might want to pull the changes from GitHub.

```console
### on bianca ###

# move the directory you cloned from GitHub back to the wharf
mv /proj/$PROJ/example/ /proj/$PROJ/nobackup/wharf/$UNAME/$USER-$PROJ/

### on rackham ###

# mount the wharf directory
mkdir -p ~/wharf_mnt
/proj/staff/dahlo/bin/sshfs $UNAME-$PROJ@bianca-sftp.uppmax.uu.se:$UNAME-$PROJ ~/wharf_mnt

# pull the updates
cd ~/wharf_mnt/example
git pull

### on bianca ###

# move the directory to its final destination on Bianca
mv /proj/$PROJ/nobackup/wharf/$UNAME/$USER-$PROJ/example/ /proj/$PROJ/
```

### Pushing and pulling

If you are a collaborator on a software you will need to do both pulling and pushing to the repo

The general approach to using git as a collaborator with GitHub on Bianca is:

1. On Bianca: make a backup of your code directory.
1. On Bianca: move the entire code directory to the wharf folder.
1. On Rackham: mount the wharf directory.
1. On Rackham: change the git remote URL to GitHub’s URL.
1. On Rackham: pull and push from GitHub.
1. On Bianca: move the directory from the wharf back to your project.
1. On Bianca: change the git remote URL back to your local Bianca repo.
1. On Bianca: push any changes you got from GitHub to your local Bianca repo.

Best way to show this is by an example:

```console
### on bianca ###

# set variables for readability
PROJ=sens2023999
UNAME=youruppmaxusername

# make a copy of your code dir, delete this later if all goes well :)
cp -ar /proj/$PROJ/code_dir /proj/$PROJ/code_dir.$(date +%Y-%m-%d)

# move the directory with your code to the wharf
mv /proj/$PROJ/code_dir/ /proj/$PROJ/nobackup/wharf/$UNAME/$UNAME-$PROJ/

### on rackham ###

# set variables for readability
PROJ=sens2023999
UNAME=youruppmaxusername

# mount the wharf folder
mkdir -p ~/wharf_mnt
/proj/staff/dahlo/bin/sshfs $UNAME-$PROJ@bianca-sftp.uppmax.uu.se:$UNAME-$PROJ ~/wharf_mnt

# update the remote repo's URL to your GitHub URL
cd ~/wharf_mnt/code_dir
git remote set-url origin git@github.com:example/example.git
git pull
git push

### on bianca ###

# move the directory back from the wharf
mv /proj/$PROJ/nobackup/wharf/$UNAME/$USER-$PROJ/code_dir/ /proj/$PROJ/

# change the remote repo's URL back to your local repo on Bianca
git remote set-url origin /path/to/local/repo

# push any changes you got from GitHub to your local repo
git push

```
