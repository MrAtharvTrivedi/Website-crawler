import requests
import re
from urllib.parse import urljoin

base_url = input("Enter the base url: ")
subdomain_wordlist = input("Enter the subdomain wordlist path: ")
directory_wordlist = input("Enter the directory wordlist path: ")
links_choice = input("Do you want to scrape all links (y/n): ")

visited_links = set()

def clear_files():
    files = [
        "Subdomains.txt",
        "Detected_endpoints.txt",
        "Found_links.txt"
    ]

    for file in files:
        open(file, "w").close()


# For sending request to a particular domain/subdomain
def send_request(subdomain, domain) :
    full_url = "https://"+subdomain+"."+domain

    try:
        requests.get(full_url, timeout=3)
        found_subdomains("Subdomains.txt", full_url)

    except Exception as e:
        pass


# Discovering endpoints for a particular subdomain
def discover_endpoint(path, directory) :
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            modified_url = line.strip() + "/" + directory

            try:
                requests.get(modified_url, timeout=3)
                found_endpoints("Detected_endpoints.txt", modified_url)

            except Exception as e:
                pass

# Accessing subdomain directory
def get_wordlist_sub(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            send_request(line.strip(), base_url)

# Accessing endpoint directory
def get_wordlist_dir(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            discover_endpoint("Subdomains.txt", line.strip())

# Writing found subdomains to a file
def found_subdomains(path, full_url):
    with open(path, 'a') as f:
        f.write(full_url + "\n")

# Writing found endpoints/paths to a file
def found_endpoints(path, full_url):
    with open(path, 'a') as f:
        f.write(full_url + "\n")

# Writing found links to a file
def found_links(path, link):
    with open(path, 'a') as f:
        f.write(link + "\n")



def website_crawler(target_url):

    unique_links = []

    if target_url in visited_links:
        return
    
    visited_links.add(target_url)

    try:
        response = requests.get(target_url, timeout=3)
        href_links = re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))
        for link in href_links:

            # Converting relative links to full links
            link = urljoin(target_url, link)

            # is used to refer to elements within the same page
            if "#" in link:
                link = link.split("#")[0]

            if (target_url in link) and (link not in unique_links):
                unique_links.append(link)
                website_crawler(link)


        for link in unique_links:
            found_links("Found_links.txt", link)

    except Exception as e:
        pass


# Clearing all the data in the files
clear_files()

# Accessing subdomain wordlist
get_wordlist_sub(subdomain_wordlist)

# Accessing endpoints wordlist
get_wordlist_dir(directory_wordlist)

if links_choice == 'y':
    with open("Subdomains.txt", 'r') as f:
        links = f.readlines()
        for link in links:
            website_crawler(link.strip())

print("The program ran successfully")
print("[+] Subdomains.txt created")
print("[+] Detected_endpoints.txt created")
if links_choice == 'y':
    print("[+] Found_Links.txt created")

