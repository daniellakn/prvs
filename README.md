# Python Requirements Vulnerabilty Scanner (PRVS)

PRVS is a command-line utility that scans for vulnerabilties in Python packages that are included in a requirements.txt (or specified name), and provides a summary, suggested upgrade, and version information about each package. 

Use the `-v`/`--verbose` switch to see vulnerability details.

Use the `-p`/`--path` switch to set the location and name of the requirements file, if it is not in the current directory, or if it not named 'requirements.txt'.

## Example Usage

```
$ python3 src/prvs.py -p test/requirements.txt 

Package found: beautifulsoup4==4.11.2
No known vulnerabilities
>>> You are using an outdated version. Latest is 4.12.3.


Package found: pillow==10.1.0
This package has 3 vulnerabilities.
>>> You are using an outdated version. Latest is 10.4.0.
>>> Consider upgrading to version 10.3.0 to resolve all known vulnerabilities.

>>> 3 vulnerabilties found across 2 vulnerable packages.
```

```
$ python3 src/prvs.py -p test/requirements.txt -v

Package found: beautifulsoup4==4.11.2
No known vulnerabilities
>>> You are using an outdated version. Latest is 4.12.3.


Package found: pillow==10.1.0
Vulnerabilties:
        Vulnerability ID: CVE-2024-28219
        Summary: Summary cannot be provided.
        Fixed in version: No fix avaiable.

Vulnerabilties:
        Vulnerability ID: BIT-pillow-2023-50447
        Summary: Arbitrary Code Execution in Pillow
        Fixed in version: 10.2.0

Vulnerabilties:
        Vulnerability ID: BIT-pillow-2024-28219
        Summary: Pillow buffer overflow vulnerability
        Fixed in version: 10.3.0

This package has 3 vulnerabilities.
>>> You are using an outdated version. Latest is 10.4.0.
>>> Consider upgrading to version 10.3.0 to resolve all known vulnerabilities.

>>> 3 vulnerabilties found across 2 vulnerable packages.
```
