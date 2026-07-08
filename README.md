# Mission Support Management System Equipment Inventory CLI

I started a Python learning project called Mission Support Management System.

It is a command-line equipment inventory tracker where I'm practicing core programming fundamentals: functions, input validation, records, menus, and Git/GitHub workflow.

I'm using this repo to document my progress over time as I keep building toward software roles in mission-focused environments.

## How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository or download the project files.
3. Open a terminal in the project folder.
4. Run the program with:

```bash
python msms.py
```

## Current Features

Right now it supports:

- Adding equipment records with an ID, name, category, status, and location.
- Listing all inventory records from the current session.
- Searching for equipment by ID.
- Validating equipment status against approved options.

## Current Limitations

- Equipment records are only stored during the current program session.
- The program does not currently support editing or deleting records.
- There are no automated tests yet.

## Next Steps

This project is being built over time as I continue learning Python and software development fundamentals.

Planned improvements:

- Add persistent storage so equipment records are saved after the program closes.
- Add options to edit and delete existing equipment records.
- Replace list-based equipment records with dictionaries or classes for cleaner data handling.
- Add automated tests for the main program functions.
- Improve command-line formatting so inventory records are easier to read.
- Continue documenting each major improvement through Git commits.

