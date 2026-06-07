# Website Crawler

A Python-based web reconnaissance tool that performs subdomain discovery, directory enumeration, and recursive website crawling to identify accessible endpoints and internal links.

## Features

* Subdomain discovery using custom wordlists
* Directory and endpoint enumeration
* Recursive website crawling
* Internal link extraction
* Relative URL handling using `urljoin`
* Automatic result storage in text files
* Configurable wordlists
* Request timeout handling

---

## How It Works

The tool performs three main tasks:

### 1. Subdomain Discovery

The program reads subdomains from a user-provided wordlist and attempts to construct valid URLs.

Example:

```text
admin
mail
blog
api
```

For a target domain:

```text
example.com
```

The tool generates:

```text
https://admin.example.com
https://mail.example.com
https://blog.example.com
https://api.example.com
```

Discovered subdomains are stored in:

```text
Subdomains.txt
```

---

### 2. Directory Enumeration

For every discovered subdomain, the tool attempts to discover accessible endpoints using a directory wordlist.

Example:

```text
login
admin
dashboard
uploads
```

Generated URLs:

```text
https://admin.example.com/login
https://admin.example.com/admin
https://admin.example.com/dashboard
```

Discovered endpoints are stored in:

```text
Detected_endpoints.txt
```

---

### 3. Website Crawling

The crawler recursively visits discovered pages and extracts links from HTML content.

Features:

* Converts relative links to absolute URLs
* Removes URL fragments (#)
* Avoids revisiting previously crawled pages
* Stores discovered links

Results are written to:

```text
Found_links.txt
```

---

## Project Structure

```text
website-crawler/
│
├── website_crawler.py
├── README.md
│
├── Subdomains.txt
├── Detected_endpoints.txt
└── Found_links.txt
```

---

## Requirements

Python 3.8+

Install dependencies:

```bash
pip install requests
```

---

## Usage

Run:

```bash
python website_crawler.py
```

The program will prompt for:

```text
Enter the base url:
Enter the subdomain wordlist path:
Enter the directory wordlist path:
Do you want to scrape all links (y/n):
```

Example:

```text
Enter the base url: example.com
Enter the subdomain wordlist path: subdomains.txt
Enter the directory wordlist path: directories.txt
Do you want to scrape all links (y/n): y
```

---

## Output Files

### Subdomains.txt

Contains discovered subdomains.

Example:

```text
https://admin.example.com
https://blog.example.com
```

### Detected_endpoints.txt

Contains discovered endpoints.

Example:

```text
https://admin.example.com/login
https://blog.example.com/dashboard
```

### Found_links.txt

Contains links discovered during crawling.

Example:

```text
https://example.com/about
https://example.com/contact
https://example.com/blog
```

---

## Technologies Used

* Python
* Requests
* Regular Expressions (re)
* urllib.parse

---

## Learning Objectives

This project was created to practice:

* HTTP requests
* Web reconnaissance concepts
* File handling
* Recursive crawling
* URL parsing and manipulation
* Working with wordlists
* Python project organization

---

## Limitations

Current limitations include:

* Uses regular expressions instead of an HTML parser
* Does not execute JavaScript
* Crawls only links visible in HTML source
* No multithreading support
* No rate limiting
* No status code validation

These improvements are planned for future versions.

---

## Future Improvements

* Multithreaded scanning
* Status code filtering
* HTML parsing with BeautifulSoup
* Domain validation using `urlparse`
* Export results to CSV/JSON
* Colored terminal output
* Better exception handling
* Progress indicators

---

## Disclaimer

This project was developed for educational purposes and authorized security testing only. Always obtain permission before scanning or testing systems that you do not own.
