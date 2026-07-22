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
- Preventing duplicate equipment IDs.
- Allows exporting the current inventory to a text report.
- Saving and loading equipment records with local JSON persistence.

## Current Limitations

- The program does not currently support editing or deleting records.
- There are no automated tests yet.
- Local JSON data and exported reports are not committed to the repository.

## Next Steps

This project is being built over time as I continue learning Python and software development fundamentals.

Planned improvements:

- Add options to edit and delete existing equipment records.
- Refactor equipment records into classes when object-oriented programming is introduced.
- Add automated tests for the main program functions.
- Improve command-line formatting so inventory records are easier to read.
- Continue documenting each major improvement through Git commits.

## Learning progress/Updates
- Refactored equipment records from list-based fields to dictionaries using named keys
- Added a feature to allow exporting of the current inventory into a local text report.
- Added basic JSON persistence so equipment records can be saved and loaded between sessions.
