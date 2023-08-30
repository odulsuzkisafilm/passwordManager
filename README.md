# Password Manager GUI Program

This is a Python program that implements a simple password manager with a graphical user interface (GUI) using the Tkinter library. The program allows you to generate strong passwords and save website login credentials securely.

## Features

- Password Generation: Generates strong passwords with a combination of letters (both lowercase and uppercase), numbers, and symbols.
- Password Saving: Saves website login information (website URL, email/username, and password) in a JSON data file.
- Search Functionality: Allows you to search for and retrieve saved website login details.
- User-Friendly Interface: Provides a user-friendly GUI for easy interaction.

## Prerequisites

- Python 3.x installed on your system.
- The `tkinter`, `pyperclip`, and `json` libraries are used in this program.

## Usage

1. Launch the program.
2. Enter the website's URL, your email/username, and click the "Generate Password" button to generate a strong password.
3. Click the "Add" button to save the website login information.
4. Use the "Search" button to retrieve login details for a specific website.
5. The program will store the data in a JSON file named `data.json` in the same directory.
