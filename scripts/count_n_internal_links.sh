#!/bin/bash
#
# Count the number of internal links.
#
# Usage:
#
#  ./scripts/count_n_internal_links.sh
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/count_n_internal_links.sh"
    echo " "
    exit 42
fi

grep -ER "\\.md\\)" --include=*.md | wc --lines
