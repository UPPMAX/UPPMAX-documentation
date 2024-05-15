# `projplot`

![Projplot plot](./img/projplot_regular_use.png)

`projplot` is an UPPMAX tool to plot your core hour usage

## Minimal use

`projplot` needs only the project code:

```bash
projplot -A [project_code]
```

For example:

```bash
projplot -A uppmax2020-2-2
```

Output will look similar to this:

![A projplot plot](./img/projplot_regular_use.png)

> Example `projplot` output. The horizontal axis
> shows the days before today, the vertical axis shows
> the cores used on that day (hence, the amount of core hours
> is the area under the curve).
> For this example project,
> apparently, the maximum number of cores per day is 800.

This graph shows you the projects core usage during the last 30 days.
The heights of the peaks in the plot shows you
how many cores that were used simultaneously,
and the width show you for how long they were used.

If we look at the big peak to the left in the diagram,
we can see that 15 cores were used for around 24 hours,
and somewhere in the middle of that period,
another 8 cores was used for a shorter period of time.

Since the plots are made using ordinary text,
there will sometimes be rounding errors
because of the low resolution of the terminal window,
which is usually around 80x30 characters.
The plot will adapt to your terminal window,
so increase the size of your window to increase the resolution of the plot
(the data being plotted has a resolution down to single seconds).

As time progresses the peaks in the graph will move to the left in the diagram.
In the standard plot of the last 30 days,
that means that when a peak exits the plot to the left,
your get those core hours back to the project.

### If you are over quota

If we look at a project that has used more core hours than their projects allocation,
the image will look like this:

![A projplot that is over quota](./img/projplot_over_quota.png)

There is a message about the core hour limit being reached at the top of the plot.
If you look in the diagram at around 10 days ago,
you will see the point where the core hour limit is reached
(the bar of `>`s).
This point is calculated by summing up all core hour usage
to the right of the bar.
What this means in reality is that if this project was to stop analyzing right now,
they would have to wait until the bar of `>`s has exited the graph to the left
(i.e. ~20 days) before they are below their core hour limit again.
Most of the time, projects do not completely stop analyzing,
so for each core hour they use the more to the right the `>` bar will move.

## Other options

`projplot` has more options, that are shown by using `--help`:

```bash
projplot --help
```

Below, these options are discussed in detail.

### Help

Use `--help` (or `-h`) to get a short description of the options and some examples:

```bash
projplot --help
```

???- question "How does that look like?"

    ```bash
    Usage: projplot -A <proj-id> [options]

    More details: https://uppmax.uu.se/support/user-guides/plotting-your-core-hour-usage

    Example runs:

    # Plot the last 30 days of project <proj>
    projplot -A <proj>

    # Plot the last 30 days of project <proj> on cluster <cluster>
    projplot -A <proj> -c <cluster>

    # Plot the last <n> days of project <proj>
    projplot -A <proj> -d <n>

    # Plot the usage for project <proj> since <date>
    projplot -A <proj> -s <date>

    # Plot the usage for project <proj> between <date_1> and <date_2>
    projplot -A <proj> -s <date_1> -e <date_2>

    # Plot the usage for project <proj> between <date_1> and <date_2>, on cluster <cluster>
    projplot -A <proj> -s <date_1> -e <date_2> -c <cluster>

    # Plot the usage for project <proj> between date <date_1> and <days> days later
    projplot -A <proj> -s <date_1> -d <days>

    # Plot the usage for project <proj> between date <date_1> and <days> days earlier
    projplot -A <proj> -e <date_1> -d <days>

    # Plot the last 30 days of project <proj>, but don't check the queue for running jobs
    projplot -A <proj> -R


    Options:
      -h, --help            show this help message and exit
      -A ACCOUNT, --account=ACCOUNT
                            Your UPPMAX project ID
      -c CLUSTER, --cluster=CLUSTER
                            The cluster you want to plot (default: current
                            cluster)
      -d DAYS, --days=DAYS  The number of days you want to plot (default: none)
      -s START, --start=START
                            The starting date you want to plot (format: YYYY-MM-
                            DD)
      -e END, --end=END     The ending date you want to plot (format: YYYY-MM-DD)
      -R, --no-running-jobs
                            Use to skip including running jobs in the plot
                            (faster). Useful if you are not running any jobs and
                            want to save time.
    ```

### Number of days

Use `--days` (or `-d`) the plot a custom number of days,
instead of the default of 30 days:

```bash
projplot -A [project_code] --days [number_of_days]
```

For example, this will plot the last 45 days:
:

```bash
projplot -A uppmax2020-2-2 --days 45
```

### Starting date

Use `--start` (or `-s`) to specify a custom starting date,
from when the time in your plot will start:

```bash
projplot -A [project_code] --start [starting_date_in_yyyy-mm-dd_format]
```

For example:

```bash
projplot -A uppmax2020-2-2 --start 2023-05-03
```

will give you a plot starting on the date 2023-05-03
and the default number of days after that date.
The command below does exactly the same, yet makes the default
number of days explicit:

```bash
projplot -A uppmax2020-2-2 --start 2023-05-03 --days 30
```

### Ending data

Use `--end` (or `-e`) to specify a custom ending date,
from when the time in your plot will end:

```bash
projplot -A [project_code] --end [ending_date_in_yyyy-mm-dd_format]
```

For example:

```bash
projplot -A uppmax2020-2-2 --end 2023-05-03
```

will give you a plot ending on the date 2023-05-03
and the default number of days before that date.
The command below does exactly the same, yet makes the default
number of days explicit:

```bash
projplot -A uppmax2020-2-2 --end 2023-05-03 --days 30
```

### Start and end date combined

Use `--start` and `--end` combined to specify a custom range
of dates for your plot:

```bash
projplot -A [project_code] --start [starting_date_in_yyyy-mm-dd_format] --end [ending_date_in_yyyy-mm-dd_format]
```

For example:

```bash
projplot -A uppmax2020-2-2 --start 2022-05-03 --end 2023-05-03
```

### Cluster

Use `--cluster` (or `-c`) to determine which UPPMAX cluster to plot.
By default, the current cluster is used.

Since the different clusters at UPPMAX have separate core hour quotas,
it makes sense to being able to plot them separately.

```bash
projplot -A [project_code] -c [cluster_name]
```

For example:

```bash
projplot -A uppmax2020-2-2 -c snowy
```

Valid cluster names are `bianca`, `rackham` and `snowy`.

???- question "How to get valid cluster names?"

    Use `projplot` with a nonsense clustername:

    ```bash
    projplot -A uppmax2020-2-2 --cluster nonsensename
    ```

    The error message will display valid cluster names.

This option can be combined with all the other options.

### Exclude running jobs

Use `--no-running-jobs` (or `-R`) to skip checking the queue for running jobs.

If you don't have any running jobs,
asking the queue system to list jobs is just a waste of time
(anywhere 1-15 seconds).
By giving `--no-running-jobs` when running `projplot`,
it skips checking the queue and if you do have jobs running,
they will not be visible in the plot or in the sum of core hours used.

```bash
projplot -A [project_code] --no-running-jobs
```

For example:

```bash
projplot -A uppmax2020-2-2 --no-running-jobs
```
