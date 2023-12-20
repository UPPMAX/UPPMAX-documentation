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
- Use VPN outside Sunet. [Link to VPN for UU](https://mp.uu.se/web/info/stod/it-telefoni/anvandarguider/network/vpn-service)
  - You can get VPN credentials from all Swedish universities.

<br>

- The whole Bianca cluster (blue) contains hundreds of virtual project clusters (green), each of which is isolated from each other and the Internet.
- Data can be transferred to or from a virtual project cluster through the Wharf, which is a special file area that is visible from the Internet.


## Text from https://www.uppmax.uu.se/support/user-guides/bianca-user-guide/

```
0. PREREQUISITES

In order to access Bianca you need to be a member of an active SNIC SENS or SIMPLER research project (these are called sensNNNNN or simpNNNNN, where N represent a digit). SUPR will tell you if you are a member and the account page should list the account on the resource bianca (this can also be useful to verify your username). If you do not have a project membership, you can request membership to an existing project in SUPR or read the SENS project application page to learn how to create a project.

Additionally, you must have a personal UPPMAX user account. This is separate from your SUPR account. See the user account application page if you do not have one. 

Once you are set up for login, this should also be reflected in SUPR through one or several additional account(s) at UPPMAX for the specific project(s) you are a member of.

Also note that you need to know your UPPMAX password. If you change it, it may take up to an hour before changes are reflected in bianca.

For advice on handling sensitive personal data correctly on Bianca, see our FAQ page.
1. Set up TWO factor authentication

Follow the instructions in Setting up two factor authentication.

Please note that you need to set up two factor authentication for UPPMAX and not for SUPR! If you have multiple two factor codes registered the correct is labeled UPPMAX (as seen below highlighted in green).

2. Login

Bianca is accessible from all SUNET IP addresses, i.e. all Swedish university networks. It is generally NOT accessible from other networks. Use your university's VPN if needed.

The login procedure requires you to pass two separate authentication mechanisms (automatically connected together). The first one logs you into the general Bianca login node (which we call the jumphost). This is the step that requires two factor authentication. You will then be automatically redirected to your project's private login node, where you will get a new password prompt (unless you set up ssh-keys).

The user name you will use in the first step is your ordinary UPPMAX user name, followed by the project ID of the project you want to work on. One of the security measures on Bianca is that all projects are kept separate on their own virtual clusters, so you must tell Bianca which project's cluster you want to connect to.
Primary login (text login)

You can use any ssh-program in all normal platforms (Windows, Mac, Linux). You can have multiple log-ins active at once.

$ ssh -A <username>-<projid>@bianca.uppmax.uu.se
Ex.
$ ssh -A myname-sens2016999@bianca.uppmax.uu.se

As password you use your normal UPPMAX password directly followed by the six digits from the second factor application from step 1.

E.g. if your password is "VerySecret" and the second factor code is 123 456 you would type VerySecret123456 as the password in this step.

If the password is correct you will get a message of your projects login node status. It can be "up and running" or "down". If it is down it will automatically spin up, but this takes a few minutes. Then you will be automatically redirected to login at your project's private login node. To be able to login there you will have to give your UPPMAX password once again, but without the two factor authentication code this time. If your password is "VerySecret" you would type in VerySecret as password in this step. To skip this password in the future, you can use ssh-keys.

If the passwords have been entered correctly, you should now be connected and you will see the computer name at the start of the command line which looks something like this:

[myuser@sens2016999-bianca ~]$

This text login is limited to 50kBit/s, so if you create a lot of text output you will have to wait some time before you get your prompt back. The system supports all cut and paste mechanisms your client computer support, but of course you are not supposed to transfer any real data in or out through this mechanism — only commands and stuff like that.

Graphical login

Bianca does not support any X-forwarding, so to use graphical applications you need to have a full graphical desktop login. Bianca uses "Thinlinc" (in webaccess mode only) with XFCE as desktop environment for this. All you should need is a rather modern browser on any platform; we have tested on Chrome and Firefox.

Just browse to: https://bianca.uppmax.uu.se

The same principle with login name and password as with text logins: first step with user-project as username and password with password followed by second factor 6 digit number, and then second step to the login node for your specific project with normal username (and here you really have to type that – in text mode that is done automatically) and normal UPPMAX password (without second factor). The redirection to the correct project login node works automatically. If the login node is sleeping you will be informed what to do.

When you are logged into your graphical environment, the resizing and even fullscreen mode (in your browser) should work as expected.

Under the hidden tab in the left edge of the screen you can find a clipboard, some keys (where the keyboard versions often interfere with your local system) and the "disconnect" button. It is important to understand the difference of "disconnect session" and "end session". When you disconnect a session you will get back exactly in the same place you left the system; if you for example edit a file, your prompt will be in the same place you left it at the next login. If you use "logout" (end session) in the XFCE menus, the system will try to close all your windows and files and end the processes related to the login.

Bianca has a autodisconnect after 30 minutes of inactivity, and in the future it is possible that we implement some kind of "automatic log out from active graphical session". 
```
