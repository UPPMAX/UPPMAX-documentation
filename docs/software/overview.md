# Software

At the UPPMAX clusters,
a lot of software is pre-installed
and accessible via the module system.

???- question "What are the UPPMAX clusters?"

    See [the UPPMAX documentation on its clusters](../cluster_guides/uppmax_cluster.md)

???- question "What is the module system?"

    See [the UPPMAX documentation on modules](../cluster_guides/modules.md)

## Software table

[Automatically updated software table](software-table.md)

## Conflicting modules

- [Conflicting modules](../cluster_guides/module_conflicts.md)

## Reach the Bioinformatics tools

- Before you can list available bioinformatics tools you need to issue the command:

```bash
module load bioinfo-tools
```

- When you list available modules with ``module avail`` after this, you will see that the bioinformatics tools are now also available in the listing.

- Note that the ``module spider`` command will show bioinformatics modules regardless of whether you have loaded the bioinfo-tools module.
- This command can also tell you whether a particular module requires the bioinfo-tools module, e.g. "module spider GEMINI/0.18.3".

## How can I request new software to be installed?

You can always install software in your home on any UPPMAX system. If there are many users who would like to request the same software, it can be installed by UPPMAX application or system experts.

Please send such requests to `support@uppmax.uu.se`.

### Installing yourself

Go to our [installation page](install.md)
