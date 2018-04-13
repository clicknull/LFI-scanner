# LFI-scanner
LFI scanner tool made for PentestCloud.io tested on macOS and Debian using python 3.6 

![Screenshot](http://ea1c162fb17d2bd72dfc-e522253f68cdb460a44ea8b394ec57b5.r89.cf5.rackcdn.com/github/lfiscanner.png)

## Installation
> git clone https://github.com/PentestCloudLabs/LFI-scanner

> cd LFI-scanner

> pip3 install -r requirements.txt

> python3 LFIscanner.py --help

## Usage example:
> python3 LFIscanner.py -u http://10.0.8.105/dvwa/vulnerabilities/fi/?page=include.php --cookie="security=low; PHPSESSID=lsrhcih3fnktbu1nlad6flba34" -w -v

### Options

* (Required) -u URL, --url URL Target URL to scan, example http://localhost/index.php?page=about

* (Optional) -w, --windows         (optional) Use if server is windows
* (Optional) -v, --verbose         (optional) display every request
* (Optional)  -c COOKIE, --cookie COOKIE (optional) HTTP request cookie
