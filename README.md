![Python CI](https://github.com/cybertimm/Password-Auditor/actions/workflows/python.yml/badge.svg)

# Password Security Analyzer

A Python-based CLI tool that evaluates password strength and highlights security weaknesses.

## Features
- Entropy-based strength analysis
- Detection of common and predictable patterns
- Secure password reuse detection using hashing
- Breach checks using Have I Been Pwned (k-anonymity)

## Requirements
- Python 3.9+

## Installation
```bash
git clone https://github.com/cybertimm/Password-Auditor.git
cd Password-Auditor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

