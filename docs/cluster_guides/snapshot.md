---
tags:
  - snapshot
  - snapshots
---

# Snapshot

Besides [the UPPMAX backup service](backup.md),
UPPMAX provides snapshot on your home folder.

Snapshot makes a frozen "picture" of some file structure as it looks at the time the snapshot was taken.
This allows you to restore a particular file as it was at some time point.

Snapshots reside on the same storage system as the original data. This means
that when the storage system fails catastrophically,
then the snapshots are gone as well.

Snapshots are taken on regular basis and only available for home directories.

You can easily access snapshots in every directory by
  `ls .snapshot` or `cd .snapshot` in a [terminal](../software/terminal.md).
  The `.snapshot` is a hidden directory that does not show up in `ls --all`.
