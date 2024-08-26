---
tags:
  - UPPMAX
  - password
  - reset
  - set
  - passwd
---

# Reset your UPPMAX password

???- question "Prefer a video?"

    See [the YouTube video 'How to reset your UPPMAX password'](https://youtu.be/3PaKjuWKQZw)

## Procedure

### 1. Go to <https://suprintegration.uppmax.uu.se/getpasswd>

Go to <https://suprintegration.uppmax.uu.se/getpasswd>.

You will be sent an email in around 5 minutes.

### 2. Open email

Open the email and click on the link that it suggests you to click.

???- question "How does that email look like?"

    Your email will look similar to this:

    ```text
    Greetings,

    a new password has been generated for your account at UPPMAX.

    You can fetch it by visiting the link below.
    Note though that the link is only valid for 7 days and one (1) visit.

    You can retrieve the password at the following link:

    https://content.uppmax.uu.se/get-password2.php?sum=hvs.CAESIGOczS0[more_letters]

    If the password has expired, you can request a new password from our homepage
    https://www.uppmax.uu.se and the link "Lost your password?".

    Note that if you requested a new password because your account was locked,
    it may take some additional time (up to an hour) before that change is
    reflected everywhere.

    If you are unsure about what your user name is, this information is available
    in SUPR (https://supr.snic.se/) under Accounts.

    For general information about how to login, change your password and
    so on, please see our getting started guide at

    http://www.uppmax.uu.se/support/user-guides/guide--first-login-to-uppmax/

    regards, UPPMAX Support


    VARNING: Klicka inte på länkar och öppna inte bilagor om du inte känner igen avsändaren och vet att innehållet är säkert.
    CAUTION: Do not click on links or open attachments unless you recognise the sender and know the content is safe.
    ```

    In this example,
    `https://content.uppmax.uu.se/get-password2.php?sum=hvs.CAESIGOczS0[more_letters]`
    is the link you should click

This will take you to a page with your new password.

### 3. Log in with your new password

At the page with your new password, you use that password to log in.

### 4. (optional) Set your own password

When being logged in to Rackham or Bianca, type:

```bash
passwd
```

Now you will be asked to repeat the old password and set a new one!

