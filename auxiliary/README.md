# RENDER

libraries inside render module uses which PyQt5 doesn't have a Python 3.12 support so it is recommended to have Python 3.11 or 3.10 venv to run the following animate.py function otherwise compatability error ( AI fix this use the right name of the error) raises.

(AI add code for venv setup and requirements too)

Also most of the files in the SPICE kernel is in .bds format, and while using animate function using .bds directly may pop an error it's recommended in that case to use SPICE toolkit name 'dskexp' to convert the file to .obj save it locally then render it.

example command
dskexp -dsk didymos_g_04657mm_spc_0000n00000_v003.bds -text didymos_g_04657mm_spc_0000n00000_v003.obj -format obj -p
ec 10

on running the command will give you an rendered image and cancelling it will redirect to .gif which will be saved in the desired path.

