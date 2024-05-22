# Webexport guide


## Rackham

- You can enable webexport by creating a publicly readable folder called **webexport** in your project directory (``/proj/[project id]``). The contents of that folder will be accessible through `https://export.uppmax.uu.se/[project id]/`.

- A publicly readable folder has the execute permission set for "other" users. Run the command chmod o+x webexport to ensure that the webexport directory has the correct permissions.

- A subset of .htaccess/.htpasswd functionality is available to control access.
