import os;
import time;

time_threshold = 315360000; # One year in seconds
applications_directory = os.path.expanduser("~/Applications");
current_time = time.time();

unused_apps = [];

# Loop through all files in app dir
for filename in os.listdir(applications_directory):
    # Get full path of the application
    application_path = os.path.join(applications_directory, filename);
    if os.path.isfile(application_path) and application_path.endswith(".app"):
        last_accessed_time = os.path.getatime(application_path)
        # Check if it's been a year since use
        if current_time - last_accessed_time > time_threshold:
            # Uninstall app
            os.system("sudo rm -rf '{}'".format(application_path));
            unused_apps.append(filename);

print("Unused apps:");
for app in unused_apps:
    print(app);