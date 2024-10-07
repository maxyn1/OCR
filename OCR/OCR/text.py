import hashlib
from itertools import product

# Define the target hash
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # MD5 hash of "password"

# Generate character combinations
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
max_length = 8

# Brute-force attack
for length in range(1, max_length + 1):
    for combination in product(characters, repeat=length):
        guess = "".join(combination)
        hash_guess = hashlib.md5(guess.encode()).hexdigest()
        if hash_guess == target_hash:
            print(f"Password found: {guess}")
            break