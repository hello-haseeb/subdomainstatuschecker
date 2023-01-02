# subdomainstatuschecker
a Bash and Python Script to check the status of domains like 200 404 or 503 


This is a bash script that checks the status of URLs in a file and writes the results to a file called "status.txt". The user is prompted to enter the name of the file that contains the URLs. The script checks the status of each URL using curl, and writes a message to the "status.txt" file indicating whether the URL is returning a 200 status, a 404 status, or is experiencing some other error. The script also has a sleep function that waits 5 seconds between checks to allow for a slower, more verbose output.
