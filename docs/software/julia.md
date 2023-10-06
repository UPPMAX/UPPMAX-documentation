# Julia user guide


## Julia installations

 There is no system-installed Julia on the clusters. Therefore you need to load Julia with the module system. Different versions of Julia are available via the module system on Rackham, Snowy, and Bianca. Some installed packages are available via the module.

As the time of writing we have the following modules:

[user@rackham1 ~]$ module avail julia
------------------------------------------------------
julia:
------------------------------------------------------
Versions:
        julia/1.0.5_LTS
        julia/1.1.1
        julia/1.4.2
        julia/1.6.1
        julia/1.6.3 
        julia/1.6.7_LTS 
        julia/1.7.2 
        julia/1.8.5
        julia/1.9.1 
        julia/1.9.3 (Default)

           

"LTS" stands for Long term support.

To load a specific version of Julia into your environment, just type e.g.

        $ module load julia/1.6.7_LTS

​Doing:

        $ module load julia

will give you the default version (1.9.3), often the latest version.

A good and important suggestion is that you always specify a certain version. This is to be able to reproduce your work, a very important key in research!

You can run a julia script in the shell by:

        $ julia example_script.jl

After loading the appropriate modules for Julia, you will have access to the read-eval-print-loop (REPL) command line by typing julia.

        $ julia

You will get a prompt like this:

julia> 

Julia has different modes, the one mentioned above is the so-called Julian mode where one can execute commands. The description for accessing these modes will be given in the following paragraphs. Once you are done with your work in any of the modes, you can return to the Julian mode by pressing the backspace key.

While being on the Julian mode you can enter the shell mode by typing ;:

julia>;
shell>pwd
/current-folder-path

This will allow you to use Linux commands. Notice that the availabilty of these commands depend on the OS, for instance, on Windows it will depend on the terminal that you have installed and if it is visible to the Julia installation.

Another mode available in Julia is the package manager mode, it can be accessed by typing ] in the Julian mode:

julia>]
(v1.8) pkg>

This will make your interaction with the package manager Pkg easier, for instance, instead of typing the complete name of Pkg commands such as Pkg.status() in the Julian mode, you can just type status in the package mode.

The last mode is the help mode, you can enter this mode from the Julian one by typing ?, then you may type some string from which you need more information:

help?> ans

julia>?
search: ans transpose transcode contains expanduser instances MathConstants readlines LinearIndices leading_ones leading_zeros
ans
A variable referring to the last computed value, automatically set at the interactive promp

Backspace will get you back to julian mode

​Exit with <Ctrl-D> or 'exit()'. 

More detailed information about the modes in Julia can be found here: https://docs.julialang.org/en/v1/stdlib/REPL/
