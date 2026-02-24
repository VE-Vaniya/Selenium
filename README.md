# Selenium Automation Project

## Overview
This project demonstrates **automated web application testing** using the **Selenium suite**, covering all three major components:  
- **Selenium IDE**
- **Selenium WebDriver** 
- **Selenium Grid** 

The objective is to apply **Software Quality Engineering (SQE)** principles and automate UI behavior testing of a web application.

## University Details
**University:** FAST National University of Computer and Emerging Sciences  
**Campus:** Lahore  
**Semester:** 5th Semester, BS Software Engineering  
**Course:** Software Quality Engineering  
**Instructor:** Dr. Ali Afzal Malik  

## Team Details
**Team Lead:** Vania Ejaz – [VE-Vaniya](https://github.com/VE-Vaniya) – 23L-3037

**Contributors:**
- **Muhammad Ahmad Butt** – [m-ahmad-butt](https://github.com/m-ahmad-butt) – 23L-3059  
- **Muhammad Amar Waqar** – [AmarWaqar-TSKLI](https://github.com/AmarWaqar-TSKLI) – 23L-3035  
- **Haseeb Ahmad** – [Haseebahmad22](https://github.com/Haseebahmad22) – 23L-3069  
- **Muhammad Zain Tahir** – [Zain485576](https://github.com/Zain485576) – 23L-3078  
- **Abdul Rafay** – [RAPHCRAP](https://github.com/RAPHCRAP) – 23L-3063

## Tech Stack
- **Language:** Python  
- **Frameworks & Tools:**  
  - Selenium IDE  
  - Selenium WebDriver  
  - Selenium Grid  
- **IDE:** PyCharm or Visual Studio Code  
- **Browser:** Mozilla Firefox  
- **Version Control:** Git & GitHub  

## Requirements

### Python
```bash
python --version
Python 3.13.7
````

📦 Download: [Python 3.13.7](https://www.python.org/downloads/release/python-3137/)

### Recommended Browser

* **Firefox** (latest version)
  Install Selenium IDE Add-on:
  🔗 [https://addons.mozilla.org/en-GB/firefox/addon/selenium-ide/](https://addons.mozilla.org/en-GB/firefox/addon/selenium-ide/)

## Project Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/VE-Vaniya/Selenium.git
```

## Automatic setup
It creates & activates venv, installs requirements.

- PowerShell:

```powershell
.\setup.ps1
```

- Command Prompt:

```cmd
setup.bat
```

## Manual setup

If you prefer to run steps manually, follow these minimal steps.

1) Create a virtual environment

```
python -m venv .venv
```

2) Activate the virtual environment

```
.venv\Scripts\activate.bat
```

3) Install dependencies

```
pip install -r requirements.txt
```

> 📝 Make sure all developers keep **requirements.txt** updated whenever new dependencies are added.
> This ensures that every team member can install all required libraries easily.

## Git & Collaboration Notes

* **Do NOT push the `venv/` folder** (it’s machine-specific).
* Always update `requirements.txt` after installing new packages:

  ```bash
  pip freeze > requirements.txt
  ```
* Before running the project, every developer should:

  ```bash
  pip install -r requirements.txt
  ```

© 2025 **Selenium Automation Project – FAST NUCES**
All rights reserved.
