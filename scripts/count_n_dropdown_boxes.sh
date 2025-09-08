#!/bin/bash
#
# Count the number of dropdown boxes.
#
# Usage:
#
#  ./scripts/count_n_dropdown_boxes.sh
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/count_n_dropdown_boxes.sh"
    echo " "
    exit 42
fi

egrep -R "\\?\\?\\?" --include=*.md | wc --lines
