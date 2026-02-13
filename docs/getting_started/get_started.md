---
tags:
  - get started
---

# Get started

This page describes how to get started with UPPMAX.

???- question "Prefer a graphical overview?"

    The processes to get started:

    ```mermaid
    flowchart TB
        subgraph get_SUPR_account[Get a SUPR account]
          get_supr_account[Apply for SUPR account]
          accept_supr_user_agreement[Accept the SUPR user agreement]
        end
        get_2fa[Get your UPPMAX 2FA]
        get_project[Apply for an UPPMAX project]
        get_uppmax_account[Apply for a user name for UPPMAX facilities]
        
        get_supr_account --> accept_supr_user_agreement
        get_SUPR_account -.-> get_2fa
        get_2fa -.-> get_project
        get_SUPR_account --> get_project
        get_project --> get_uppmax_account
    ```

    - The solid lines denote a dependency, e.g. you need an UPPMAX account
      to get an UPPMAX project.
    - The dashed lines denote a 'maybe' or 'optional', e.g. some UPPMAX
      projects require two factor authorisation.

## Step 1: Get a SUPR account

First, one needs an an SUPR account.
See how to get one at [the UPPMAX guide 'Apply to a SUPR account'](supr_account.md).

This is needed to administer your projects and accounts on one or several academic clusters over Sweden.

## Step 2: Get a 2FA for your UPPMAX user account

All parts of UPPMAX require two factor authentication.
See how to set this up at
[the guide 'Setting up two factor authentication for UPPMAX'](get_uppmax_2fa.md).

!!! warning

    - Please be aware of that this is different from the SUPR 2FA that you may have set up earlier.
    - Also, each centre has their own 2FA, so one from NSC/Tetralith won't work for UPPMAX.

## Step 3: get an UPPMAX project

Second, one needs to have an active research project.
See how to get one at [the UPPMAX guide 'Apply for a project'](project_apply.md).

## Step 4: Get a user account for Pelle or Bianca, depending on type of project

After having been granted membership in the project [on SUPR, activate your user accounts](https://supr.naiss.se/account/)

## Step 5: Wait for an email with further instructions

- The email may land in you trash bin so do look there as well.
- Follow the instructions! You'll need the UPPMAX 2FA set up, see Step 2 to be able to log in.
- The password you got will only work once and for a limited time period.

## Step 6: First time log in

- [Login to our clusters](login.md)

## Step 7: Change your password to something you'll remember

When logged in on a UPPMAX system via a terminal, type ``passwd`` and follow the instructions on the screen.

!!! info

    The password is not seen in the terminal, neither as characters nor ``*`` or similar.

## Step 8: use UPPMAX

Now you can use the UPPMAX resources!

- [Login to our clusters](login.md)
- [Transfer files from/to your UPPMAX account](../cluster_guides/file_transfer.md)
- [Schedule jobs](../cluster_guides/slurm.md).

To make this step easier,
UPPMAX provides for [courses and workshops](../courses_workshops/courses_workshops.md).

If you are stuck, never hesitate to [contact support](../support.md).
