#!/bin/bash
#
# Indents 3 spaces to 4 spaces.
#
for filename in $(find . | grep .md)
do
# Three spaces at the start of a line (`^   `), followed by a non-space (`[^ ]`)
  sed -i 's/^   ([^ ])/    \\1/g' ${filename}
done

echo "Cannot get this to work..."
