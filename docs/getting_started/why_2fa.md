---
tags:
  - 2FA
  - MFA
  - UPPMAX
  - Why
---

# Why is 2FA important?

By requiring a second factor, typically a cell phone or other physical device,
it becomes much harder for an attacker to gain access to your account
if they somehow have gotten hold of your password
(which in this case is the 1:st factor).

For security reasons you will have to use a two factor authentication system
if you are a) connecting to UPPMAX from outside of Sweden, or b) connecting
from a network within Sweden that does not support forward and reverse DNS
lookups (due to a misconfiguration in your network, you can ask your
internet service provider about this). More information about why can be
found below.

## From outside Sweden

If you try to connect directly to our resources from computers outside Sweden
you will most likely be required to set up and use two factor
authentication (you will be asked for a code from your second factor
automatically if required).

Another alternative, if you need to access UPPMAX from outside Sweden,
may be to use a Swedish VPN service.
For example, if you're employed at Uppsala University,
then you can connect using the university's VPN service.

## From within Sweden

If you are required to use two factor authentication,
and are connecting from a computer in Sweden, this is typically caused by
your computer not having a proper DNS name, or the forward and reverse name
resolution do not match.

If this is the case, please contact your ISP and ask them to correct this.

## Note

You can check forward and reverse name resolution on this webpage:

- [http://www.whatismyip.com/reverse-dns-lookup](http://www.whatismyip.com/reverse-dns-lookup)

To see what address the other side thinks you come from (which will likely be what our systems see), services like

- [https://ifconfig.co/](https://ifconfig.co/)

can be helpful.

On Linux, you can also use these commands:

- Forward resolution: `host mycomputername.domain.tld`.
  You have to replace `mycomputername.domain.tld`
  with your computers actual name, for example:

```bash
host rackham2.uppmax.uu.se
```

will give:

```bash
rackham2.uppmax.uu.se has address 89.44.250.83
```

- Reverse resolution: `host my_ipnumber`.
  You have to replace `my_ipnumber` with your computers actual IP number,
  for example:

```bash
host 89.44.250.83
```

which should give something similar to:

```bash
89.44.250.83.in-addr.arpa domain name pointer rackham2.uppmax.uu.se
```
