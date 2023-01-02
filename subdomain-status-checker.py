import time
import requests

file_name = input("Enter the name of the file with the URLs: ")

with open(file_name, "r") as f:
    for url in f:
        url = url.strip()
        try:
            r = requests.get(url)
            if r.status_code == 200:
                message = f"{url} is returning a 200 status."
            elif r.status_code == 404:
                message = f"{url} is returning a 404 status."
            elif r.status_code == 500:
                message = f"{url} is returning a 500 status."
            elif r.status_code == 502:
                message = f"{url} is returning a 502 status."
            elif r.status_code == 503:
                message = f"{url} is returning a 503 status."
            elif r.status_code == 504:
                message = f"{url} is returning a 504 status."
            else:
                message = f"{url} is experiencing a connection timeout, SSL certificate error, redirect loop, slow loading, or broken links."
        except Exception as e:
            message = f"An error occurred while checking {url}: {e}"
        with open("status.txt", "a") as f:
            f.write(message + "\n")
        time.sleep(5)
