#!/bin/bash
#
# A simple pipeline to count the tags in the tags.json file
jq '.[].[].tags.[] ' tags.json |
	sort |
	uniq -c |
	sort -nr > tags-counted.txt
