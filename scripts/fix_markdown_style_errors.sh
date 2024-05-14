#!/bin/bash
#
# Fix markdown style errors,
# as is recommended by the Markdown checker.
#
# Usage:
#
#   ./scripts/fix_markdown_style_errors.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/fix_markdown_style_errors.sh"
    echo " "
    exit 42
fi

#
# This is too powerful, as it unindents:
#
#########################################
# ???- question "A question?"
#
#     Some text that needs to be indented
#########################################
#
# to
#
#########################################
# ???- question "A question?"
#
# Some text that needs to be indented
#########################################
#

# markdownlint --fix '**/*.md' --ignore node_modules --fix

# ./scripts/remove_trailing_spaces.sh
