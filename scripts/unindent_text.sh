#!/bin/bash
#
# Unindents text in all markdown files
#
# For an indented block, a link to a broken image is ignored, as the link checker assumes it to be code.
# In our case, it is not: for us, it is usually an admonition (i.e. a 'question' or 'info' block)
# Here all indented text is unindented
# https://github.com/UPPMAX/UPPMAX-documentation/issues/114
#
# Usage:
#
#   ./scripts/unindent_text.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/unindent_text.sh"
    echo " "
    exit 42
fi

for filename in $(find . | grep .md)
do
sed -i 's/^    //g' "${filename}"
sed -i 's/^    //g' "${filename}"
sed -i 's/^    //g' "${filename}"
done
