# INET4031 Add Users Script and User List

## Program Description

This script helps add multiple users and assign them to groups on a Linux system automatically. Instead of typing commands for each user, the script reads a file and runs the necessary commands to create users, set their passwords, and add them to groups.

Normally a system administrator would do this manually like this:
sudo adduser username  
sudo passwd username  
sudo adduser username groupname 
This script does the same thing but much faster and with fewer mistakes.

## Program User Operation

This next section will explain how to use the script! Basically the script processes an input file containing user details and executes system commands based on it.

### Input File Format
Each line in the input file represents a user and follows this format:
username:password:last_name:first_name:group1,group2

Field Breakdown:
username - The system login name.
password - The user's password.
last_name - User's last name.
first_name - User's first name.

group1,group2 - Groups the user should be added to.
To skip a line, start it with #.
To add a user without any groups, use - in the groups field.

Example input:
user01:password123:Doe:John:group1,group2
user02:password123:Smith:Jane:-

### Command Excuction

To run the script, first make sure that it has execute permissions by doing: chmod +x create-users.py
Then execute it with: sudo ./create-users.py < create-users.input

### "Dry Run"
Before making actual changes, you can test the script in "dry run" mode.
This means the script will only print the commands instead of executing them.

To do a dry run, comment out the os.system(cmd) lines in the script and run:

./create-users.py < create-users.input
This helps check if everything is correct before making real changes.
