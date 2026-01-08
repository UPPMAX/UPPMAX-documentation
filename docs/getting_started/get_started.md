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
        subgraph get_uppmax_account[Get an UPPMAX account]
          get_supr_account[Get a SUPR account]
          accept_supr_user_agreement[Accept the SUPR user agreement]
        end
        get_2fa[Get your UPPMAX 2FA]
        get_project[Apply for an UPPMAX project]
        
        get_supr_account --> accept_supr_user_agreement
        get_uppmax_account -.-> get_2fa
        get_2fa -.-> get_project
        get_uppmax_account --> get_project
    ```

    - The solid lines denote a dependency, e.g. you need an UPPMAX account
      to get an UPPMAX project.
    - The dashed lines denote a 'maybe' or 'optional', e.g. some UPPMAX
      projects require two factor authorization.

## Step 1: get an UPPMAX user account

First, one needs an an UPPMAX user account.
See how to get one at [the UPPMAX guide 'Apply to a user account'](user_account.md#apply-to-an-uppmax-user-account).

## (optional) Step 2: get a 2FA for your UPPMAX user account

Some parts of UPPMAX require two factor authentication.
See how to set this up at
[the guide 'Setting up two factor authentication for UPPMAX'](get_uppmax_2fa.md).

## Step 3: get an UPPMAX project

Second, one needs to have an active research project.
See how to get one at [the UPPMAX guide 'Apply for a project'](project_apply.md).

## Step 4: use UPPMAX

Now you can use the UPPMAX resources!

- [Login to our clusters](login.md)
- [Transfer files from/to your UPPMAX account](../cluster_guides/file_transfer.md)
- [Schedule jobs](../cluster_guides/slurm.md).

To make this step easier,
UPPMAX provides for [courses and workshops](../courses_workshops/courses_workshops.md).

If you are stuck, never hesitate to [contact support](../support.md).
