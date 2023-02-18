# This is the main file for the Password Generator and Storage Program.

# Import main modules
import sys

sys.path.insert(0, 'res')
sys.path.insert(0, 'bin')

# Import app modules
from res import f


#Log the startup
f.LogStartUp()

# Check if the modules work or not.

# 0n the launch, we will check if the application was already launched or not by viewing our data fileset.
# TODO: Install the res folder along with the files, and empty bin folder

if(not f.checkFileExists("bin/gp.txt")):
    f.Log("This is the first launch.","mainFile")
    from res import s
    s.showWindow()
else:
    f.Log("Data found","mainFile")
    from res import m
    m.showWindow()
