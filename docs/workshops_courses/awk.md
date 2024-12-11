# Awk workshop
AWK is an interpreted programming language designed for text processing and typically used as a data extraction and reporting tool.

This two-days workshop aims to promote and demonstrate the flexibility of the tool, where the overhead of more sophisticated approaches and programming languages is not worth the bother.

Learn how to

- use Awk as an advanced grep command, capable of arithmetic selection rules with control over the content of the matched lines
- perform simple conversions, analysis or filter you data on the fly making it easy to plot or read in your favorite research tool
- handle and take advantage on data split over multiple file data sets.
- use Awk as simple function or data generator
- perform simple sanity checks on your results
- Awk for bioinformaticians

Use what you learn and dive into the basic concepts of bioinformatics with simple exercises on typical scientific problems and tasks.

## Venue and registration:

Date: 16 and 17 January, 2025
Time: 9:15 - 12:00 and 13:15 -16:00
Location: Zoom: link wil be sent to applicants
Application: form.

## Schedule

1-st day 9:15 - 12:00
Seminar session
Examples of typical problems suitable for Awk “treatment”
Introduction to the basics of Awk scripting language
Solving interactively simple problems
Lunch break
Exercises 13:15 -16:00
Solving interactively the exercise problems
2-nd day 9:15 - 12:00
Awk for bioinformaticians - seminar
Case Study: Manipulating the output from a genome analysis - vcf and gff
Filtering and formatting raw data
Counting and piling features
Indexing and hashing to compare variants and annotations
Lunch break
Walk-through session on various topics:
Awk parsing “simultaneously” multiple input files
Multiple input files - second approach scenario will be discussed.
How to trick awk to accept options on the command line like regular program i.e. $ script.awk filename parameter1 parameter2 link
Declaring and calling functions in awk - link
Input/output to/from an external programs
Learn how to send input to an external program (might be based on your data) and read the result back - link
Handy tips: awk oneliners use with Vim, gnuplot…
Also: Suggest topic for discussion or see recently suggested topics.

## Prerequisites

### MacOS
The system provided awk version will work for most of the examples during the workshop with few exceptions, which are noted in the online material.

Tilda ~ sign on Mac with Swedish keyboard layout - Alt + ^

### Linux

Several distributions have other awk flavors installed by default. The easiest fix is to install the gnu version gawk i.e. for Ubuntu: sudo apt install gawk

### Windows 10

Ubuntu for Windows 10 - it is better to read from the source, despite it might not be the easiest tutorial. To my experience, this is the best Linux environment without virtualization.
MobaXterm use the internal package manager to install gawk. The default is provided by Busybox and is not enough for the purpose of the workshop.
Linux computer center
Just login to your account and use the provided awk - any version newer than 4 will work.
rackham3:[~] awk -V GNU Awk 4.0.2 Copyright (C) 1989, 1991-2012 Free Software Foundation.

### Virtual Linux Machine

Just follow some tutorial on how to setup and use the virtual Linux environment.

### VirtualBox

Ubuntu on Public Clouds
GitHub & Binder (you need only a browser)
Singularity
singularity run shub://pmitev/Teoroo-singularity:gawk 'BEGIN{ for(i=1;i<=4;i++) print i}'

## Feedback from previous workshops:

2024.08 | 2024.01
2023.09 | 2023.01*
2022.09 | 2022.01
​2021.09 | 2021.01
2020.08 | 2020.01
2019.08 | 2019.01
2018.08 | 2018.01
2017.01 | 2017.08
2016.08 | 2016.01
2015.10
* not enough data to be anonymous

## Contacts for the course:

Pavlin Mitev
Jonas Söderberg
Lars Eklund
Richel Bilderbeek
UPPMAX

