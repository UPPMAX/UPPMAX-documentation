#!/bin/bash
#
# Indents 3 spaces to 4 spaces.
#
# For an indented block, a link to a broken image is ignored, as the link checker assumes it to be code.
# In our case, it is not: for us, it is usually an admonition (i.e. a 'question' or 'info' block)
# Here all indented text is unindented
# https://github.com/UPPMAX/UPPMAX-documentation/issues/114
#
for filename in $(find . | grep .md)
do
# Three spaces at the start of a line (`^   `), followed by a non-space (`[^ ]`)
sed -i 's/^   ([^ ])/ \1/g' ${filename}
done
