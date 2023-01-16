# Bianca

- Bianca is a great platform for computationally intensive research on sensitive personal data. It can also be useful for:
  - national and international collaboration on sensitive personal data (without a high compute need)
  - other types of sensitive data
- Bianca is not good for:
  - storing data
  - publishing data
     - unless the dataset is very popular among Bianca users, e.g. [Swegen](https://snd.gu.se/en/catalogue/study/ext0285), [SIMPLER](https://www.simpler4health.se/)

 
## Bianca's design

- Bianca was designed
  - to make accidental data leaks difficult
  - to make correct data management as easy as possible
  - to emulate the HPC cluster environment that SNIC users were familiar with
  - to provide a maximum amount of resources
  - and to satisfy regulations.

### Bianca has no Internet
... but we have “solutions”

![Image](./img/biancaorganisation-01.png)

- Bianca is only accessible from within Sunet (i.e. from university networks).
- Use VPN outside Sunet. [Link to VPN for UU](https://mp.uu.se/en/web/info/stod/it-telefoni/it-support/network-on-campus/vpn-service)
  - You can get VPN credentials from all Swedish universities.

<br>

- The whole Bianca cluster (blue) contains hundreds of virtual project clusters (green), each of which is isolated from each other and the Internet.
- Data can be transferred to or from a virtual project cluster through the Wharf, which is a special file area that is visible from the Internet.

### The log in steps
1. When you log in to [https://bianca.uppmax.uu.se](https://bianca.uppmax.uu.se), your SSH or ThinLinc client first meets the blue Bianca login node.
    - `<username>-<projid>@bianca.uppmax.uu.se`
    - like: `myname-sens2016999@bianca.uppmax.uu.se`
2. After checking your [2-factor authentication](https://www.uppmax.uu.se/support/user-guides/setting-up-two-factor-authentication/), this server looks for your virtual project cluster.
3. If it's present, then you are transferred to a login prompt on your cluster's login node. If not, then the virtual cluster is started.
4. Inside each virtual project cluster, by default there is just a one-core login node. When you need more memory or more CPU power, you submit a job (interactive or batch), and an idle node will be moved into your project cluster.


### Data transfers:
- <https://www.uppmax.uu.se/support/user-guides/bianca-user-guide/> 
  - section 3: Transfer files to and from Bianca
- wharf
- NGI Deliver through SUPR
- Transit server (SSH to transit.uppmax.uu.se)

### Software

- Modules library (almost same as Rackham)
- Local Conda repository
- Local Perl modules
- Local R packages

- More info at [Bianca user guide](https://www.uppmax.uu.se/support/user-guides/bianca-user-guide/)


## ThinLinc

- Bianca offers graphical login
  - You need to be on SUNET or use VPN. 
  - On web:
    - [https://bianca.uppmax.uu.se](https://bianca.uppmax.uu.se)
    - requires [2-factor authentication](https://www.uppmax.uu.se/support/user-guides/setting-up-two-factor-authentication/)

 
![Image](./img/Thinlinc2.jpg)


!!! abstract "keypoints"
    - If you handle sensitive data, apply for a SNIC-SENS project
    - SENS projects will get accounts on Bianca
    - Bianca has no internet itself but there are solutions like:
        - wharf
        - transit server
        - many installed software
    - Ask support if you need additional software tools

