#!../uppmax_venv/bin/python

import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup
from gtts import gTTS
from markdown import markdown


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Markdown file to convert")
    parser.add_argument(
        "-l", "--lang", type=str, default="en", help="Language to convert to"
    )
    return parser.parse_args()


def markdown_to_text(md):
    """Converts a markdown string to plaintext
    and remove elements that should not be read"""

    html = markdown(md)

    # remove code trash
    html = re.sub(r"<pre>(.*?)</pre>", " ", html)
    html = re.sub(r"<code>(.*?)</code >", " ", html)
    html = re.sub(r"<p>\?\?\? (.*?)", " ", html)
    html = re.sub(r"\|-(.*)", " ", html)
    html = re.sub(r"```(.*)", " ", html)
    html = re.sub(r"t2s(.*)", " ", html)
    html = re.sub(r"-([a-zA-Z])", r"dash-\1", html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    plain_txt = "".join(soup.findAll(text=True))

    # Substitutes
    subs = [
        ("UPPMAX", "uppmax"),
        ("et.c.", "etcetera"),
        ("e.g.", "for example"),
        ("SBATCH", "s-batch"),
        ("srun", "s-run"),
        ("srun", "s-run"),
        ("scancel", "s-cancel")
    ]

    for m, s in subs:
        plain_txt = plain_txt.replace(m, s)

    return plain_txt


if __name__ == "__main__":
    args = parse_args()

    p = Path(args.input)
    with open(p, "r") as f:
        md = f.read()

    text = markdown_to_text(md)
    print("Parsed text")
    print("==" * 33)
    print(text)
    a = gTTS(text=text, lang=args.lang)
    a.save(p.with_suffix(".mp3"))
