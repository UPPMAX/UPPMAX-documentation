#!/bin/bash
#
# Create the software table.
#
# The software table is generated on each deploy on GitHub actions,
# so you have to do that manually if you want to view it locally:
#
# Usage:
#
#   ./scripts/create_software_table.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/create_software_table.sh"
    echo " "
    exit 42
fi

python3 scripts/sw_table_md_creator.py -i https://export.uppmax.uu.se/staff/software_table_ci/software_table.json -o docs/software/software-table.md
