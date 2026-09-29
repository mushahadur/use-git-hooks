# My Python Project 

This project just uses **Git Hooks** to maintain code quality and formatting.

## Setup Git Hooks Locally

Before making any commits, please set up the automated pre-commit hooks:

1. Install the pre-commit package:
   ```bash
   pip install pre-commit
   ```

2. Install the git hook scripts:
   ```bash
   pre-commit install
   ```

Now, every time you run `git commit`, your Python code will be automatically checked for formatting (`black`) and style rules (`flake8`).
