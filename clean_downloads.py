import os;
import time;
import send2trash;

DAYS_BEFORE_MOVE = 15;
current_time = time.time();

downloads_path = os.path.join(os.path.expanduser('-'), 'Downloads');

# Move old files to trash
for filename in os.listdir(downloads_path):
  file_path = os.path.join(downloads_path, filename);
  if os.path.isfile(file_path):
    file_time = os.path.getmtime(file_path);
    if current_time - file_time > DAYS_BEFORE_MOVE * 86400:
      send2trash.send2trash(file_path);