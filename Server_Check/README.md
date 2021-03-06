# server_check.py #
### Short Description: ###
It will check to see if a server is up or not on either port 80 or 443 through an IPv4 socket.
<br><br>

### Attribution: ###
Project is based off a script under the GNU GPL v3.0 license written by FreeCodeCamp contributor Hillary Nyakundi:
*https://github.com/larymak/Python-project-Scripts/blob/main/ServerChecker/*

**Thank you for making this available**.
<br>
This was fun. :)

#### Changes made: ####
- Added comments.
- Added main function.
- Added validator while loops to check responses.
- Added exit() function to approprate lines.
- Added and changed some variables.
<br>

### Purpose: ###
The script will check for a response from the website and port given by user input.
- Reports based off the returned value of True or False from the checking function. 
- It will ask for more input to continue checking another website. 
- If not, will exit the program.

#### Execution Steps: ####
1. Download this file or fork the repository.
2. Run the server_check.py file from it's location path in the filesystem.
3. Correctly enter only the IP address or hostname (domainname.tld i.e.:(cisco.com))
4. Answer yes or no to HTTPS check.
    - If yes, it check port 443 of the server.
    - If no, it checks port 80 of the server.
    - If else, you'll be scolded by the program and asked again.
5. Answer yes or no to another website check.
    - If yes, it continues the program from the beginning
    - If no, it exits the program
    - If else, you'll be scolded by the program and asked again. 
