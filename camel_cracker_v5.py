"""
Name: Camel Cracker v5
Author: Benyad Cina, z5258384
Description: Supports brute force, dictionary and spidering attacks. Indicates the
             time taken to crack the inputed password.
Note: Github Copilot was enabled in the construction of this program. So some of
      the code may remain from Github Copilot in cleaning and formating.
"""

print("""
============================================
============== CAMEL CRACKER ===============      
============================================
======= BRUTE FORCE PASSWORD CRACKER =======      
============================================     

        ..  ..   / o._)                   .-
       /--'/--\  \-'||        .----.    .'  
      /        \_/ / |      .'      '..'    
    .'\  \__\  __.'.'     .'          i-._
      )\ |  )\ |      _.'
     // \\ // \\
    ||_  \\|_  \\_
    '--' '--'' '--'

============================================      
======== ASCII ART ARCHIVE by mrf ==========      
============================================      
""")

import itertools
import time
# import multiprocessing

def brute_force_guesser(max_length, target_password):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?'
    # chars = 'abcdefghijklmnopqrstuvwxyz'
    start_time = time.time()
    for password_length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=password_length):
            password = ''.join(guess)
            if password == target_password:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Elapsed Time: {elapsed_time:.10f} seconds")
                print(f"Password found: {password}")
                return password
    return None

def dictionary_guesser(target_password, wordlist):
    try:
        with open(wordlist, 'r') as f:
            start_time = time.time()
            found = False
            for line in f:
                password = line.strip('\n')
                if password == target_password:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Elapsed Time: {elapsed_time:.10f} seconds")
                    print(f"Password found: {password}")
                    found = True
                    break
            if not found:
                print("Password not found in the wordlist")
    except FileNotFoundError:
        print("Wordlist file not found.")

def spidering_guesser(target_password, wordlist):
    try:
        with open(wordlist, 'r') as f:
            start_time = time.time()
            found = False
            for line in f:
                password = line.strip('\n')
                if password == target_password:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Elapsed Time: {elapsed_time:.10f} seconds")
                    print(f"Password found: {password}")
                    found = True
                    break
            if not found:
                print("Password not found in the wordlist")
    except FileNotFoundError:
        print("Wordlist file not found.")

def main():
    max_length = int(input("Enter maximum password length: "))
    target_password = input("Enter target password: ")
    attack_option = input("Enter: 1 for brute force attack | 2 for dictionary attack | 3 for spidering attack: ")

    if attack_option == '1':
        guesser = brute_force_guesser(max_length, target_password)
    elif attack_option == '2':
        wordlist = input("Enter the wordlist file: ")
        guesser = dictionary_guesser(target_password, wordlist)
    elif attack_option == '3':
        wordlist = input("Enter the wordlist file: ")
        guesser = spidering_guesser(target_password, wordlist)
    else:
        print("Invalid attack_option")
        return

if __name__ == "__main__":
    main()
