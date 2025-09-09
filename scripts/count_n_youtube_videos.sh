#!/bin/bash
#
# Count the number of YouTube videos.
#
# Usage:
#
#  ./scripts/count_n_youtube_videos.sh
# 
if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/count_n_youtube_videos.sh"
    echo " "
    exit 42
fi

grep -ER "youtu\\.be" --include=*.md | wc --lines

