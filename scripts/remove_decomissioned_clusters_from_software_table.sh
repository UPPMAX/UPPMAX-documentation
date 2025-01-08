#!/bin/bash
#
# Removes all decomissioned clusters from the software table
#
# A hack until https://github.com/UPPMAX/UPPMAX-documentation/issues/93
# is done properly.
#
# Usage:
#
#   ./scripts/remove_decomissioned_clusters_from_software_table.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "FATAL ERROR."
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "  ./scripts/remove_decomissioned_clusters_from_software_table.sh"
    echo " "
    exit 42
fi

sed -i 's/Irma, //g' docs/software/software_table.html
sed -i 's/Miarka, //g' docs/software/software_table.html
sed -i 's/Irma//g' docs/software/software_table.html
sed -i 's/Miarka//g' docs/software/software_table.html
