![Dardel server racks](./img/dardel_racks.png)

The Rackham cluster will be decommissioned at the end of 2024 so all projects have to migrate their data and calculations to other resources. The plan from NAISS is that all Rackham users will move to the Dardel cluster at PDC.

To facilitate this move we have created Darsync, a tool that can inspect your files and make suggestions to make the transfer easier, as well as generating a script file you can submit to [SLURM](slurm.md) to perform the actual file transfer. [Read more about how to use Darsync here](../darsync).
