# Log in to Bianca


## Bianca's design

- Bianca was designed
    - to make accidental data leaks difficult
    - to make correct data management as easy as possible
    - to emulate the HPC cluster environment that SNIC users were familiar with
    - to provide a maximum amount of resources
    - and to satisfy regulations.

!!! info "Bianca has no internet"

    - Still you can log in, but it is done in two steps!
    - We recomend the ThinLink web portal, to enable graphics
    
## Log in to Bianca with ThinLinc

- Bianca offers graphical login
    - You need to be on SUNET or use VPN
    - On web:
        - [https://bianca.uppmax.uu.se](https://bianca.uppmax.uu.se)
        - requires [2-factor authentication](https://www.uppmax.uu.se/support/user-guides/setting-up-two-factor-authentication/)

### The log in steps
1. When you log in to [https://bianca.uppmax.uu.se](https://bianca.uppmax.uu.se), your SSH or ThinLinc client first meets the blue Bianca login node.
    - user name: `<username>-<projid>@bianca.uppmax.uu.se`
        - like: `myname-sens2016999@bianca.uppmax.uu.se`
    - password: your password, directly followed by the 6-digit 2-factor
        - like: verysecret678123
2. After checking your [2-factor authentication] this server looks for your virtual project cluster.
3. If it's present, then you are transferred to a login prompt on your cluster's login node. If not, then the virtual cluster is started.
    - you are prompted to give your username and password again, this time without projid and 2nd-factor:
         - username: <myname>
         - password: verysecret
4. Inside each virtual project cluster, by default there is just a one-core login node. When you need more memory or more CPU power, you submit a job (interactive or batch), and an idle node will be moved into your project cluster.


 
![Image](./img/Thinlinc2.jpg)


!!! info

    Check out or Bianca Portal for info about:
    - NAISS-SENS
    - Sensitive data
    - The Bianca solution
    - Tranfer of data
    
    

    
### Bianca has no Internet
... but we have “solutions”

![Image](./img/biancaorganisation-01.png)

- Bianca is only accessible from within Sunet (i.e. from university networks).
- Use VPN outside Sunet. [Link to VPN for UU](https://mp.uu.se/en/web/info/stod/it-telefoni/it-support/network-on-campus/vpn-service)
  - You can get VPN credentials from all Swedish universities.

<br>

- The whole Bianca cluster (blue) contains hundreds of virtual project clusters (green), each of which is isolated from each other and the Internet.
- Data can be transferred to or from a virtual project cluster through the Wharf, which is a special file area that is visible from the Internet.


