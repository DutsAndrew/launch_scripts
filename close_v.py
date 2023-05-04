# closes all visible applications on the screen

import os;

script = 'tell application "System Events" to set the visible of every process whose visible is true and name is not "Finder" to false';

os.system(f"osascript -e '{script}'");