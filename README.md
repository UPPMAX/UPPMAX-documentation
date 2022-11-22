# UPPMAX Userguide

## Getting started

To work on the website locally first create a virtual environment and install
the required dependencies

``` bash
python -m venv uppmax_venv
source uppmax_venv/bin/activate
pip install -r requirements.txt
```

Then serve the website and software table by running

``` bash
python sw_table.py
```
under `/scripts` and then serve the website by

``` bash
mkdocs serve
```

## Text-to-speech


The script `md_to_speech.py` takes an `.md` file, parses the text and generates
an mp3 using [`gTTS`](https://gtts.readthedocs.io/en/latest/). Run it by
 

```
python md_to_speech.py --input txt.md --lang en
```
