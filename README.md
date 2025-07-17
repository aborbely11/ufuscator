# ufuscator
🛡️ Ufuscator – Multi-encoding Obfuscation and Mutation Engine

Ufuscator is a powerful Python3 tool designed to obfuscate and mutate code or payloads for red teaming, penetration testing, WAF evasion, and secure testing environments.

It supports dozens of encoding, transformation, and evasion techniques to generate unique payloads from a single input — including combos and randomized mutations.
🚀 Features

    🔐 Encodings: Base64, Base16, Base32, Hex, URL, HTML Entities, JS Escape, ROT13, Unicode, UTF-8, XOR

    🧬 Transformations: Reversed, Odd-Even Swaps, Zero-width fake characters

    🎭 Language-specific outputs: Python chr(), JS string concatenation, SQL char()/nchar() style

    🧪 Technique combinations: Apply multiple obfuscation layers together

    🎲 Randomized mutations with flags --random, --combo, and --deep for fuzzing and evasion testing

    💣 CLI interface for fast usage in offensive and defensive scenarios

📦 Usage
python3 ufuscator.py "<your-payload-here>"

Optional mutation modes:
python3 ufuscator.py "<payload>" --random     # Apply 3 random techniques
python3 ufuscator.py "<payload>" --combo      # Generate 5 diverse mutations
python3 ufuscator.py "<payload>" --deep       # Generate 10 deep chained obfuscations

⚠️ Legal Notice

This tool is intended for educational and authorized testing purposes only. Unauthorized usage against systems without explicit permission is illegal and unethical.
