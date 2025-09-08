#!/bin/bash
#
# Count the number of Markdown lines.
#
# Usage:
#
#  ./scripts/count_lines.sh
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/count_lines.sh"
    echo " "
    exit 42
fi

find . | grep -c "\\.md$"
