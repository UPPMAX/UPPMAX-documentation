---
tags:
  - project
  - UPPMAX
---

# UPPMAX project

To use [UPPMAX](../cluster_guides/uppmax.md) resources, one needs:

- [an UPPMAX user account](user_account.md):
  you need one for an UPPMAX project
- [an active research project](project.md):
  this page :-)

This page is about UPPMAX projects:

- [Apply to an UPPMAX project](project_apply.md)
- [View your existing UPPMAX projects](#view-your-uppmax-projects)
- [Read about the types of UPPMAX projects](#type-of-uppmax-projects)

## View your UPPMAX projects

[SUPR](https://supr.naiss.se/) (the 'Swedish User and Project Repository')
is the website that allows one to request access to Swedish computational
resources and to get an overview of the requested resources.

???- question "How does the SUPR website look like?"

    ![First SUPR page](./img/supr_first_page.png)

    > First SUPR page

    ![SUPR 2FA login](./img/supr_2fa.png)

    > SUPR 2FA login. Use the SUPR 2FA (i.e. **not** UPPMAX)

After logging in, the [SUPR](https://supr.naiss.se/)
website will show all projects you are a member of,
under the 'Projects' tab.

???- question "How does the 'Projects' tab of the SUPR website look like?"

    ![An example overview of SUPR projects](./img/supr_projects.png)

    > An example overview of SUPR projects

## How to convert my project name to an account name for [the job scheduler](../cluster_guides/slurm.md)?

Here is a simple conversion table:

Project name    |Account name for [the job scheduler](../cluster_guides/slurm.md)?
----------------|-----------------------------------------------------------------
NAISS 2024/22-49|`naiss2024-22-49`
sens2017625     |`sens2017625`

Else, on an UPPMAX cluster do:

```bash
cd /proj
ls
```

and look for a project folder that resembles the name of your project.
The name of that folder is the name of your account.

???- question "How does that look like?"

    Here is part of the output:

    ```bash
    naiss2023-22-57           naiss2024-22-227  snic2015-10-19           snic2018-8-136  snic2020-15-16   snic2021-22-513   snic2022-22-1164  snic2022-5-333    uppstore2019112
    naiss2023-22-570          naiss2024-22-24   snic2015-10-25           snic2018-8-139  snic2020-15-161  snic2021-22-517   snic2022-22-117   snic2022-5-334    uppstore2019113
    naiss2023-22-574          naiss2024-22-244  snic2015-10-8            snic2018-8-14   snic2020-15-162  snic2021-22-521   snic2022-22-1172  snic2022-5-339    uppstore2019114
    naiss2023-22-577          naiss2024-22-247  snic2015-1-142           snic2018-8-141  snic2020-15-163  snic2021-22-522   snic2022-22-1173  snic2022-5-34     uppstore2019115
    naiss2023-22-578          naiss2024-22-253  snic2015-1-164           snic2018-8-143  snic2020-15-164  snic2021-22-525   snic2022-22-1178  snic2022-5-343    uppstore2019117
    naiss2023-22-58           naiss2024-22-257  snic2015-1-176           snic2018-8-144  snic2020-15-165  snic2021-22-526   snic2022-22-1179  snic2022-5-364    uppstore2019118
    naiss2023-22-580          naiss2024-22-26   snic2015-1-177           snic2018-8-145  snic2020-15-17   snic2021-22-529   snic2022-22-1180  snic2022-5-373    uppstore2019119
    naiss2023-22-582          naiss2024-22-270  snic2015-1-201           snic2018-8-146  snic2020-15-172  snic2021-22-530   snic2022-22-1181  snic2022-5-376    uppstore2019120
    naiss2023-22-583          naiss2024-22-275  snic2015-1-204           snic2018-8-147  snic2020-15-173  snic2021-22-535   snic2022-22-1184  snic2022-5-392    uppstore2019121
    naiss2023-22-586          naiss2024-22-281  snic2015-1-228           snic2018-8-148  snic2020-15-175  snic2021-22-537   snic2022-22-1186  snic2022-5-403    uppstore2019123
    naiss2023-22-590          naiss2024-22-282  snic2015-1-242           snic2018-8-149  snic2020-15-177  snic2021-22-538   snic2022-22-1194  snic2022-5-407    uppstore2021-23-134
    naiss2023-22-598          naiss2024-22-295  snic2015-1-259           snic2018-8-15   snic2020-15-178  snic2021-22-541   snic2022-22-1195  snic2022-5-408    uu_1dl550_2021
    naiss2023-22-600          naiss2024-22-299  snic2015-1-268           snic2018-8-150  snic2020-15-179  snic2021-22-544   snic2022-22-1197  snic2022-5-415    uucompbiochem
    naiss2023-22-608          naiss2024-22-3    snic2015-1-281           snic2018-8-151  snic2020-15-18   snic2021-22-546   snic2022-22-1198  snic2022-5-42     var_inf_sim_alex
    naiss2023-22-62           naiss2024-22-301  snic2015-1-315           snic2018-8-152  snic2020-15-182  snic2021-22-547   snic2022-22-12    snic2022-5-423    viher_snic2022
    naiss2023-22-620          naiss2024-22-303  snic2015-1-33            snic2018-8-153  snic2020-15-183  snic2021-22-550   snic2022-22-1200  snic2022-5-428    viscaria_pilot
    naiss2023-22-621          naiss2024-22-305  snic2015-1-345           snic2018-8-154  snic2020-15-185  snic2021-22-554   snic2022-22-1207  snic2022-5-432    vrognas
    naiss2023-22-623          naiss2024-22-307  snic2015-1-364           snic2018-8-155  snic2020-15-186  snic2021-22-555   snic2022-22-1208  snic2022-5-443    wamr
    naiss2023-22-624          naiss2024-22-308  snic2015-1-37            snic2018-8-156  snic2020-15-188  snic2021-22-557   snic2022-22-121   snic2022-5-451    wave_energy_parks
    naiss2023-22-627          naiss2024-22-310  snic2015-1-398           snic2018-8-157  snic2020-15-189  snic2021-22-559   snic2022-22-1214  snic2022-5-454    wheatrnaseq
    naiss2023-22-632          naiss2024-22-319  snic2015-1-399           snic2018-8-158  snic2020-15-19   snic2021-22-56    snic2022-22-1216  snic2022-5-461    wheatrnaseq2
    naiss2023-22-633          naiss2024-22-322  snic2015-1-410           snic2018-8-159  snic2020-15-190  snic2021-22-562   snic2022-22-1224  snic2022-5-466    wiosym
    naiss2023-22-634          naiss2024-22-324  snic2015-1-451           snic2018-8-16   snic2020-15-191  snic2021-22-563   snic2022-22-1227  snic2022-5-484    xfooli
    naiss2023-22-64           naiss2024-22-326  snic2015-1-466           snic2018-8-161  snic2020-15-192  snic2021-22-564   snic2022-22-1228  snic2022-5-503    yeast1000storage
    naiss2023-22-640          naiss2024-22-330  snic2015-1-475           snic2018-8-162  snic2020-15-193  snic2021-22-565   snic2022-22-123   snic2022-5-506    yeast-genomics
    naiss2023-22-648          naiss2024-22-332  snic2015-1-52            snic2018-8-163  snic2020-15-195  snic2021-22-569   snic2022-22-1231  snic2022-5-51     yeast_hybrid_barcode
    naiss2023-22-652          naiss2024-22-339  snic2015-16-12           snic2018-8-164  snic2020-15-196  snic2021-22-570   snic2022-22-1233  snic2022-5-52     zengkun
    naiss2023-22-654          naiss2024-22-341  snic2015-16-27           snic2018-8-165  snic2020-15-197  snic2021-22-571   snic2022-22-1234  snic2022-5-528    zinc22
    naiss2023-22-655          naiss2024-22-345  snic2015-16-34           snic2018-8-166  snic2020-15-198  snic2021-22-572   snic2022-22-1236  snic2022-5-530
    naiss2023-22-658          naiss2024-22-347  snic2015-1-72            snic2018-8-167  snic2020-15-199  snic2021-22-573   snic2022-22-1237  snic2022-5-544
    naiss2023-22-659          naiss2024-22-351  snic2015-1-92            snic2018-8-168  snic2020-15-2    snic2021-22-574   snic2022-22-1238  snic2022-5-548
    naiss2023-22-660          naiss2024-22-354  snic2015-6-101           snic2018-8-169  snic2020-15-20   snic2021-22-579   snic2022-22-1247  snic2022-5-552
    naiss2023-22-662          naiss2024-22-358  snic2015-6-102           snic2018-8-170  snic2020-15-201  snic2021-22-580   snic2022-22-125   snic2022-5-555
    naiss2023-22-665          naiss2024-22-362  snic2015-6-104           snic2018-8-171  snic2020-15-202  snic2021-22-582   snic2022-22-1250  snic2022-5-560
    naiss2023-22-667          naiss2024-22-363  snic2015-6-107           snic2018-8-173  snic2020-15-203  snic2021-22-583   snic2022-22-1253  snic2022-5-568
    naiss2023-22-67           naiss2024-22-375  snic2015-6-109           snic2018-8-175  snic2020-15-204  snic2021-22-584   snic2022-22-1254  snic2022-5-582
    ```

## Type of UPPMAX projects

These are the type of UPPMAX projects that exist:

- NAISS projects
- UPPMAX projects
- NGI Delivery projects
- Course projects
