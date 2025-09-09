#!/bin/bash
#
# Count the number of pages with tags.
#
# Usage:
#
#  ./scripts/count_n_pages_with_tags.sh
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/count_n_pages_with_tags.sh"
    echo " "
    exit 42
fi

grep -ER "^tags:$" --include=*.md | wc --lines
