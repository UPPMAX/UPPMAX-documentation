# MariaDB server on Pelle

> Note: default configuration allows only connections from localhost.

## Initializing the MariaDB server-database

### Load MariaDB module

```bash
module load MariaDB/11.7.0-GCC-13.3.0
```

### Create mariadb_data directory

```bash
export MARIADB_DATA=/proj/uppmax-XXX-xx/mariadb_data
mkdir -p $MARIADB_DATA
```

### Initialize the database

```bash    
mariadb-install-db --datadir=$MARIADB_DATA

Installing MariaDB/MySQL system tables in '/proj/uppmax-XXX-xx/mariadb_data' ...
OK
...
```

### Start the server

```bash
mariadbd-safe --datadir=$MARIADB_DATA &

mysqld_safe Logging to '/proj/uppmax-XXX-xx/mariadb_data/pelle1.uppmax.uu.se.err'.
251126 13:53:07 mysqld_safe Starting mariadbd daemon with databases from /proj/uppmax-XXX-xx/mariadb_data
```

### Check the user

```bash
 mariadb -e "SELECT User, Host, plugin, Password , authentication_string FROM mysql.user WHERE User='$USER';"
+--------+-----------+-----------------------+----------+-----------------------+
| User   | Host      | plugin                | Password | authentication_string |
+--------+-----------+-----------------------+----------+-----------------------+
| sven   | localhost | mysql_native_password | invalid  | invalid               |
+--------+-----------+-----------------------+----------+-----------------------+
```

### Stop the server 

```bash
mariadb-admin shutdown
```

## New user and changing passwords

It is convenient to have separate user with password for the purpose of running a tool and still be able to administer (start and stop the server) with the default user created during the database initialization, which does not require password.

```bash
mariadb

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 11.7.0-MariaDB Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    
MariaDB [(none)]>
```

Type the SQL commands bellow. Please, select different PASSWORD !!!

```sql
-- Create user with all privileges and remote access
-- Replace '%' with specific IP if you want to restrict remote access
CREATE USER 'newuser'@'%' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

## Set/change password of the default user if necessary

!!! Please select different PASSWORD !!!

```bash
mariadb -e "ALTER USER '$USER'@'localhost' IDENTIFIED VIA mysql_native_password USING PASSWORD('changeme'); FLUSH PRIVILEGES;"
```

### Check again, now you need to provide password

```bash
mariadb -p -e "SELECT User, Host, plugin, Password , authentication_string FROM mysql.user WHERE User='$USER';"
Enter password: 
+--------+-----------+-----------------------+-------------------------------------------+-------------------------------------------+
| User   | Host      | plugin                | Password                                  | authentication_string                     |
+--------+-----------+-----------------------+-------------------------------------------+-------------------------------------------+
| sven   | localhost | mysql_native_password | *7ACE763ED393514FE0C162B93996ECD195FFC4F5 | *7ACE763ED393514FE0C162B93996ECD195FFC4F5 |
+--------+-----------+-----------------------+-------------------------------------------+-------------------------------------------+
```

## Example SLURM sbatch job

```bash
#!/bin/bash -l
#SBATCH -Jtest
#SBATCH -A project
#SBATCH -t 00:15:00
...

# Load MariaDB module
module load MariaDB/11.7.0-GCC-13.3.0

export MARIADB_DATA=/proj/uppmax-XXX-xx/mariadb_data
# Start the server
mariadbd-safe --datadir=$MARIADB_DATA &
sleep 5

# Start the main program
start_my_program

# Stop the server
mariadb-admin shutdown
```

## Links

- [Quick start guides](https://mariadb.com/docs/server/mariadb-quickstart-guides)
- [Remote connections](https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-remote-connection-guide)
