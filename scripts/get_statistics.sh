#!/bin/bash
#
# Get some statistics about these pages
#
# Usage:
#
#  ./scripts/get_statistics.sh
# 
if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/get_statistics.sh"
    echo " "
    exit 42
fi


echo "Number of lines"
./scripts/count_lines.sh

echo "Number of dropdown boxes"
./scripts/count_n_dropdown_boxes.sh

echo "Number of images"
./scripts/count_n_images.sh

echo "Number of internal links"
./scripts/count_n_internal_links.sh

echo "Number of Mermaid graphs"
./scripts/count_n_mermaid_graphs.sh

echo "Number of pages with (search) tags"
./scripts/count_n_pages_with_tags.sh

echo "Number of YouTube videos"
./scripts/count_n_youtube_videos.sh

echo "Number of pages"
./scripts/count_pages.sh
