# `nextflow` & `nf-core` on UPPMAX

[https://www.nextflow.io](https://www.nextflow.io)

- Official documentation: [https://www.nextflow.io/docs/latest/index.html](https://www.nextflow.io/docs/latest/index.html)


## Available versions from the [module](../cluster_guides/modules.md) system

Check which versions are available

```bash
# On Pelle/Maya
module avail nextflow
-------------------------------------------------------- /sw/arch/eb/modules/all ---------------------------------------------------------
   Nextflow/24.10.2    Nextflow/25.10.2 (D)
...

# On Rackham/Bianca
module load bioinfo-tools 
module avail nextflow
------------------------------------------------- /sw/mf/rackham/bioinfo-tools/pipelines --------------------------------------------------
   Nextflow/latest (D)    Nextflow/0.26.0     Nextflow/19.01.0         Nextflow/20.10.0         Nextflow/21.04.1    Nextflow/22.10.1
   Nextflow/0.17.3        Nextflow/0.31.1     Nextflow/20.02.0-edge    Nextflow/21.01.0-edge    Nextflow/21.10.6
   Nextflow/0.22.2        Nextflow/18.10.1    Nextflow/20.04.0-edge    Nextflow/21.02.0-edge    Nextflow/22.10.0
   ...
```

Nextflow provided by the module system on Pelle and Maya do not allow users to alter the version as regular Nextflow installations.

## `nextflow` from the [module](../cluster_guides/modules.md) system on Rackham/Bianca

- latest `nextflow` - Bianca/Rackham

```bash
module load bioinfo-tools
module load Nextflow/latest  # this also loads java as requirement

nextflow -v
nextflow version 25.04.7.5955
```

- other `nextflow` versions on Rackham/Bianca

```bash
export NXF_VER=23.10.1

nextflow -v
nextflow version 23.10.1.5891
```

```bash
# To check the available versions on Rackham/Bianca
ls /sw/bioinfo/Nextflow/latest/rackham/nxf_home/framework/
20.04.1  21.04.3  22.10.1  22.10.4  23.04.2  23.10.0  24.04.2  24.04.5  24.10.2  24.10.5  25.04.1  25.04.4  25.04.7
20.07.1  21.10.6  22.10.2  22.10.8  23.04.3  23.10.1  24.04.3  24.10.0  24.10.3  24.10.6  25.04.2  25.04.5
20.10.0  22.10.0  22.10.3  23.04.1  23.04.4  24.04.1  24.04.4  24.10.1  24.10.4  25.04.0  25.04.3  25.04.6
```

---

## `nf-core` from the module system

[https://nf-co.re](https://nf-co.re)
!!! warning

    On transit use module system is not available. Instead use the full path to the corresponding tools  
    - `nextflow` - `/sw/generic/pixi-tools/bin/nextflow`  
    - `nf-core` - `/sw/generic/pixi-tools/bin/nf-core`  
    - `dds-cli` - `/sw/generic/uv-tools/tool_bin/dds`  
    - `pyega3` - `/sw/generic/uv-tools/tool_bin/pyega3`  

```bash
# On Pelle/Maya
module load nf-core

# On Rackham/Bianca
module load bioinfo-tools
module load nf-core   # this also load the nextflow and java as requirements
```

---

## `nf-core` pipelines on Bianca

<!-- Due to the combination of indented code (that needs to be surrounded by -->
<!-- empty lines and a numbered list (that needs no empty lines), there -->
<!-- is no way to satisfy markdownlint -->
<!-- markdownlint-disable MD029 -->

1. Login to `transit.uppmax.uu.se` - [documentation](../cluster_guides/transfer_bianca.md#transit-server)
2. Mount the `wharf` of your project.

    ```bash
    user@transit:~$ mount_wharf sens2023531
    Mounting wharf (accessible for you only) to /home/<user>/sens2023531
    Password: 
    Second factor (TOTP UPPMAX): 
    done.
    ```

3. Navigate to your `wharf` folder
4. Disable Singularity cache

    ```bash
    export SINGULARITY_DISABLE_CACHE=true
    export APPTAINER_DISABLE_CACHE=true
    unset NXF_SINGULARITY_CACHEDIR
    ```

5. Run `/sw/generic/pixi-tools/bin/nf-core` to download the pipeline.

    ```bash
     /sw/generic/pixi-tools/bin/nf-core pipelines download -c yes ampliseq

                                          ,--./,-.
          ___     __   __   __   ___     /,-._.--~\ 
    |\ | |__  __ /  ` /  \ |__) |__         }  {
    | \| |       \__, \__/ |  \ |___     \`-._,-`-,
                                          `._,._,'

    nf-core/tools version 3.0.2 - https://nf-co.re

    WARNING  Could not find GitHub authentication token. Some API requests may fail.
    ? Select release / branch: 2.11.0  [release]

    In addition to the pipeline code, this tool can download software containers.
    ? Download software container images: singularity

    Nextflow and nf-core can use an environment variable called $NXF_SINGULARITY_CACHEDIR that is a path to a directory where remote 
    Singularity images are stored. This allows downloaded images to be cached in a central location.
    
    ? Define $NXF_SINGULARITY_CACHEDIR for a shared Singularity image download folder? [y/n]: n

    If transferring the downloaded files to another system, it can be convenient to have everything compressed in a single file.
    This is not recommended when downloading Singularity images, as it can take a long time and saves very little space.
    ? Choose compression type: none
    INFO     Saving 'nf-core/ampliseq'
            Pipeline revision: '2.11.0'
            Use containers: 'singularity'
            Container library: 'quay.io'
            Output directory: 'nf-core-ampliseq_2.11.0'
            Include default institutional configuration: 'True'
    INFO     Downloading centralised configs from GitHub
    INFO     Downloading workflow files from GitHub
    INFO     Processing workflow revision 2.11.0, found 30 container images in total.
    ...
    ```

7. Running on Bianca

    ```bash
    module load bioinfo-tools Nextflow
    nextflow run ... -profile uppmax --project sens-XXXX-XX ....
    ```

<!-- markdownlint-enable MD029 -->

Note: you might need `-c configs/conf/uppmax.config`,
make sure you have the file
(it is an option to download it during the pipeline download process).
[https://github.com/nf-core/configs/blob/master/conf/uppmax.config](https://github.com/nf-core/configs/blob/master/conf/uppmax.config)
[https://nf-co.re/configs/uppmax](https://nf-co.re/configs/uppmax)


## `nf-core` pipelines available offline on Bianca/Maya

UPPMAX does not maintain complete mirror anymore.
Only most requested pipelines are mirrored offline.
To check the available pipelines, run

```bash
tree -L 2 /sw/bioinfo/nf-core-pipelines/latest/rackham

...
├── rnaseq
│   ├── 1.0
│   ├── 1.1
│   ├── 1.2
│   ├── 1.3
...
```

To run a pipeline from the UPPMAX mirror, run

```bash
module load bioinfo-tools
module load nf-core-pipelines # this also loads Nextflow

nextflow run $NF_CORE_PIPELINES/pipeline_name/revision/workflow ...
```


## Common problems

- **Task is running out of resources (memory or time)**

Add lines to your configuration that overrides the settings for the problematic task, for example:

```python
process {
    withName: 'NFCORE_RNASEQ:RNASEQ:ALIGN_STAR:STAR_ALIGN' {
        cpus   = 12
        memory = '72.GB'
        time   = '24.h'
    }
}
```

More: [https://www.nextflow.io/docs/latest/config.html#process-selectors](https://www.nextflow.io/docs/latest/config.html#process-selectors)

## **[Troubleshooting nf-core](https://nf-co.re/docs/usage/troubleshooting/overview)**
