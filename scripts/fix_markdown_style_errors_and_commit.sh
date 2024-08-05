#!/bin/bash
#
# Fix markdown style errors and commit.
#
# Usage:
#
#   ./scripts/fix_markdown_style_errors_and_commit.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/fix_markdown_style_errors_and_commit.sh"
    echo " "
    exit 42
fi

git add .
git commit -m "Before fixing markdown style"
./scripts/fix_markdown_style_errors.sh
git add .
git commit -m "Fix markdown style"
