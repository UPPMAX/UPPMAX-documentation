# Software on Transit

[Transit](../cluster_guides/transit.md) 
is an UPPMAX service that can be used to securely transfer files.

This page describes the software on [Transit](../cluster_guides/transit.md).

After [logging in to Transit](../cluster_guides/login_transit.md),
you cannot make lasting changes to anything, 
except for mounted [wharf](../cluster_guides/wharf.md) directories. 
However, anything you have added to your [Rackham](../cluster_guides/rackham.md) home directory 
is available on [Transit](../cluster_guides/transit.md). 

In addition, some modules are available.

 * SciLifeLab Data Delivery System - [https://delivery.scilifelab.se/](https://delivery.scilifelab.se/)

    ```bash
    # Load the tool from the software module tree
    module load bioinfo-tools dds-cli

    # Run the tool
    dds
    ```
  ![dds-cli](../img/dds-cli.png)

To download data from TCGA, 
[log in to Rackham](../getting_started/login_rackham.md) 
and install the GDC client to your home directory. 
Then [log in to Transit](../cluster_guides/login_transit.md), 
mount the [wharf](../cluster_guides/wharf.md), 
and run `./gdc-client`.

!!! warning "2FA on transit"

    If you connect from abroad and 
    you are asked for the **2FA** (_two factor authentication_), 
    there is a grace period (_about 5 minutes_) in which you can 
    `ssh`/`scp`/`rsync`/`sftp` to **transit** without the need for **2FA**. 
    This allows you to use these and other tools 
    that might experience problems with the **2FA**.
