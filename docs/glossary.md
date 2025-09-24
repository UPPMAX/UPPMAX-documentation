# Glossary

This glossary contains key terms used in UPPMAX documentation and computing environments.

## B

### Batch Job
A computational task that is submitted to the job scheduler (Slurm) to run non-interactively. Batch jobs are submitted using job scripts and run when resources become available.

### Bianca
[Bianca](cluster_guides/bianca.md) is one of the [UPPMAX clusters](cluster_guides/uppmax_cluster.md), suitable for working with sensitive data. Bianca is internet-restricted for security reasons.

## C

### Command Prompt
The text at the start of the line in a terminal where you can type commands. It indicates that the terminal is waiting for user input. For example: `[sven@rackham2 my_folder]$`.

### Compute Node
A computer in an HPC cluster that performs the actual computational work. Users run their jobs on compute nodes, as opposed to login nodes which are used for system access and light tasks.

## F

### FileZilla
A user interface application to send data from your computer to UPPMAX clusters and vice-versa. FileZilla provides a graphical interface for file transfers.

## G

### GUI
Graphical User Interface - a visual interface for taking user inputs, as opposed to command-line interfaces.

## I

### Interactive Session
A computing session where users can interactively run commands and programs on compute nodes. Unlike batch jobs, interactive sessions provide real-time interaction with the system.

## J

### Job
A computational task submitted to the cluster's job scheduler (Slurm). Jobs can be either batch jobs (non-interactive) or interactive sessions.

## L

### Login Node
A computer where users first arrive after logging in to an UPPMAX HPC cluster. Login nodes are shared resources used for system access, file management, and job submission, but not for intensive computations.

## M

### Modules
Software modules are a way to manage different versions of software on UPPMAX clusters. The [module system](cluster_guides/modules.md) allows users to load specific versions of software tools and libraries.

## N

### NAISS
National Academic Infrastructure for Supercomputing in Sweden. The organization that coordinates high-performance computing resources across Swedish universities.

## P

### Pelle
[Pelle](cluster_guides/pelle.md) is an upcoming general-purpose UPPMAX cluster, paid by Uppsala University. Uppsala users of Rackham will be moved to Pelle.

### Principal Investigator (PI)
The researcher in charge of a research project who is responsible for applying for computational resources and managing project membership. PIs can add members to projects and accept membership applications.

### Project
A computational allocation on UPPMAX resources. Projects have associated compute time, storage quotas, and user memberships managed through SUPR.

### Proj
The project folder in UPPMAX clusters that is shared among all project members. This folder is secure and isolated from the internet.

## R

### Rackham
[Rackham](cluster_guides/rackham.md) is one of the UPPMAX clusters that serves as a general-purpose cluster. Rackham will be replaced by Pelle in the future.

## S

### Slurm
Simple Linux Utility for Resource Management - the job scheduler used on UPPMAX clusters. Slurm manages the allocation of computational resources and schedules when jobs are executed.

### Snowy
[Snowy](cluster_guides/snowy.md) is one of the UPPMAX clusters. Snowy is different from other clusters as it has no dedicated login nodes - access is done via Rackham login nodes.

### SSH
Secure Shell - a protocol and tool for secure remote access to computer systems. SSH is used to connect to UPPMAX clusters from remote locations.

### SUNET
Swedish University Network - the network that connects Swedish universities and research institutions. Users must be inside SUNET to access certain UPPMAX resources like Bianca.

### SUPR
Swedish User and Project Repository - the web portal at [https://supr.naiss.se/](https://supr.naiss.se/) where users manage their accounts, apply for projects, and request access to computational resources.

### SUPR Account
An account that gives access to project management functionality for submitting project proposals on SUPR and managing computational resources.

## T

### Terminal
A program that allows you to run commands through a text-based interface. Also called a command-line interface or console.

### Two-Factor Authentication (2FA)
A security method that requires two forms of identification to access an account. UPPMAX requires 2FA for enhanced security, typically using a password and a code from a mobile device.

## U

### UPPMAX
Uppsala Multidisciplinary Center for Advanced Computational Science - the organization that operates several high-performance computing clusters in Sweden.

### UPPMAX Account
An account that gives access to UPPMAX servers and clusters, such as Bianca, Rackham, Snowy, and Pelle.

## V

### VPN
Virtual Private Network - a service that allows users to connect to SUNET (Swedish University Network) from outside locations, enabling access to UPPMAX resources that require being inside the university network.

## W

### Wharf
A special folder on Bianca that acts like a "postbox" for data/file exchange between the internet-restricted Bianca cluster and the outside world. Files should not be kept in wharf long-term for security reasons.

### WinSCP
A Windows application that provides a user interface for transferring data between your local computer and UPPMAX clusters.