# How can I display my disk quota?

To limit the amount of disk space each user can allocate we use a disk quota system at UPPMAX. The default disk quota is 32 GByte in your home directory. Every NAISS-project also comes with a default 128 GByte backed-up project storage. If more data is needed you may apply for an UPPMAX Storage Project and get more quota. UPPMAX project have a default 512 GByte backed-up project storage and a and 512 GB nobackup space.

You can display your current usage with the command [uquota](../software/uquota.md).

When you exceed your quota, the system will not let you write any more data and you have to either remove some files or request more quota. The 'uquota' command will also show the date and to what limit your quota will change to, if you have been given a larger quota.

Before contacting support, clean out unnecessary data and make an inventory of
the data in your project (what type of data, how big, why it's needed).
Here are two commands:

```bash
du -b $PWD | sort -rn | awk 'NR==1 {ALL=$1} {print int($1*100/ALL) "% " $0}'
```

This first command results in a list of subdirectories ordered
by size and proportion of total size.


```bash
find $PWD -print0 -type f | xargs -0 stat -c "%s %n" | sort -rn
```

This second command produces a list of the files in the current directory
that take up most space. These may take a long time to complete, use `CTRL + C`
to cancel execution if you change your mind.

After these two checks,
to get more disk space, [contact support](../support.md)
and state how much, for how long time, and why you need it.
See the storage project application page for more information
on how we handle and prioritise storage requests.

You should also read the [Disk Storage Guide](disk_storage_guide.md).
