# Dataset Information

## Source
The system uses datasets adapted from:
- [VirusTotal](https://www.virustotal.com/)
- [ClamAV](https://www.clamav.net/)
- Public malware repositories like VirusShare and Kaggle datasets.

## Features Extracted
- File size, entropy, string frequency, opcode sequences
- MD5/SHA-256 hash
- API call traces (if available)
- Packed/Obfuscated indicators

## Labeling
- **Malicious**: Identified by known AV engines or verified in VirusTotal.
- **Benign**: Verified clean files from trusted sources.

## Format
The data will be stored in a `.csv` format for AI training and in SQLite for real-time querying.

