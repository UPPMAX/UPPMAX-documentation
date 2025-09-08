#!/bin/bash
#
# Count the number of Mermaid graphs.
#
# Usage:
#
#  ./scripts/count_n_mermaid_graphs.sh
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/count_n_mermaid_graps.sh"
    echo " "
    exit 42
fi

egrep -R "mermaid$" --include=*.md | wc --lines
