# Allinea DDT - Distributed Debugging Tool

UPPMAX has 96 licenses (one license per (MPI) process) that allows you to debug programs running in parallel with up to 6 nodes on 16 cores or any other combination. The licenses are shared between all users that are in active debugging session.

To use the graphical user interface (GUI) make sure you have X11 forwarded when connecting to Tintin.

$ ssh -Y rackham.uppmax.uu.se
To use the program load the ddt module from you command line.

$ module load ddt
Make sure you have compiled your code with debugging flag options!

To start the program run:

$ ddt

or

$ ddt ./myprogram
Debugging Multithreaded programs:
Start an interactive job with multiple cores (e.g. "interactive -p core -n 20 -A snicXYZ -t 04:00:00") before starting DDT. In the run window, select the OpenMP box. You can change the number of OpenMP threads directly in the DDT window before running.

Debugging MPI programs:
To be able to debug MPI program select MPI option as well as the "Submit to Queue" option, and then click on "Change" to select submission script configuration for Rackham and provide the job specific options.



System> select "Auto-Detect" for "MPI/UPC Implementation" and tick "Create Root and Workers group automatically".



Job Submission> Browse and select "/sw/comp/ddt/7.0/templates/rackham-core.qtf" in the filed "Submission template file:". Make sure that "Quick Restart" is also ticked. This will allow you to restart your program without cancelling the allocated time and allocating it again. (There is also a rackham-node.qtf in the same directory as the rackham-core.qtf configuration, this will allow you to submit the node and devcore partitions as well.)



"Edit Queue Submission Parameters..." to specify Partition, Project and requested time. Failing to provide project number will cause failures in the submission process.



On the main configuration window the button "Run" will change to "Submit". Click on this button to submit your debugging session to the queue manager.

If you enable "Memory debugging", click the "Details" button and tick "Preload the memory debugging library" and select "C/Fortran threads" in the "Language:" field. Read the manual for more detail on the other options in this panel.



Useful links

Allinea DDT home page

Support, known issues and release history

User Guide
