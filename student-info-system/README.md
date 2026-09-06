# Student Info System

A command-line student information system built as part of my Python mini-projects collection. Unlike `student-registration-system` (a text-file based CRUD project), this one is built around a dictionary-based data structure, with each student's number as the key and their details (name, surname, grades) stored as a nested dictionary.

## Features

- **Add student** — register a new student with a unique student number
- **Add grade** — add a grade to an existing student's grade list
- **Show average** — calculate and display a student's grade average
- **List records** — display all registered students and their grades
- **Search record** — look up a single student by number
- **Update record** — edit a student's name/surname
- **Delete record** — remove a student from the system
- **Exit**

## In progress

- **Calculate letter grade** — convert a student's average into a letter grade (not yet implemented)

## How it works

- All data is stored in memory in a single dictionary (`ogrenciler`), keyed by student number. No file storage or database is used — data resets each time the program runs.
- Each student record is a nested dictionary holding name, surname, student number, and a list of grades.
- The program runs as a loop showing a numbered menu; the user picks an option to trigger the corresponding function.
- Input validation (`try`/`except`) guards against non-numeric input for student numbers and grades.

## Tech

Pure Python — no external libraries. Uses dictionaries, lists, functions, and basic exception handling.

## Run

```bash
python3 student-info-system.py
```