---
tags:
  - course
  - workshop
  - R
  - Julia
  - MATLAB
  - intro
  - introduction
---

# Introduction to running Julia, R, and MATLAB in HPC

Learn how to run R, MATLAB, and Julia at Swedish HPC centres. We will show you how to find and load the needed modules, how to write a batch script, as well as how to install and use your own packages, and more.
The course will consist of lectures interspersed with hands-on sessions where you get to try out what you have just learned.

We will mainly use Tetralith at NSC for the examples for the course, but there is little difference in how you use the various HPC centres in Sweden and you should have no problems applying the knowledge to the other systems.

**NOTE:** the course will **NOT** cover the topic of improving your programming skills in R, MATLAB, and Julia. Likewise, we will not cover advanced techniques for code optimization.

**NOTE** if you are interested in running Python at Swedish HPC centres, then we recommend the course "Introduction to Python and Using Python in an HPC environment" which will run 24-25 April + 28-29 April. The first day is the introduction to Python and it is possible to just participate that day.

**Remote/online participation:** The course will be completely online and we will use Zoom. More information about connecting and such will be sent to the participants close to the course.

**Prerequisites:** some familiarity with the LINUX command line (recordings from HPC2N's Linux intro here and UPPMAX Linux Intro here and also here), basic R, MATLAB, or Julia, depending on which language(s) you are interested in. See below for links to useful material if you need a refresher before the course.

## Schedule

This course will consist of three days (**9:00-16:00**), one for each language. It is a cooperation between HPC2N, LUNARC, and UPPMAX.

Full schedule can be found on the rendered presentations for each course day: <https://uppmax.github.io/R-matlab-julia-HPC/>

- **Day 1, Mon. 24. March**
    - 9:00 - 16:00 R

- **Day 2, Tue. 25. March**
    - 9:00 - 16:00 MATLAB

- **Day 3, Wed. 26. March**
    - 9:00 - 16:00 Julia

## Materials

    Exercises and .rst files can be downloaded from the course's GitHub page: <https://github.com/UPPMAX/R-matlab-julia-HPC>
    Rendered presentations can be found here: <https://uppmax.github.io/R-matlab-julia-HPC/>
    Recordings are here: TBA
    Q/A document for each day, as PDF: TBA

## Links to refresher material

This is NOT in any way mandatory for participation or part of the course. It is a list of links to useful refresher material for those who would like to read up on Julia/R/MATLAB/Linux/etc. before the course.

- Julia
    - Aalto Univ.: <https://github.com/AaltoRSE/julia-introduction>
    - Software Carpentry: <https://carpentries-incubator.github.io/julia-novice/>
- R
    - Software Carpentry: <https://swcarpentry.github.io/r-novice-gapminder/index.html>
    - Parallel R: <https://github.com/menzzana/parallel_R_course>
- MATLAB
    - Software Carpentry: <https://swcarpentry.github.io/matlab-novice-inflammation/>
    - MATLAB documentation at MathWorks: <https://se.mathworks.com/help/matlab/index.html>
- Linux intro
    - Linux intro from "Introduction to Kebnekaise": <https://hpc2n.github.io/intro-linux/>  (Recordings)
    - [Material in the UPPMAX introduction course](https://docs.uppmax.uu.se/courses_workshops/uppmax_intro_course/)
- Slurm
    - Contained in the "Introduction to Kebnekaise" course: <https://hpc2n.github.io/intro-course/batch/> (Recordings)
    - [UPPMAX Slurm guide](https://docs.uppmax.uu.se/cluster_guides/slurm/)
    - [Material in the UPPMAX introduction course](https://docs.uppmax.uu.se/courses_workshops/uppmax_intro_course/)

**Time and Dates:** 24-26 March 2025, three days, one for each language. 9:00 - 16:00 each day. The last hour each day will be used for extra time for exercises.

**Onboarding:** Friday, 21. March (1 hour - time to be decided)

**Location:** ONLINE. Zoom link will be sent to participants a few days before the course.

**Deadline for registration:** 17. March 2025

[Registration from HPC2N page](https://www.hpc2n.umu.se/events/courses/2025/spring/r-matlab-julia)

Participation in the course is free.

Please make sure have an account at SUPR as well as at NSC if you want to participate in the hands-on part of the training. There will be a course project on NSC that can be used to run the examples in during the hands-on. If you are affiliated with IRF, LTU, UMU, MIUN, or SLU and have account/project at HPC2N you can use HPC2N's local cluster if you prefer. Also, if you have an account/project at LUNARC or one at UPPMAX, you may use that instead if you want. If you do not have an account at SUPR and/or UPPMAX/HPC2N/LUNARC/NSC, you will be contacted with further instructions for how to create those. You are STRONGLY encouraged to sign up to SUPR as soon as possible after registering for the course.

NOTE:

    Kebnekaise has become a local resource. Please also read the page about "Kebnekaise will be retired as a national resource". HPC2N accounts are ONLY meant for people who are at Umeå university, one of HPC2N's partnersites (IRF, LTU, MIUN, SLU), or are in a research group with a PI at one of those.
    Cosmos (LUNARC) is also a local resource, for those at Lund University.
    UPPMAX accounts are only for local Uppsala people.
    Everyone else must use NSC for the course.

**Course project:** As part of the hands-on, you may be given temporary access to a course project, which will be used for running the hands-on examples. There are some policies regarding this, that we ask that you follow:

    You may be given access to the project before the course; please do not use the allocation for running your own codes in. Usage of the project before the course means the priority of jobs submitted to it goes down, diminishing the opportunity for you and your fellow participants to run the examples during the course. You can read more detailed information about the job policies of NSC here and NSC usage rules here.
    The course project will be open 1-2 weeks after the course, giving the participants the opportunity to test run examples and shorter codes related to the course. During this time, we ask that you only use it for running course related jobs. Use your own discretion, but it could be: (modified) examples from the hands-on, short personal codes that have been modified to test things learned at the course, etc.
    Anyone found to be misusing the course project, using up large amounts of the allocation for their own production runs, will be removed from the course project.
    You will likely also be given access to a storage area connected to the compute project. Any data you store there should be course-related and if you wish to save it you should copy it to somewhere else soon after the course as it will be deleted about a month later.

The course uses compute resources provided by the National Academic Infrastructure for Supercomputing in Sweden (NAISS) at NSC partially funded by the Swedish Research Council through grant agreement no. 2022-06725.
