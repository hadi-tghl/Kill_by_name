**Process Management Script**

This script (main.py) is a simple command-line tool for listing and terminating processes. It uses the myClass.py module to define a Process class, which is utilized to display information about running processes and terminate a specified process.

**Usage:**

  ./main.py [options] <process_id>
  
<process_id>: The process ID (PID) of the target process.

**Options:**

    -i, --info: Display more information about the specified process.
    
**Files**

main.py
This is the main script that provides functionality for listing and terminating processes. It takes a process ID as an argument and provides additional options for displaying more information about the process.
Usage Examples:
  ./main.py <process_id>
List processes with more information:
  ./main.py -i <process_id>
  
**Notes**

 Ensure that the script has executable permissions (chmod +x main.py) before running it.
 Use the script responsibly, especially when terminating processes (kill -9). Terminating processes abruptly can result in data loss or unexpected behavior.

 
