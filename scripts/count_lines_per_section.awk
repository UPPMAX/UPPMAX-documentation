# Counts non-empty lines in each ## level section
#
# Written by an AI, tested by a human - this code may not handle corner cases

function is_empty(s){ return s ~ /^[[:space:]]*$/ }

$0 ~ /^##[[:space:]]/ {
  if (cur != "") print cur ": " count
  cur=$0; count=0
  next
}

{
  if (cur != "" && !is_empty($0)) count++
}

END { if (cur != "") print cur ": " count }
