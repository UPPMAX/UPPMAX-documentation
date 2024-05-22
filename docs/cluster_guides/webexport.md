# Webexport guide


## Rackham

- You can enable webexport by creating a publicly readable folder called **webexport** in your project directory (``/proj/[project id]``).
- The contents of that folder will be accessible through `https://export.uppmax.uu.se/[project id]/`.

- A publicly readable folder has the execute permission set for "other" users.
- Run the command ``chmod o+x webexport`` to ensure that the webexport directory has the correct permissions.

- A subset of [.htaccess](httpd.apache.org/docs/current/howto/htaccess.html)/[.htpasswd](httpd.apache.org/docs/2.4/programs/htpasswd.html) functionality is available to control access.

- Example:
    - ``/crex/proj/naiss2024-1-123/webexport/Project_portal/.htaccess``
    - ``/crex/proj/naiss2024-1-123/Nisse/.htpasswd``

    - Note that you need the full physical ``/crex/proj...`` path. This full path is given from the `command, ``pwd -P``.
