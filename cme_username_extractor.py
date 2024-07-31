import subprocess
import re

# Prompt user for all input at the beginning
ip_address = input("Enter the target IP address: ")
username = input("Enter the username: ")
password = input("Enter the password: ")
output_file = input("Enter the name for the output file (e.g., usernames.txt): ")

# Construct the CrackMapExec command
cmd = f"crackmapexec smb {ip_address} -u {username} -p {password} --users"

# Run CrackMapExec and capture the output
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

# Check if the command was successful
if result.returncode != 0:
    print("Error running CrackMapExec. Output:")
    print(result.stderr)
    exit(1)

# Extract usernames from the output
usernames = re.findall(r'(?:INLANEFREIGHT\.LOCAL|WORKGROUP)\\(\w+)', result.stdout)

# Remove duplicates and sort
unique_usernames = sorted(set(usernames))

# Write usernames to the file
with open(output_file, 'w') as f:
    for username in unique_usernames:
        f.write(f"{username}\n")

print(f"\nOperation completed. {len(unique_usernames)} usernames have been saved to {output_file}")
