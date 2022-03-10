#! /usr/bin/env python3
#! python3
#! python

# Project based off a script under the GNU GPL v3.0 license by Hillary Nyakundi:
# https://github.com/larymak/Python-project-Scripts/blob/main/ServerChecker/


# Start of the actual script.

# Importing socket module for connect method to pass a tuple of the socket method to check AF_INET for IPv4 addresses and SOCK_STREAM for open port used.
import socket

# Defining function to check URL connection status with address passed as the url variable as a parameter.
def up_check(url, port):
    # Function description text.
    '''This function will make connection attempts to the server address given using a socket
       Returns: Connection status to the server.'''
    # Try/except statement block to return status as True or False.
    try:
        # Assigning socket() method to shorter variable passing AF_INET and SOCK_STEAM for address and port check.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # calling connect() method and passing tuple of url variable and port 80.
        s.connect((url, port))
        # return True to to main function
        return True
    except:
        # If the try statement fails, then return False to the main function.
        return False

# Defining the main() function of the program.
def main():
    # Initiate continuous loops of programatic steps for URL check while True.
    while True:
        # Print the salutations and new line.
        print('\nWelcome to the World Wide Web site checker!\n.')
        # Ask user for web address input and assign to variable.
        url = input('Please enter the website: ')
        # Continuous loop to check if the answer for protocol query is incorrect.
        while True:
            # Ask user for HTTPS check.
            port = input('.\nDo you want to check HTTPS? ')
            # If no, assign port 80 and break protocol query loop.
            if port in {'n', 'N', 'no', 'No', 'NO'}:
                print('.\nChecking port 80 access...')
                port = 80
                prtcl = 'HTTP'
                break
            # If yes, assign port 443 and break protocol query loop
            elif port  in {'y', 'Y', 'yes', 'Yes', 'YES'}:
                port = 443
                prtcl = 'HTTPS'
                break
            # Annoy user for correct input and continue the protocol query loop until condition is met.
            else:
                print(".\nPlease answer correctly! Let's try again...\n")
                continue


        # Pass url and port variables as parameters to the up_check() function and check if it returns True.
        if up_check(f'{url}', int(port)):
            # Print the confirmation.
            print(f'.\n{url} is up and running on {prtcl} port {port}!\n.')
        # If the check returns False:
        else:
            # Print the failure.
            print(f'.\nThe website {url} seems to be down or unreachable on {prtcl} port {port}!\nAre you sure you typed that in correctly?\n.')

        # Another continuous loop to check if answer for another website query is correct.
        while True:
            # Ask the user if there is another address to check.
            con_quest = input(".\nIs there another website you'd like to check? ")
            # If no, print a farewell message and exit the script.
            if con_quest in {'n', 'N', 'no', 'No', 'NO'}:
                print('Have a nice day! :D\n')
                exit()
            # If yes, print restart message break from another website query and continue the primary loop.
            elif con_quest in {'y', 'Y', 'yes', 'Yes', 'YES'}:
                print("Alright! Let's start over...\n")
                break
            # Annoy user again for correct input and continue the loop until condition for another website query is met.
            else:
                print(".\nPlease answer correctly! Let's try again...\n.")
                continue


# Check if this is the main script by checking if the __name__ of the script is __main__.
if __name__ == '__main__':
    # If True, then call the main() function.
    main()

# Just in case, exit the environment back to the command line interface.
exit()
# End of Script. 
