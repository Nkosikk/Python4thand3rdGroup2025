# Python Selenium Automation Project - Ndosi

This project is a Selenium-based automation framework using Python and Pytest, following the Page Object Model (POM) design pattern.

## Project Structure
The project is organized into several directories:

- **Basics/**: Basic Python practice scripts.
- **Configurations/**: Configuration files, such as `data.ini` for managing test data and environment settings.
- **Pages/**: Contains Page Object classes representing different pages of the application (e.g., `loginPage.py`, `homePage.py`).
- **tests/**: Contains test scripts and `conftest.py` for shared fixtures and setup.
- **utils/**: Utility modules for browser setup, common actions, and reading configuration files.
- **allure-results/**: Stores test execution results for Allure reporting.

## Recommended Software Requirements
* Python 3.x
* PyCharm (or any preferred IDE)
* pip (Python package installer)

## Dependencies Required
* `selenium`: For web browser automation.
* `pytest`: For running tests.
* `allure-pytest`: For generating detailed test reports.

## Installation of Dependencies
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install the required packages (create a requirements.txt if needed, otherwise install manually):
   ```bash
   pip install selenium pytest allure-pytest
   ```

## How to execute tests
To run the tests and generate Allure results, use the following command:

```bash
pytest -s -v -m "dev" --alluredir="allure-results" --browser chrome
```

To view the Allure report:
```bash
allure serve allure-results
```
