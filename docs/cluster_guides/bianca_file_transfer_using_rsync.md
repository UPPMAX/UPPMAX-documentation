# File transfer to/from Bianca using rsync

[rsync](../software/rsync.md) is a tool [to do file transfer to/from Bianca](transfer_bianca.md),
that works under Linux, Mac and Windows.

To transfer files to/from Bianca using [rsync](../software/rsync.md), do the following steps:

```mermaid
flowchart TD
  local_computer_ourside_sunet[Local computer outside of SUNET]
  local_computer[Local computer]
  transit[Transit]
  bianca[Bianca]
  local_computer_ourside_sunet --> |1. Get inside SUNET|local_computer
  local_computer --> |2. login| transit
  local_computer --> |4. rsync| bianca
  bianca --> |5. rsync| local_computer
  transit --> |3. mount| bianca
```

## 1. Get inside SUNET

Get inside SUNET.

???- question "Forgot how to get within SUNET?"

    See the 'get inside the university networks' page [here](../getting_started/get_inside_sunet.md)

## 2. Log in to Transit

On your local computer, start a terminal and use [`ssh`](../software/ssh.md) to login to Transit:

```bash
ssh [username]@transit.uppmax.uu.se
```

where

- `[username]` is your UPPMAX username

For example:

```bash
ssh richel@transit.uppmax.uu.se
```

See [Log in to transit](login_transit.md) for more details
on how to log in to [Transit](transit.md).

## 3. Mount Bianca

On transit, mount the wharf of your Bianca project:

```bash
mount_wharf [project_id]
```

where

- `[project_id]` is the ID of your [NAISS project](../getting_started/project.md)


???- question "What about the `[path]` argument?"

    Well spotted!

    Indeed, the Transit server gives these arguments:

    ```bash
    mount_wharf [project_id] [path]
    ```

    However, the `[path]` argument is optional: if not
    given, a default will be used. 
    
    To simplify matters, here we use the default.

for example:

```bash
mount_wharf sens2016001
```

The password here is your UPPMAX password and your UPPMAX 2FA.

Now a folder called `sens2016001` is created.

## 4. Tranfer files to Bianca

On local computer:

```bash
rsync --recursive my_folder [username]@transit.uppmax.uu.se:[project_id]
```

where

- `[project_id]` is the ID of your [NAISS project](../getting_started/project.md)
- `[username]` is your UPPMAX username

for example:

```bash
rsync --recursive my_folder richel@transit.uppmax.uu.se:sens2016001
```

No need to specify the path to the mounted folder, if defaults are used.

The files can now be found in [your wharf folder](wharf.md).

## 5. Tranfer files from Bianca to you local computer

On your local computer, do:

```bash
rsync --recursive [username]@transit.uppmax.uu.se:[project_id] .
```

where

- `[project_id]` is the ID of your [NAISS project](../getting_started/project.md)
- `[username]` is your UPPMAX username
- `.` means 'in the current folder of my local computer' or 'here'

for example:

```bash
rsync --recursive richel@transit.uppmax.uu.se:sens2016001 .
```

To copy all folders in wharf to your local computer.
