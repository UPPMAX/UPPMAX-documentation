#!/bin/bash
#
# Remove trailing spaces of all .md files,
# as is recommended by the Markdown checker.
#
# Usage:
#
#   ./scripts/remove_trailing_spaces.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/remove_trailing_spaces.sh"
    echo " "
    exit 42
fi

# We are at the root folder

find . -type f | grep "\\.md$" | xargs -0 perl -pi -e 's/ +$//'
