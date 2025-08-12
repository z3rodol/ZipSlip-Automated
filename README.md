# ZipSlip-Automated
When I was doing HackTheBox's Certificate machine, I came across a website vulnerable to this attack. I wanted to do it manually. But I realized it wasn't that easy to do. That's where I came up with the idea for this little script to automate this attack.

# Usage

```python3 ZipSlip.py archive.zip shell.php 2```

<img width="1182" height="161" alt="image" src="https://github.com/user-attachments/assets/c94a162f-d2ea-4692-8395-708e8247fedb" />

# Help
usage: ZipSlip.py [-h] [--verbose] archive_name file_name levels

Zipslip Attack Automation Script

positional arguments:
- archive_name : Name of the archive to create
- file_name : Name of the file to include (Example revshell.php)
- levels : Number of levels (Exemple 2)

options:
- -h, --help : show this help message and exit
- --verbose, -v : Verbose mode
