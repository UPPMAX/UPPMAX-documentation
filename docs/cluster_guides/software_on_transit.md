# Software on Transit

>Update: 02.02.2026

[Transit](../cluster_guides/transit.md) is an UPPMAX service that can be used to securely transfer files.

The purpose of the transit server is to give users access to their wharf folders on Bianca/Maya on Linux running machine with certain limitations.

- **Users home folders are ephemeral**, i.e. any changes will be lost 5 minutes after last interactive login session. The **writable** portion of the home folder is **limited to 2.9GB**, **shared between all users**, which could lead to unexpected results when tools need to cache in their usual location (pip, conda, etc).
    ```bash
    df -h | grep  "home/\|Filesystem"
    
    Filesystem          Size  Used Avail Use% Mounted on
    overlay             2.9G  2.4G  580M  81% /gorilla/home/user_1
    overlay             2.9G  2.4G  580M  81% /gorilla/home/user_2
    overlay             2.9G  2.4G  580M  81% /gorilla/home/user_3
    ...
    ```
- Transit is **world-wide accessible**.
- **X11 and any port forwarding is disabled** i.e. graphical tools do not work.
- **The software module system of Pelle is available** on transit.
- **Apptainer is available** but users needs to redirect TMP and CACHE to their wharf folders. This solution leads to EXTREMELY slow builds. Pulling containers is not affected - it is as fast as saving to wharf.

   ```bash
   export APPTAINER_CACHEDIR=$HOME/sens2023531/APPTAINER_CACHE
   export APPTAINER_TMPDIR=$HOME/sens2023531/APPTAINER_TMP
   mkdir -p $APPTAINER_CACHEDIR $APPTAINER_TMPDIR
   ```

Below are some temporary solutions for commonly used tools.
Please, use the full path to run the tools.

- `nextflow` - `/sw/generic/pixi-tools/bin/nextflow`
- `nf-core` - `/sw/generic/pixi-tools/bin/nf-core`
- `dds-cli` - `/sw/generic/uv-tools/tool_bin/dds`
- `pyega3` - `/sw/generic/uv-tools/tool_bin/pyega3`
- `globus-cli` - `/sw/generic/pixi-tools/bin/globus`
- `google-cloud-sdk` - `/sw/generic/pixi-tools/bin/gcloud`,`gsutil`...
- `ena-webin-cli` - `/sw/generic/pixi-tools/bin/ena-webin-cli`
- `aspera-cli` - `/sw/generic/pixi-tools/bin/ascli`
- `awscli` - `/sw/generic/pixi-tools/bin/aws`
- `lftp` - `/sw/generic/pixi-tools/bin/lftp`
- `filesender` - `/sw/generic/uv-tools/tool_bin/filesender`
- `filesender.py` - `/sw/generic/uv-envs/EOSC-filesender/.venv/bin/filesender.py`
