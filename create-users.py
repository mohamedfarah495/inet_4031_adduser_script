#!/usr/bin/python3

# INET4031
# Mohamed Farah
# Date Created: 3/22/2025
# Date Last Modified: 3/24/2025

#os is used to execute Linux commands, re is used for regular expressions to match patterns in text, and sys is used to handle system input (stdin)
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        #After the above line reads each line, this line will check if the line starts with '#' which indicates that it's a comment and ignore it 
        match = re.match("^#",line)

        #Splits the line using ':' as a delimiter to extract user datails
        fields = line.strip().split(':')

        #Skips the line if it's a comment or if it doesn't have 5 fields
        if match or len(fields) != 5:
            continue

        #These 3 lines get the user details from the input file
        username = fields[0] #the username being created
        password = fields[1] #the user's password
        gecos = "%s %s,,," % (fields[3],fields[2]) #Full name format for /etc/passwd

        #This line extracts groups the user should be added to (split by ',')
        groups = fields[4].split(',')

        #Displays message indicating user account creation
        print("==> Creating account for %s..." % (username))
        #the cmd variable creates a new user without setting a password immediately
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #It has to be commented out the first time because of the dry run, if uncommented, this line will execute the command to create the users
        #print cmd
        os.system(cmd)

        #Displays message indicating password assignment
        print("==> Setting the password for %s..." % (username))
        #cmd is a Linux command and it helps set the user's password securely
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #It has to be commented out the first time to do the dry run, if uncommented and the code doesn't run properly, it will execute the password setting command
        #print cmd
        os.system(cmd)

        for group in groups:
            #the if group != '-' statement checks if the user has a valid group and if that's true, the user is added to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
