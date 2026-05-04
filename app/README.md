# Factory.ai Test Automation — Python Calculator

This project shows how to wire up a Factory.ai Droid with custom skills
for automated test creation and execution.

## Project structure

```
factory-test-project/
├── app/
│   └── calculator.py          ← the Python app being tested
├── tests/
│   ├── test_calculator.py     ← pytest test cases
│   └── generate_test_report.py← report generator script
├── .factory/
│   ├── droids/
│   │   └── qa-droid.md        ← custom QA sub-droid
│   └── skills/
│       ├── test-creator/
│       │   └── SKILL.md       ← skill: generate test cases
│       ├── test-executor/
│       │   └── SKILL.md       ← skill: run tests & report results
│       └── test-report-generator/
│           └── SKILL.md       ← skill: create Excel test report
└── README.md
```

## Setup

1. Install Factory CLI:
   ```bash
   npm install -g @factory-ai/cli
   ```

2. Install Python dependencies:
   ```bash
   pip install pytest openpyxl
   ```

3. Authenticate with Factory:
   ```bash
   factory auth login
   ```

4. Start the Droid in your project root:
   ```bash
   factory
   ```

## Usage

### Create test cases for a module
Type in Factory chat:
```
/test-creator app/calculator.py
```
or just:
```
Create test cases for the calculator module
```

### Run all tests
```
/test-executor
```
or:
```
Run all tests and show me the results
```

### Generate Excel test report
```
/test-report-generator
```
or:
```
Generate the test report in Excel
```
This creates:
- `tests/calculator_junit_<YYYYMMDD_HHMMSS>.xml`
- `tests/calculator_test_report_<YYYYMMDD_HHMMSS>.xlsx`
and includes reference script details inside the report.

### Run a specific test
```
Run only the divide tests
```

### Delegate to the QA Droid
The main Droid will automatically delegate testing tasks to `qa-droid`.
You can also be explicit:
```
Ask the QA droid to check my test coverage
```

## Skills reference

| Skill | Invoke | What it does |
|---|---|---|
| `test-creator` | `/test-creator` | Reads source, generates pytest test file |
| `test-executor` | `/test-executor` | Runs pytest, reports pass/fail summary, suggests fixes |
| `test-report-generator` | `/test-report-generator` | Runs `tests/generate_test_report.py` and generates timestamped JUnit + Excel reports in `tests/` |

## Running tests manually (without Factory)

```bash
# Run all tests
python -m pytest tests/ -v

# Run a specific test class
python -m pytest tests/test_calculator.py::TestCalculator -v

# Run tests matching a pattern
python -m pytest tests/ -v -k "divide"

# Run only previously failed tests
python -m pytest tests/ --lf -v

# Generate a coverage report
pip install pytest-cov
python -m pytest tests/ --cov=app --cov-report=term-missing

# Generate a timestamped Excel report
python tests/generate_test_report.py --test-target app/test_calculator.py
```
