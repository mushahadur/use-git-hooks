# Instructions to start

This repository uses manual **Git Pre-commit Hooks** combined with **Black** and **Flake8** to enforce code formatting and quality control before any code is committed.

---

## STEPS:

### Step 1: Create the Hook File
Navigate to the hidden `.git/hooks` directory of your cloned repository and create a file named `pre-commit`:

```bash
cd .git/hooks
touch pre-commit
```

### Step 2: Add the Automation Script
Open the newly created `pre-commit` file and paste the shell script inside it to trigger validation during `git commit`. I provided this file.

### Step 3: Make the Script Executable
By default, Git ignores hook scripts unless they have execution permissions. Run the following command inside the `.git/hooks` directory to make it executable safely:

```bash
chmod +x pre-commit
```
or
```bash
chmod 777 pre-commit
```
---

### Step 3: Install the black Python package:

```bash
pip3 install black
```

---

### Step 4: Test code file to show formatting errors:
```bash
python3 -m black --check app.py
```

---


### Step 5: Solve this file:
```bash
python3 -m black app.py
```
