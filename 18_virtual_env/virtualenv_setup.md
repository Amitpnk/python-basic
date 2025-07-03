# 🐍 Python Virtual Environment Setup

This guide shows how to create and use a virtual environment to isolate dependencies for your Python projects.

## ✅ Why Use a Virtual Environment?

- Keeps project dependencies separate.
- Prevents conflicts between packages.
- Recommended for all Python projects.

## 🛠️ Step-by-Step Guide

### 1. Create a Virtual Environment

```bash
python -m venv venv
````

This will create a folder named `venv/` containing the virtual environment.

### 2. Activate the Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal prompt.

### 3. Install Packages (e.g. `requests`)

```bash
pip install requests
```

### 4. Freeze Requirements

```bash
pip freeze > requirements.txt
```

This saves the installed packages so others can replicate the environment.

### 5. Deactivate Environment

```bash
deactivate
```

## 🔁 Recreate Environment on Another Machine

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 📂 Directory Structure

```
your_project/
├── venv/
├── main.py
├── requirements.txt
└── ...
```

## 📌 Tips

* Never commit the `venv/` folder to version control (use `.gitignore`)
* Use a virtual environment for each project
