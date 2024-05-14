# UPPMAX Documentation

[![check-links](https://github.com/UPPMAX/UPPMAX-documentation/actions/workflows/check_links.yaml/badge.svg?branch=main)](https://github.com/UPPMAX/UPPMAX-documentation/actions/workflows/check_links.yaml)
[![Check spelling](https://github.com/UPPMAX/UPPMAX-documentation/actions/workflows/check_spelling.yaml/badge.svg?branch=main)](https://github.com/UPPMAX/UPPMAX-documentation/actions/workflows/check_spelling.yaml)

This repository contains the source code for the [UPPMAX
documentation](https://uppmax.github.io/UPPMAX-documentation/)

## Contributing

Everyone is welcome to contribute either by creating a new issue or solving an
[existing one](https://github.com/UPPMAX/UPPMAX-documentation/issues) by submitting
a pull request. The recommended workflow for collaborators when working on an
issue is to:

1. Clone the [repository](https://github.com/UPPMAX/UPPMAX-documentation/issues)
2. Create a new branch where you add your changes
3. Push and submit a pull request
4. If the change is accepted after review it will be merged into the main
   branch

## Working on the documentation locally

To work on the website locally first create a virtual environment and install
the required dependencies

``` bash
python3 -m venv uppmax_venv
source uppmax_venv/bin/activate
pip install -r requirements.txt
```

Then activate the environment and serve the website on localhost

``` bash
mkdocs serve
```

## Optional dependencies

### Software table

Dependencies:

```bash
pip install natsort
```

The software table is generated on each deploy on GitHub actions,
so you have to do that manually if you want to view it locally:

``` bash
./scripts/create_software_table.sh
```

### Text-to-speech

Dependencies:

```bash
pip install beautifulsoup4\>=4.11.1 gTTS\>=2.2.4
```

The script `md_to_speech.py` takes an `.md` file, parses the text and generates
an mp3 using [`gTTS`](https://gtts.readthedocs.io/en/latest/). Run it by

```bash
python3 scripts/md_to_speech.py --input txt.md --lang en
```

## Files used by continuous integration scripts

Filename                              |Descriptions
--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------
[mlc_config.json](mlc_config.json)    |Configuration of the link checker, use `markdown-link-check --config mlc_config.json --quiet docs/**/*.md` to do link checking locally
[.spellcheck.yml](.spellcheck.yml)    |Configuration of the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally
[.wordlist.txt](.wordlist.txt)        |Whitelisted words for the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally
[.markdownlint.jsonc](.markdownlint.jsonc)|Configuration of the markdown linter, use `markdownlint "**/*.md"` to do markdown linting locally. The name of this file is a default name.
[.markdownlintignore](.markdownlintignore)|Files ignored by the markdown linter, use `markdownlint "**/*.md"` to do markdown linting locally. The name of this file is a default name.

## Test for markdown linter

???- question "What it it?"

    This is it.

    ```bash
    echo "This is it"
    ```

## Credits

The website is created using
[mkdocs-material](https://squidfunk.github.io/mkdocs-material). The landing
page and layout was inspired by the documentation of the HPC cluster
[LUMI](https://docs.lumi-supercomputer.eu/).



