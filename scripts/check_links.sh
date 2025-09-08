#!/bin/bash
#
# Check links
#
# Usage:
#
#   ./scripts/check_links.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/check_links.sh"
    echo " "
    exit 42
fi

markdown-link-check --config mlc_config.json --quiet "docs/**/*.md"
