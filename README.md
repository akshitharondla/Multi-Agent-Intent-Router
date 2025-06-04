# Multi-Agent AI System

This project demonstrates a multi-agent AI system with a Classifier Agent, JSON Agent, Email Agent, and a Shared Memory module.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run main script: `python main.py`

## Agents
- **Classifier Agent**: Detects format and intent.
- **JSON Agent**: Parses and validates structured JSON.
- **Email Agent**: Extracts sender, urgency, and details from email text.

## Memory
Uses Redis or SQLite to track conversations and extracted data.

## Sample Inputs
Check the `samples/` folder for example input files.

## Outputs
Logged in `logs/` folder.
