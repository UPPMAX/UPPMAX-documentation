# Counts non-empty lines within section "## Sources"
#
# Probably doesn't work if there isn't a single matching section,
# I checked that all files had that by
#   $ ls -1 | wc -l
#   $ grep -c "## Sources" * | grep -c ":1"
# giving the same count. The latter is a surprisingly slow command.

function is_empty(s){ return s ~ /^[[:space:]]*$/ }

$0 ~ /^##[[:space:]]Sources/ {
  in_sources = 1
  count = 0
  next
}

$0 ~ /^##[[:space:]]/ && in_sources {
  in_sources = 0
}

in_sources && !is_empty($0) {
  count++
}

END {
  if (in_sources || count > 0)
    print FILENAME ": " count
}

