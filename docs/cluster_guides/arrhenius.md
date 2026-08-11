# Arrhenius

Arrhenius is a future NAISS cluster and likely the successor
of Bianca and Rackham and Tetralith.

Some of its features, as shown at the NAISS User Meeting
of 2024-10-01 (and are likely to change):

- Around 40 PFlops
- Has CPUs and GPUs
- Allows for regular and sensitive data
- Allows for cloud services
- Allows for AI
- Storage about 27 PB for regular data, 10 PB for sensitive data
- 65% will be owned by Sweden (the numbers above show the values for the
  complete cluster)


<!--

This email is the first of several to be sent by NAISS before and during the start of Arrhenius.

The HPC partition of Arrhenius is scheduled to open for general use on June 1st, 2026. The HPC partition consists of:

·      HPC CPU partition,

·      HPC GPU partition and

·      Lustre file system.

At this stage, the hardware has just been installed and accepted, and NAISS has just started using most of the delivered HW, so the start date is still somewhat uncertain.

As you know, Arrhenius will replace the following NAISS resources:

·      Alvis with Mimer Storage at Chalmers,

·      Tetralith with NSC Center Storage at Linköping University,

·      Dardel with Klemming at KTH,

·      Bianca for sensitive data at Uppsala University,

·      Swedish Science Cloud (SSC).

Moving all projects and users from the existing NAISS computers to Arrhenius will require considerable time and effort.

These are the current end-dates for operating these systems as NAISS resources:

 

Alvis

2026-09-30

Tetralith

2026-09-30

Dardel

2026-12-31

Bianca

2026-12-31

SSC

2026-06-30

 

The idea is to start with Alvis and Tetralith as soon as possible.

Please note that Alvis and Tetralith will have a gradually decreasing number of active nodes from 2026-07-01.

The move of the Dardel data is expected to start on October 1. It will follow the same principles as for Alvis and Tetralith. More information will be available after the summer.

Sensitive data from Bianca will be moved by the Sensitive Data team, together with the users, when the Arrhenius SENS partition is ready in September 2026. Information will be handled in a separate email.

Also, the Persistent Compute and Data partition of Arrhenius, which will replace the Swedish Science Cloud, is planned to be taken into use in June 2026. Since the current number of users on the Science Cloud is limited, information about that transition will be handled in a separate email.

Test users on HPC
During the second part of May, we plan to have test users from various scientific fields evaluate the HPC system to identify issues and verify functionality before general use. Those users will be selected by NAISS and contacted separately.

User names
Each user who is a member of a NAISS/SUPR project on Arrhenius must create a login account and select a username, password, and two-factor secret for Arrhenius in SUPR. This functionality is planned to be available to test users when Arrhenius is ready for testing and to other users from June 1.

Different types of storage on Arrhenius
Arrhenius HPC has two types of storage:

·      Flash storage (2 PB) can be used for data to applications with stringent bandwidth requirements.

·      Disk (25 PB) for home directories, applications, and projects with normal HPC requirements.

Each storage partition is allocated separately. Users coming from Alvis will receive a small allocation of Flash storage. For other users to obtain a quota for Flash storage, a justification must be submitted to NAISS support. In the future, request Flash storage when you apply for another allocation.

SENS has a separate secure storage area of 10 PB, and the Persistent Computing and Data (PCD) has a separate object storage of 2.5 PB (raw data). Existing allocations on SENS will just be moved over. For future allocations, these storage areas will be granted at the same time you apply for an allocation on the SENS and PCD partitions, respectively.

Please note that the storage sizes mentioned above are the total capacity and include the EuroHPC part of 35% of the total capacity.

Storage Allocations
NAISS has identified a considerable amount of data on the existing systems that hasn’t been used for a long time (cold data). The disk system of Arrhenius is a parallel file system built for high capacity. It is not sustainable to continue to use this more expensive disk system for cold data. Also, NAISS has only the mission of providing data storage during processing, so Arrhenus will have a file system dimensioned only for regularly used data. This means that many projects will receive smaller allocations on Arrhenius than their previous total allocation on Alvis, Tetralith and Dardel.

Projects must ensure that the data they plan to move to Arrhenius fits within Arrhenius's storage allocation (total size and number of files). This must be ready before the actual move.

Alvis users should note that Arrhenius will have a quota for the number of files per project. The initial value for this quota is estimated and set by NAC. For data moved from Alvis, the Python and Conda environments will not be moved, since they can’t be used directly on Arrhenius; see https://www.c3se.chalmers.se/news/alvis-data-migration/ for more information.

Since Alvis has not had a file count quota, projects migrating from Alvis will be allowed to temporarily exceed the file count quota for 90 days to facilitate the move.

To help users store cold data, NAISS will soon provide a cost-efficient object storage system at self-cost.

Current Tetralith users can run the storagereport command to get an overview of which data is "cold" (not accessed for a long time). The PI and proxy can request help from NAISS to access and delete data in the project storage directory regardless of file permissions.

HPC Computing Allocations
HPC projects ending after June 1st (from Alvis and Tetralith) will automatically have their allocations scaled and transferred to Arrhenius. Since Arrhenius is equipped with faster CPUs and GPUs, allocations will be scaled down to keep the actual capacity similar. Projects with new allocations for Arrhenius will be started using the allocations approved by NAC.

Test of Arrhenius BEFORE the data move.
 

We strongly advise projects to start testing Arrhenius at an early stage, when Arrhenius is opened before all users, and their data is moved. Although the most widely used applications will be available on Arrhenius from day one, not all will be installed and tested at launch. Also, an application developed or used by only one project may need to be ported by that project. Please select suitable experienced users to do an early test of the software. Please use a small but relevant data set. The data and program files for this initial test can be moved over by the users. Instructions for that will be available on the Arrhenius documentation pages, see https://hpc.pages.naiss.se/user-documentation/support-docs/arrhenius_hpc/basics/quickstart/#transfer-of-files

When applications or other required software or functionality are missing, NAISS support should be informed, and it will try to install software prioritised by the estimated user base and the order in which requests are received.

 

Choices for moving data to Arrhenius
 

Please note that all data to be used on Arrhenius needs to be moved from the source system. Even if Tetralith is also located in Linköping, the file systems of Arrhenius and Tetralith are completely separate.

 

The Principal Investigator (PI) or the project (or someone he/she delegates this to) should plan the migration, including when and how to move the project’s data. NAISS, together with the local support staff, can help projects move data. The principal investigator or the selected deputy is responsible for coordinating the data move and communication within the project and with NAISS. The planning should be based on the tests in the previous paragraph. So if a project is missing essential functionality or applications on Arrhenius, you should request a late move and contact NAISS support for further assistance.

 

Each project can suggest when its project data should be moved to Arrhenius. Note that data will be unavailable from the source computer when the move starts and will later be removed from the source. Note that moving the data can take considerable time if the number of files is large. Also note that home directories are not moved by NAISS since they are small and are fairly dependent on the actual system. Instructions for moving home directories will be available on the Arrhenius documentation pages; see https://hpc.pages.naiss.se/user-documentation/support-docs/arrhenius_hpc/basics/quickstart/#transfer-of-files.

 

We suggest that the PI or deputy, as soon as possible, selects to move the project data according to one of the following options:

 

·      as soon as possible

·      start on a specific date

·      as late as possible

·      with no help from NAISS. This alternative can cause problems, so we don’t recommend it.

·      The PI must also specify where the data should be moved from.

 

Please note that:

NAISS will move project data only once per project and per computer. In exceptional circumstances, we can make exceptions - contact NAISS support to request this.
NAISS will only move data, not copy it. If you absolutely need a writable copy left, contact NAISS support to discuss this.
The latest selectable date for Alvis/Mimer is 2026-08-31.
 

 

On Tetralith
For example, move data from Tetralith /proj/DIRECTORYNAME to the corresponding project storage on Arrhenius, /nobackup/proj/disk/DIRECTORYNAME/from-tetralith. The PI can choose from:

·      No move

·      Move the entire project directory to Arrhenius, e.g., /proj/disk/DIRECTORYNAME will be moved to /nobackup/proj/disk/DIRECTORYNAME/from-tetralith

·      Move the subdirectory of the project directory named to-arrhenius to Arrhenius, e.g.

/proj/disk/DIRECTORYNAME/to-arrhenius will be moved to

/nobackup/proj/disk/DIRECTORYNAME/from-tetralith

 

For more information on the move of files from Tetralith, see https://hpc.pages.naiss.se/user-documentation/support-docs/arrhenius_hpc/basics/quickstart/#transfer-of-files

 

On Alvis
For example, move data from Alvis:

/mimer/NOBACKUP/groups/DIRECTORYNAME/to-arrhenius-disk

to the corresponding project storage on Arrhenius:

/nobackup/proj/disk/DIRECTORYNAME/from-alvis

and from  /mimer/NOBACKUP/groups/DIRECTORYNAME/to-arrhenius-flash

 to /nobackup/proj/flash/DIRECTORYNAME/from-alvis. 

The PI can choose from:

·      No move

·      Move the subdirectories of the project directory named to-arrhenius-disk to Arrhenius Disk and to-arrhenius-flash to Arrhenius Flash.

Note that it is not possible to move the entire directory from Alvis. It has to be divided into flash and disk.

 

For more information on the move of files from Alvis, see https://www.c3se.chalmers.se/news/alvis-data-migration/

 

 

Best Regards

Gert Svensson

NAISS

-->
