# Camel Cracker v5

## Description

**Camel Cracker v5** is a basic password cracking tool that supports three types of attacks: brute force, dictionary, and spidering. It provides information about the time taken to crack a given password. This program is designed to demonstrate various password cracking techniques and their respective efficiency to different cases.

### Features

- **Brute Force Attack:** Generates and tests all possible combinations of characters up to a specified maximum length to find the target password.
- **Dictionary Attack:** Reads a wordlist file and tries to match the target password with words from the list.
- **Spidering Attack:** Similar to a dictionary attack but includes a tailored wordlist specific to target.

## Usage

1. Run the program using Python.
```bash
   python3 camel_cracker_v5.py
```
2. Select the type of attack you want to perform:
   - 1 for brute force attack
   - 2 for dictionary attack
   - 3 for spidering attack
4. Follow the on-screen prompts to input the necessary information:
   - Maximum password length (for brute force attack)
   - Target password
   - Wordlist file (for dictionary and spidering attacks)

The program will attempt to crack the password and display the results, including the time taken to find the password if successful.

## Analysis

Camel Cracker v5 uses a modular approach with separate functions for each type of attack. Here's how it works:

- **Brute Force Attack:** This attack generates all possible combinations of characters up to the specified maximum length and tests them one by one. The process is computationally intensive, especially for longer passwords, as it tries every possible combination until it succeeds. The program is however limited to single threaded operations at this stage of development.

- **Dictionary Attack:** In this attack, the program reads a wordlist file and compares each word to the target password. If there's a match, it reports success. This is faster than brute force for common passwords but relies on the quality of the wordlist.

- **Spidering Attack:** This attack is similar to the dictionary attack but is tailored to a specific target. It reads a wordlist file and matches the target password with the words from the list. It can be useful when the password format is unique.

### Learning Outcomes

While working on this project, I learned the following:

- Password cracking can be resource-intensive, especially for long and complex passwords.
- The importance of having a comprehensive wordlist for dictionary attacks.
- How to structure a Python program with separate functions for different tasks.
- Multiprocessing and multithreading. However I was unable to get it working for this current iteration.
- Handling file operations and user inputs.

## Author

- **Benyad Cina**
- Student ID: z5258384
- Course: 6441

### Note

This program was developed with the assistance of GitHub Copilot in regards to code cleaning and formating.

Due to the lack of multi-threading capabilities, the time taken to solve the password is not indicative of 
a strong password. Advanced password cracker utilise all CPU cores and thereby are able to crack passwords
significantly faster. Instead you this program as a guideline to see whether one inputted password is stronger
than another inputted password.

---

**Disclaimer:** This program should only be used for educational and ethical purposes. Unauthorized use for malicious intent is strictly prohibited.
