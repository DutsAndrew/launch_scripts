# closes all running applications

import os

script = 'tell application "System Events" to set the visible of every process whose visible is true and name is not "Finder" to false\n' \
         'tell application "System Events" to set the procs to every process whose background only is false and name is not "Finder"\n' \
         'repeat with proc in procs\n' \
         '   try\n' \
         '       tell proc to quit\n' \
         '   end try\n' \
         'end repeat'

os.system(f"osascript -e '{script}'")