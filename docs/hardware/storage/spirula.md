# Spirula

Spirula is a DDLS-funded SciLifeLab FAIR Data Storage system which exposes 10
PB of raw S3 compatible object storage (or blob storage) through Ceph Object
Gateway, also known as RADOS Gateway (RGW).

- Spirula is not in production.
- There is no backup of any data stored on Spirula.
- You should not store any primary data on Spirula.
- Spirula does not expose any public endpoints.

See [storage systems](../../cluster_guides/uppmax_storage_system.md) for other
storage systems at UPPMAX.

## Support

The responsibility for Spirula is shared between UPPMAX and SciLifeLab.

Spirula is accessible from within UPPMAX and from certain whitelisted
SciLifeLab addresses. Access to Rackham/Pelle is not granted for projects with
Spirula allocations, in cases where you don't have access to Rackham/Pelle
through some other means please refer to <FAIRstorage@scilifelab.se> for more
information.

In general follow these guidelines when requesting support.

Contact SciLifeLab DC at <FAIRstorage@scilifelab.se> for issues regarding:

- Project grants, allocations and quota in SUPR.
- Access to Spirula through SciLifeLab addresses.
- FAIR Storage and the intended use-cases for Spirula.

Contact UPPMAX Support at <support@uppmax.uu.se> for issues regarding:

- Retrieving access tokens and/or quota from the SSH service.
- Technical implementation and/or limitations of the system.


## Usage

### Access tokens and displaying usage quota

If you are able to `ping` and `ssh` to `s3.spirula.uppmax.uu.se` you can
interact with UPPMAX's _SSH to S3 credential service_. You will login the
service using your UPPMAX user account and second factor authentication.

```sh
ssh s3.spirula.uppmax.uu.se
Password: ********
Two factor (UPPMAX): 123456
 _   ________________  ___  ___  __   __      _____       _            _
| | | | ___ \ ___ \  \/  | / _ \ \ \ / /     /  ___|     (_)          | |
| | | | |_/ / |_/ / .  . |/ /_\ \ \ V /______\ `--. _ __  _ _ __ _   _| | __ _
| | | |  __/|  __/| |\/| ||  _  | /   \______|`--. \ '_ \| | '__| | | | |/ _` |
| |_| | |   | |   | |  | || | | |/ /^\ \     /\__/ / |_) | | |  | |_| | | (_| |
 \___/\_|   \_|   \_|  |_/\_| |_/\/   \/     \____/| .__/|_|_|   \__,_|_|\__,_|
                                                   | |
                                                   |_|
You have 2 available credentials. Please select which credential to use:
0: User tintin in sll1234001
1: Project user for sll1234001
```

After selecting which credentials you want to use you can either retrieve your
access credentials or view your current usage and quota.

```sh
SSH to S3 credentials service - v0.2
-------------------------------------------
You have several options. Please select what you want to do.
1: Retrieve S3 Access Credentials
2: View Current Quota
```


### Configuring a S3 client

Spirula through the Ceph Object Gateway supports multiple S3 compliant clients
such as `aws cli` or `s3cmd`. Setup differs between tools, adopt the
configuration below to your particular needs.


#### AWS CLI

For setting up AWS command line interface `aws cli` to use Spirula you can
create or update the `~/.aws/config` configuration file with the following
options:

```bash
# ~/.aws/config
[default]
region = None
endpoint_url = https://s3.spirula.uppmax.uu.se:8443
```

Full usage instructions and configuration options for `aws cli`  are available
through AWS
[documentation](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html).
