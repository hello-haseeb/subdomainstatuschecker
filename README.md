# subdomainstatuschecker
a Bash and Python Script to check the status of domains like 200 404 or 503 


This is a bash script that checks the status of URLs in a file and writes the results to a file called "status.txt". The user is prompted to enter the name of the file that contains the URLs. The script checks the status of each URL using curl, and writes a message to the "status.txt" file indicating whether the URL is returning a 200 status, a 404 status, or is experiencing some other error. The script also has a sleep function that waits 5 seconds between checks to allow for a slower, more verbose output.


The given script is used to check the status of the URLs listed in a file. It reads each URL from the file, makes a GET request to the URL using the Python requests library, and checks the status code of the response. If the status code is one of the following: 200, 404, 500, 502, 503, or 504, a message is generated and written to a file called "status.txt". If the status code is not one of these values, a message indicating that the URL is experiencing a connection timeout, SSL certificate error, redirect loop, slow loading, or broken links is generated and written to the file.

To use this script, you will need to have Python 3 and the requests library installed. You will also need to provide the name of the file containing the list of URLs as input when running the script. The script will pause for 5 seconds before making the next request, to avoid overloading the server with requests.

Please note that this script is provided for educational and informational purposes only. It is your responsibility to ensure that you have permission to access the URLs and that you are using the script in a legal and ethical manner.
