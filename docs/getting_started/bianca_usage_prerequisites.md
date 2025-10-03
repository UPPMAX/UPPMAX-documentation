# Prerequisites for using Bianca

To be allowed to [log in to Bianca](../getting_started/login_bianca.md),
one needs all of these:

- [An active research project](#an-active-research-project)
- [An UPPMAX account](#an-uppmax-user-account)
- [An UPPMAX password](#an-uppmax-password)

These prerequisites are discussed in detail below.

## An active research project

One [prerequisite for using Bianca](#prerequisites-for-using-bianca)
is that you need to be a member of an active SNIC SENS
or SIMPLER research project (these are called `sens[number]` or `simp[number]`,
where `[number]` represent a number, for example `sens123456` or `simp123456`).

???- question "Forgot your Bianca projects?"

    One easy way to see your Bianca projects is to use the
    Bianca remote desktop login screen at <https://bianca.uppmax.uu.se/>.

    ![The Bianca remote desktop login screen](./img/bianca_remote_desktop_login_shows_sens_projects.png)

[SUPR](https://supr.naiss.se/) (the 'Swedish User and Project Repository')
is the website that allows one to request access to Bianca
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

To see if a project has access to Bianca, click on the
project and scroll to the 'Resources' section. In the 'Compute' subsection,
there is a table. Under 'Resource' it should state 'Bianca @ UPPMAX'.

???- question "How does the 'Resources' page of an example project look like?"

    ![The 'Resources' page of an example project.](./img/supr_project_sens2023598_resources.png)

    > The 'Resources' page of an example project.

Note that the 'Accounts' tab can be useful to verify your username.

???- question "How does the 'Accounts' tab help me find my username?"

    ![An example of a SUPR 'Accounts' tab](./img/supr_accounts.png)

    > An example of a SUPR 'Accounts' tab.
    > The example user has username `sven-sens2023598`,
    > which means his/her UPPMAX username is `sven`

You can become a member of an active SNIC SENS by:

- request membership to an existing project in SUPR
- [Apply for an UPPMAX project](project_apply.md)

## An UPPMAX user account

Another [prerequisite for using Bianca](#prerequisites-for-using-bianca)
is that you must have a personal [UPPMAX user account](../getting_started/user_account.md).

## An UPPMAX password

Another [prerequisite for using Bianca](#prerequisites-for-using-bianca)
is that you need to know your UPPMAX password.
If you change it, it may take up to an hour before changes are reflected in Bianca.

For advice on handling sensitive personal data correctly on Bianca, see our FAQ page.

## Second-factor identification or TOTP

[UPPMAX 2FA](get_uppmax_2fa.md)
