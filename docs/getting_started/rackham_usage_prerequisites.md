# Prerequisites for using Rackham

To be allowed to [log in to Rackham](../getting_started/login_rackham.md),
one needs all of these:

- [An active research project](#an-active-research-project)
- [An UPPMAX account](#an-uppmax-user-account)
- [An UPPMAX password](#an-uppmax-password)
- (for the [Rackham remote desktop website](login_rackham_remote_desktop_website.md)) [An UPPMAX 2FA](#an-uppmax-2fa)

These prerequisites are discussed in detail below.

## An active research project

One [prerequisite for using Rackham](#prerequisites-for-using-rackham)
is that you need to be a member of an active SNIC
or SIMPLER research project (these can have many names such as `uppmax[number]`,
`snic[number]` or`naiss[number]`),
where `[number]` represent a number, for example `uppmax2021-2-1`, `snic2022-6-230` or `naiss2023-6-382`).

???- question "Forgot your Rackham projects?"

    How to see you [research projects](project.md) is described at [research projects](project.md).

    Spoiler: go to [https://supr.naiss.se](https://supr.naiss.se)

[SUPR](https://supr.naiss.se/) (the 'Swedish User and Project Repository')
is the website that allows one to request access to Rackham
and to get an overview of the requested resources.

???- question "How does the SUPR website look like?"

    ![First SUPR page](./img/supr_first_page.png)

    > First SUPR page

    ![SUPR 2FA login](./img/supr_2fa.png)

    > SUPR 2FA login. Use the SUPR 2FA (i.e. **not** UPPMAX)

After logging in, the [SUPR](https://supr.naiss.se/)
website will show all projects you are a member of,
under the 'Projects' tab.

???- question "How does the 'Projects' tab of the SUPR website look like?"

    ![Example overview of SUPR projects](./img/supr_projects.png)

    > Example overview of SUPR projects

To see if a project has access to Rackham, click on the
project and scroll to the 'Resources' section. In the 'Compute' subsection,
there is a table. Under 'Resource' it should state 'Rackham @ UPPMAX'.

???- question "How does the 'Resources' page of an example project look like?"

    ![The 'Resources' page of an example project](./img/supr_project_naiss2024-22-49_resources.png)

    > The 'Resources' page of an example project. This project has two compute
    > resources and two storage resources.

Note that the 'Accounts' tab can be useful to verify your username.

???- question "How does the 'Accounts' tab help me find my username?"

    ![An example of a SUPR 'Accounts' tab](./img/supr_accounts.png)

    > An example of a SUPR 'Accounts' tab.
    > The example user has username `sven-sens2023598`,
    > which means his/her UPPMAX username is `sven`

You can become a member of an active SNIC SENS by:

- request membership to an existing project in SUPR
- create a project. See the UPPMAX page on
  how to submit a project application [here](project_apply.md)

## An UPPMAX user account

Another [prerequisite for using Rackham](#prerequisites-for-using-rackham)
is that you must have a personal [UPPMAX user account](../getting_started/user_account.md).

## An UPPMAX password

Another [prerequisite for using Rackham](#prerequisites-for-using-rackham)
is that you need to know your UPPMAX password.
See [how to reset and set your UPPMAX password](reset_uppmax_password.md)
to do so.

## An UPPMAX 2FA

Another [prerequisite for using Rackham](#prerequisites-for-using-rackham),
but only for the [Rackham remote desktop website](login_rackham_remote_desktop_website.md))
is to have an UPPMAX 2FA.
See [how to get an UPPMAX 2FA](get_uppmax_2fa.md)
