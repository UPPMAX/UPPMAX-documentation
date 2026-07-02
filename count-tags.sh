#!/bin/bash
#
# A oneliner to count the tags in the tags.json file
jq '.[].[].tags.[] ' tags.json | sort | uniq -c | sort -n
