# Selenium Python Automation Framework

A scalable UI test automation framework built with Selenium WebDriver, 
Python, and PyTest using the Page Object Model (POM) design pattern.

## Features
- Page Object Model (POM) architecture
- Reusable BasePage with explicit waits
- Config-driven test data (config.ini)
- HTML test reports via pytest-html
- Headless execution support
- Screenshot capture on failure

## Tech Stack
- Python 3.x
- Selenium WebDriver
- PyTest
- pytest-html
- WebDriver Manager (auto chromedriver)

## Project Structure
\```
selenium-python-automation-framework/
├── pageObjects/      # Page classes (BasePage, LoginPage, ...)
├── testCases/        # Test scripts
├── utilities/        # Config reader and helpers
├── testData/         # config.ini
├── conftest.py       # Fixtures (driver setup/teardown)
├── pytest.ini        # PyTest configuration
└── requirements.txt
\```

## How to Run

### Install dependencies
\```bash
pip install -r requirements.txt
\```

### Run all tests
\```bash
pytest
\```

### Run with HTML report
\```bash
pytest --html=reports/report.html --self-contained-html
\```

## Sample Report
![Report Screenshot](screenshots/sample_report.png)