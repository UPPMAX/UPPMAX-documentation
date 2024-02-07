![Dardel server racks](./img/dardel_racks.png)

The Rackham cluster will be decommissioned at the end of 2024 
so all projects have to migrate their data and calculations to other resources. 
The plan from NAISS is that all Rackham users will move to 
the Dardel cluster at PDC.

To facilitate this move we have created Darsync, 
a tool that can inspect your files and make suggestions 
to make the transfer easier, 
as well as generating a script file you can submit to [SLURM](slurm.md) 
to perform the actual file transfer. 
[Read more about how to use Darsync here](../cluster_guides/darsync.md).

To transfer your files to Dardel:

1. Get access to a SUPR project with Dardel.
   This is described at [PDC's page on getting access to Dardel](https://www.pdc.kth.se/support/documents/getting_access/get_access.html).
   You will get an email when you are added to a project,
   this can take some hours.

???- question "How do I know I have access to a Dardel project?"

    Login to [https://supr.naiss.se/](https://supr.naiss.se/).
    If there is a PDC project,
    you may have access to a project with Dardel.

    ![](supr_naiss_dardel_project.png)

    > Example user that has access to a PDC project

    If you may a PDC project that does not use Dardel,
    click on the project to go the the project overview.

    ![](supr_naiss_dardel_project_overview.png)

    > Example PDC project overview

    From there, scroll down to 'Resources'.
    If you see 'Dardel' among the compute resources, 
    you have confirmed you have access to a Dardel project.

    ![](naiss_project_dardel_resources.png)

    > Resources from an example PDC project

1. Get a PDC account via SUPR.
   This is described at [the PDC page on getting access](https://www.pdc.kth.se/support/documents/getting_access/get_access.html#supr-account).
   You will get a PDC account overnight.

???- question "How do I know I have a PDC account?"

    Login to [https://supr.naiss.se/](https://supr.naiss.se/).
    and click on 'Accounts' in the main menu bar at the left.

    If you see 'Dardel' among the resources, and status 'Enabled'
    in the same row, you have a PDC account!

    ![](supr_naiss_dardel_account.png)

    > Example of a user having an account at PDC's Dardel HPC cluster

## Link

 * [PDC's page on getting access to Dardel](https://www.pdc.kth.se/support/documents/getting_access/get_access.html)

 * [PDC's page on login to Dardel](https://www.pdc.kth.se/support/documents/login/dardel.html)


