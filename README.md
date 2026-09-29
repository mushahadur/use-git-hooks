# Python Project with Automated Git Hooks 

This repository uses manual **Git Pre-commit Hooks** combined with **Black** and **Flake8** to enforce code formatting and quality control before any code is committed.

---

## 🛠️ Prerequisites

Before setting up the hooks, you need to install the required Python packages for linting and formatting. Run the following command in your terminal:

```bash
pip3 install flake8 black
```

---

## 🎣 Git Hook Setup Instructions

Follow these step-by-step instructions to activate the pre-commit hook on your local system:

### Step 1: Create the Hook File
Navigate to the hidden `.git/hooks` directory of your cloned repository and create a file named `pre-commit`:

```bash
cd .git/hooks
touch pre-commit
```

### Step 2: Add the Automation Script
Open the newly created `pre-commit` file in your favorite text editor and paste the shell script inside it to trigger validation during `git commit`.

### Step 3: Make the Script Executable
By default, Git ignores hook scripts unless they have execution permissions. Run the following command inside the `.git/hooks` directory to make it executable safely:

```bash
chmod +x pre-commit
```

---

## 🔍 Manual Code Quality Verification

If you want to manually test, check, or format your Python files (e.g., `app.py`) without triggering a git commit, you can use these commands:

### 1. Lint Code with Flake8
Check for syntax errors, unused imports, or style violations:
```bash
flake8 app.py
```

### 2. Format Dry-Run with Black
Check if the file requires formatting without actually modifying the code:
```bash
black --check app.py
```

### 3. Auto-Format with Black
Automatically format the file to match modern Python industry standards:
```bash
black app.py
```
