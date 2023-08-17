# Import the os module
import os

# Get the current script directory
script_dir = os.path.dirname(__file__)

# Define the names of the scripts to call
scripts = ["auto_file_prefix.py", "project_organizer.py"]

# Loop through the scripts and execute them
for script in scripts:
    # Join the script directory and the script name
    script_path = os.path.join(script_dir, script)
    # Open and read the script file
    with open(script_path, "r") as script_file:
        script_code = script_file.read()
    # Execute the script code
    exec(script_code)