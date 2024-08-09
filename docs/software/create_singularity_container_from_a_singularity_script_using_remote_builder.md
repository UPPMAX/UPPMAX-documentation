---
tags:
  - Singularity
  - Singularity script
  - create
  - build
  - website
  - Sylabs
  - remote builder
---

# Create a Singularity container from a Singularity script using a website

There are multiple ways how to [create a Singularity container from a Singularity script](create_singularity_container_from_a_singularity_script.md).

This page shows how to do so using a website

## Procedure

### 1. Go to to Sylabs website

Go to [the Sylabs website](https://www.sylabs.io/)

???- question "How does that look like?"

    The Sylabs website looks similar to this:

    ![The Sylabs website](./img/sylabs_select_container_services.png)

### 2. Got to the Sylabs Singularity Container Services website

On [the Sylabs website](https://www.sylabs.io/),
click 'Products | Singularity Container Services'

???- question "Where to click?"

    Click here:

    ![The Sylabs website](./img/sylabs_select_container_services.png)

You will be takes to the 'Singularity Container Services'.

???- question "How does that look like?"

    The Singularity Container Services website looks similar to this:

    ![The Singularity Container Services website](./img/sylabs_container_services_not_logged_in.png)

### 3. Sign in or sign up

At the 'Singularity Container Services' website, click 'Sign Up' or 'Sign In'

???- question "How does signing in look like?"

    Signing in looks similar to this:

    ![Signing in to the Singularity Container Services](./img/sylabs_sign_in.png)

You are now logged in at the 'Singularity Container Services':

???- question "How does that look like?"

    The Singularity Container Services looks similar to this after logging in:

    ![Logged in](./img/sylabs_container_services_logged_in.png)

### 4. Go to the remote builder

Click on 'Remote builder'.

???- question "Where to click?"

    Click here:

    ![Here is where you can click on 'Remote builder'](./img/sylabs_container_services_logged_in_click_remote_builder.png)

### 5. Setup the remote builder

The remote builder shows a Singularity script and some default settings.

???- question "How does that look like?"

    The remote builder's default settings look similar to this:

    ![The remote builder's default settings](./img/sylabs_remote_builder_first_content.png)

Make the following changes:

- paste your Singularity script in the text box
- change `Repository` to a valid name (as indicated), for example, as `default/my_container`

???- question "How does that look like?"

    The remote builder with modified values looks similar to this:

    ![Filled in values](./img/sylabs_click_submit_build.png)

### 6. Let the container be built

Click 'Submit Build'.

???- question "Where to click?"

    Click here:

    ![Click 'Submit Build'](./img/sylabs_click_submit_build.png)

The building will start.

???- question "How does that look like?"

    A build that has just started looks similar to this:

    ![Building in progress](./img/sylabs_view_remote_build_in_progress.png)

After a while the building will be done.

???- question "How does that look like?"

    A build that has finished looks similar to this:

    ![Building done](./img/sylabs_view_remote_build_done.png)

### 7. Download the container

There are multiple ways to download your Singularity container:

- Download from the website: click on 'View image',
  then scroll down and click 'Download'

???- question "How does that look like?"

    Click on 'View image' here:

    ![Click on 'View image'](./img/sylabs_remote_builder_click_view_image.png)

    The 'View image' page looks similar to this:

    ![View image](./img/sylabs_view_image.png)

    At the 'View image' page, scroll down to find the 'Download' button:

    ![View image and click on Download](./img/sylabs_view_image_download.png)

- Use a `singularity pull`

For example:

```bash
singularity pull library://sven/default/my_container
````

???- question "How does that look like?"

    For example:

    ```bash
    $ singularity pull library://pontus/default/sortmerna:3.0.3
    WARNING: Authentication token file not found : Only pulls of public images will succeed
    INFO:    Downloading library image
     65.02 MiB / 65.02 MiB [=========================================================================================================================================] 100.00% 30.61 MiB/s 2s
    ```

### 8. Use the container

How to use a container, depends on what it does.

Here are some thing to try:

Run the container without arguments, in the hope of getting a clear error message with instructions:

```bash
./my_container.sif
```

Run the container in the hope of seeing its documentation:

```bash
./my_container.sif --help
```

Run the container on the local folder, in the hope of getting a clear error message with instructions:

```bash
./my_container.sif .
```
