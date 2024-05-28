# How do I install local Perl packages?

## What is available already in the perl modules?

- A number of packages are available by default with all Perl versions. 

- For Perl version 5.18.4 in particular (available through the software module system as `perl/5.18.4`), we have installed many more Perl packages. These are available by loading the software module `perl_modules/5.18.4`. We have a [complete list of the Perl packages available](perl.md#perl-module-search-on-perl_modules5262rackham).

- If you would like to use [**BioPerl**](https://bioperl.org/), `module avail BioPerl` after loading bioinfo-tools will show the versions available. The latest is `BioPerl/1.6.924_Perl5.18.4`, which is built against Perl `5.18.4` so also loads the modules `perl/5.18.4` and `perl_modules/5.18.4`.

## Install other packages

You could email support at support@uppmax.uu.se and suggest we include the package in `perl_modules`. If that doesn't work, or you decide to install it for yourself, please keep reading.

First you have to decide where you want to put your local Perl packages. Save this in a temporary environment variable called MY_PERL, make sure to substitute the path with your own:

```bash
export MY_PERL=/home/johanhe/slask/perl/
```

Then we download and install a more light weight CPAN client called cpanm, which have less confusing settings to configure and also makes it easier to install local packages. We'll then also install the module local::lib to a directory of your choice:

```bash
wget -O- http://cpanmin.us | perl - -l $MY_PERL App::cpanminus local::lib
```

Now we should be ready to set up the correct environment variables and load them for this session:

```bash
echo "eval `perl -I $MY_PERL/lib/perl5 -Mlocal::lib=$MY_PERL`" >> ~/.bash_profile 
echo "export PATH=$MY_PERL/bin/:$PATH" >> ~/.bash_profile 
source ~/.bash_profile
```

After this is done we can always install local packages easily by using the command:

```bash
cpanm [name-of-package-to-install]
```bash

