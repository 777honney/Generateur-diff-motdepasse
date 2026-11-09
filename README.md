# Wordlist Generator

## Description
This Python script generates a file containing **every possible combination** of characters for a given password length. It uses the `itertools` module to produce these combinations exhaustively.

## How it works
1. The script asks the user for the desired password length.
2. It uses a character set made of lowercase letters (`a-z`) and digits (`0-9`), i.e. 36 possible characters.
3. Using `itertools.product`, it generates every possible combination of that length.
4. Each combination is written to a file named `ro.txt`, one per line.
5. A `"Document créé"` message confirms the script finished running.

## Example usage
```bash
python script.py
La longueur du mot de passe : 3
Document créé
```

This will generate every possible 3-character combination in `ro.txt` (this file name as to be change), for example:

<img width="523" height="443" alt="image" src="https://github.com/user-attachments/assets/7a592068-2259-4bde-920e-1d290d6440a3" />


## ⚠️ Warning: exponential growth
The number of combinations follows the formula `36^length`. It grows very fast:

| Length | Number of combinations | Approx. size |
|--------|--------------------------|---------------|
| 3      | 46,656                   | a few KB       |
| 4      | 1,679,616                | a few MB       |
| 5      | ~60 million              | several hundred MB |
| 6      | ~2.1 billion             | tens of GB     |

Beyond 5-6 characters, the script can fill up your disk and take a very long time to run.

## Requirements
- Python 3
- No external dependencies (only the standard library `itertools`)

## Intended use
This kind of generator is typically used for **educational purposes or password-strength testing** (e.g. measuring brute-force time against a system you own or are authorized to test). It must not be used to access accounts or systems without authorization.

## Possible improvements
-  Optimize the speed up disk writes.
- Automatically limit or warn if the requested length exceeds a reasonable threshold.
