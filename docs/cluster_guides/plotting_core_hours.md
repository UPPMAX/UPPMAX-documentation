# Plotting your core hour usage
In IG: Support / User guides / Plotting your core hour usage

Basic plots
To get a graph over your core hour usage, use the tool projplot

Syntax: $ projplot -A proj-id [options]

Options:

  -h, --help:   Show this help message and exit
  -A ACCOUNT, --account=ACCOUNT:   Your UPPMAX project ID
  -c CLUSTER, --cluster=CLUSTER:   The cluster you want to plot (default: current cluster)
  -d DAYS, --days=DAYS:   The number of days you want to plot (default: none)
  -s START, --start=START:   The starting date you want to plot (format: YYYY-MM-DD)
  -e END, --end=END:   The ending date you want to plot (format: YYYY-MM-DD)
  -R, --no-running-jobs:   Use to skip including running jobs in the plot (faster). Useful if you are not running any jobs and want to save time.

As seen in the syntax description, the only mandatory argument is the -A flag. It specifies the project you want to plot the core hour usage of.

Example:

$ projplot -A b2010074
which will give you a picture like this, after ~10 seconds: 

basic projplot

This graph shows you the projects core hour usage during the last 30 days. The heights of the peaks in the plot shows you how many core that was used simulatiously, and the width show you for how long they were used.

If we look at thebig peak to the left in the diagram, we can see that ~15 core was used for ~24 hours, and somewhere in the middle of that period, another ~8 cores was used for a shorter period of time. Since the plots are made using ordinary text (ascii), there will sometimes be rounding errors because of the low resolution of the terminal window (usually 80x30 or there about). The plot will adapt to your terminal window, so increase the size of your window to increase the resolution of the plot (the data being plotted has a resolution down to single seconds).

As time progresses the peaks in the graph will move to the left in the diagram. In the standard plot of the last 30 days, that means that when a peak exits the plot to the left, your get those core hours back the the project.

If you are over quota
If we look at a project that has used more core hours than their projects allocation, the image will look like this:

Over limit

There is a message about the core hour limit being reached at the top of the plot. If you look in the diagram at ~10 days ago, you will see the point where the core hour limit is reached (the bar of greater-than-signs). This point is calculated by summing up all core hour usage to the right of the bar. What this means in reallity is that if this project was to stop analyzing right now, they would have to wait until the bar of greater-than-signs has exited the graph to the left (i.e. ~20 days) before they are below their core hour limit again. Most of the time, projects do not completely stop analyzing, so for each core hour they use the more to the right the greater-than-sign bar will move.

More options
There are a couple of options your can specify to modify the plot.

-d or --days, custom number of days
Default: 30

If you want to see more (or less) days than the default 30, you can specify it with the -d option. 


$ projplot -A proj-id -d 45
will plot the last 45 days.

-s or --start, custom starting point
If you specify -s in your command you will change where in time your plot will start. 


$ projplot -A proj-id -s YYYY-MM-DD
will give you a plot starting on the date YYYY-MM-DD and 30 days after that date (can be combined with the -d option to give you an arbitrary number of days).

-e or --end, custom ending point
As with the -s option, this will give you a plot that ends on the specified date, and 30 days before that date (can be combined with the -d option to give you an arbitrary number of days).


$ projplot -A proj-id -e YYYY-MM-DD
-s and -e combined
As you might have guessed, this will give you a plot of the interval you have specifed, no matter how long it is.


$ projplot -A proj-id -s YYYY-MM-DD -e YYYY-MM-DD
-c or --cluster, which cluster to plot
Default: current cluster

Since the different clusters at uppmax have separate core hour quotas, it makes sense to being able to plot them separately. This option can be combined with all the other options.


$ projplot -A proj-id -c tintin
-h or --help, show you this information
The help will print a short description of the options and some examples.

$ projplot -h

-R or --no-running-jobs, skip checking the queue for running jobs
If you don't have any running jobs, asking the queue system to list jobs is just a waste of time (anywhere 1-15 seconds). By giving -R when running projplot, it skips checking the queue and if you do have jobs running, they will not be visible in the plot or in the sum of core hours used.

$ projplot -A proj-id -R
