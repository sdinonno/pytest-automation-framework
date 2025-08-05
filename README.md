# pytest-automation-framework

This repository provides an automation framework for testing with [pytest](https://pytest.org/) and includes example tests for the [automationexercise.com API](https://automationexercise.com/api/).

## Prerequisites

- **Python 3.7 or higher**  
  Download the latest version from [Python.org](https://www.python.org/downloads/).
- **Git**  
  Optional, for cloning this repository locally. Download it from [git-scm.com](https://git-scm.com/).
- **Recommended code editor:**  
  - [PyCharm](https://www.jetbrains.com/pycharm/)
  - [Visual Studio Code](https://code.visualstudio.com/)

> It is recommended to have basic Python knowledge before working on this project.

## Installation

1. **Clone this repository**  
   ```bash
   git clone https://github.com/sdinonno/pytest-automation-framework.git
   cd pytest-automation-framework
   ```

2. **Install dependencies**  
   Using a virtual environment is recommended but optional for this project.

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   If you have multiple Python installations, use `python3` and `pip3` instead.

3. **Verify your Python installation**  
   ```bash
   python --version
   ```
   If this fails, try:
   ```bash
   python3 --version
   ```

## Running Tests

From the project root, run:

```bash
python -m pytest
```
or
```bash
pytest
```

This command will discover and execute all tests in the project.

## Project Structure

- `/tests` – Contains automated test cases.
- `/src` or `/framework` – (Optional) Source code for the automation framework.
- `requirements.txt` – List of project dependencies.
- `README.md` – This file.

## Notes on Virtual Environments

Although you can install packages globally, it is best practice to use virtual environments to avoid conflicts between projects. You can create one with:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

Then install the dependencies as described above.

## Useful Resources

- [pytest official documentation](https://docs.pytest.org/en/stable/)
- [RealPython: Python Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [API Automation with Python](https://automationexercise.com/api/)

---

Questions or suggestions? Open an issue or contact the maintainer.
