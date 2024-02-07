# Dardel Migration

![Dardel server racks](./img/dardel_racks.png)

The Rackham cluster will be decommissioned at the end of 2024 so all projects have to migrate their data and calculations to other resources. The plan from NAISS is that all Rackham users will move to the Dardel cluster at PDC. 

To facilitate this move we have created Darsync, a tool that can inspect your files and make suggestions to make the transfer easier, as well as generating a script file you can submit to [SLURM](slurm.md) to perform the actual file transfer. [Read more about how to use Darsync here]

This migration consists of a couple of steps summarized below. Press the links to get more detailed explaination of each step.

1. Create SSH key and add it to the PDC Login Portal.
    - Create the password less SSH key in a terminal logged into Rackham:
```bash
# generate the key
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519-pdc

# view the public part of they key
# which should be entered into the PCD Login Portal
cat ~/.ssh/id_ed25519-pdc.pub
```
    - Open the [PDC Login Portal](https://loginportal.pdc.kth.se/) and follow [PDC:s instructions on how to add SSH keys.](https://www.pdc.kth.se/support/documents/login/ssh_login.html#in-the-login-portal)
    - Once you have added you key you have to [add UPPMAX as allowed to use the key.](../dardel_ssh-keys/#optional-adding-uppmax-to-addresses) Click on `Add address` for it and add `*.uppmax.uu.se`
1. Run the migration tool [Darsync](../darsync.md).
```bash
module load darsync

darsync check --local-dir /path/to/dir
# fix any errors the check step found
darsync gen --local-dir /path/to/dir --outfile ~/dardel_transfer_script.sh
```
1. Submit the transfer script created by Darsync to SLURM.
```bash
sbatch --output=~/dardel_transfer.out --error=~/dardel_transfer.err ~/dardel_transfer_script.sh
```
1. Once the submitted job has finished, have a look at the log file produced by the job and make sure it did not end in a error message.
```bash
tail ~/dardel_transfer.out
tail ~/dardel_transfer.err
```
1. Delete the SSH key you created after the migration has completed.
```bash
rm ~/.ssh/id_ed25519-pdc*
```


