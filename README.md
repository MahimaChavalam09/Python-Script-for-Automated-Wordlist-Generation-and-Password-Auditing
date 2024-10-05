# Python-Script-for-Automated-Wordlist-Generation-and-Password-Auditing

Automated Wordlist Generation and Password Auditing
This project automates the process of generating wordlists using Crunch and performing password auditing using Hydra. It is designed for security auditing and penetration testing to identify weak passwords on a target system.

Disclaimer: This tool should only be used on systems that you own or have explicit permission to test. Unauthorized use of these tools is illegal and unethical.

Features
Generates custom wordlists based on specific parameters (length, character set).
Automates password brute-forcing for services like FTP, SSH, and others using Hydra.
Stores audit results in a log file for review.
Installation: 
Requirements- 
Kali Linux with:

           Crunch: Pre-installed in Kali Linux for wordlist generation.
           Hydra: Pre-installed in Kali Linux for brute-force attacks.
           Python 3.x: To run the automation script.

      Parameters 
      
-- min_length: Minimum length of passwords to generate.

--max_length: Maximum length of passwords to generate.

--charset: The character set to use for wordlist generation (e.g., abc123).

--service: The service to attack (e.g., ftp, ssh).

--ip_address: IP address of the target machine.

--username: The username for login attempts.

Output :
Generated wordlists are saved in the specified output file (default: wordlist.txt).

Audit results (success, failures, and logs) are stored in audit_log.txt.
