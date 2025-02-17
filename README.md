# Xelera-Parser

A set of tools for extracting information from a Xelera ransomware executable.

> **Note:** Xelera ransomware is unlikely to become widespread. It appears to be a one-off solution, and its code quality is notably poor.  
> Read more: [Seqrite Blog - Xelera Ransomware](https://www.seqrite.com/blog/xelera-ransomware-fake-fci-job-offers/)

## 📂 Repository Contents

- **`decrypt_notoken887.py`** – Decrypts encrypted `notoken887` output from `final.pyc`.
- **`get_crypto_address.py`** – Extracts the Litecoin address from `imports.pyc`.
- **`get_bot_token.py`** – Retrieves the Discord bot token from `imports.pyc`.
- **`main.py`** – Retrieves bot token and Litecoin address from Xelera executable.

## Usage
- Run desired script and follow instructions in terminal.

## Credits
- [pyinstxractor-ng](https://github.com/pyinstxtractor/pyinstxtractor-ng) for extracting the contents of a PyInstaller executable.
---

For research and educational purposes only. Use responsibly.
