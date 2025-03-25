#!/usr/bin/python3

# INET4031
# Mohamed Farah
# Date Created: 3/22/2025
# Date Last Modified: 3/25/2025

import os  # Used to run system commands
import re  # Used for matching patterns in text (like detecting comments)
import sys  # Used for system input/output handling

# Ask the user if they want to do a dry-run before reading the input file
dry_run_input = input("Would you like to run in dry-run mode? (Y/N): ").strip().lower()
dry_run = dry_run_input == 'y'  # If user types 'Y', dry-run mode is activated

# Let the user know which mode is running
if dry_run:
    print("\nDry-run mode activated. No changes will be made.\n")
else:
    print("\nRunning in normal mode. Users and groups will be created.\n")

def main():
    # Open and read the input file
    with open("create-users.input", "r") as file:
        for line in file:
            # Check if the line is a comment (starts with #)
            match = re.match("^#", line)
            # Split the line using ":" to get user details
            fields = line.strip().split(':')

            # If the line is a comment or does not have exactly 5 fields, handle it accordingly
            if match or len(fields) != 5:
                if dry_run:
                    print(f"Skipping invalid or commented line: {line.strip()}")
                continue  # Skip this line and move to the next

            # Extract user details from the fields
            username = fields[0]  # The username for the new account
            password = fields[1]  # The user's password
            gecos = "%s %s,,," % (fields[3], fields[2])  # User's full name format for Linux systems
            groups = fields[4].split(',')  # List of groups the user should be added to

            # Print message indicating account creation
            print(f"==> Creating account for {username}...")

            # Command to create a new user without setting a password immediately
            cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

            if dry_run:
                print(f"Dry-run: Would execute -> {cmd}")  # Show the command that would run
            else:
                os.system(cmd)  # Run the command if not in dry-run mode

            # Print message for setting user password
            print(f"==> Setting the password for {username}...")

            # Command to set the password securely
            cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

            if dry_run:
                print(f"Dry-run: Would execute -> {cmd}")  # Show the command that would run
            else:
                os.system(cmd)  # Run the command if not in dry-run mode

            # Loop through each group and add the user to it
            for group in groups:
                if group != '-':  # If the user has valid groups, add them
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd = f"/usr/sbin/adduser {username} {group}"

                    if dry_run:
                        print(f"Dry-run: Would execute -> {cmd}")  # Show the command that would run
                    else:
                        os.system(cmd)  # Run the command if not in dry-run mode

if __name__ == '__main__':
    main()

