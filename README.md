# Financial Pre-Plans CLI (`fin_pre_plans`)

A modular, production-ready Python Command-Line Interface (CLI) utility built for structured personal expense tracking, dynamic category management, and automated financial report generation with strict currency precision.

---

## Key Features

* **Exact Financial Precision:** Utilizes Python's `decimal.Decimal` with explicit rounding to prevent floating-point calculation drift.
* **Dynamic Category Management:** Real-time category selection and on-the-fly custom category insertion during entry sessions.
* **Safe Overrides:** Detects existing item entries and allows price updates while tracking history.
* **CSV Data Persistence:** Automatically writes formatted, timestamped reporting to isolated CSV files in append mode.
* **Automated Unit & Integration Test Suite:** Full automated test coverage using `pytest`, `monkeypatch`, and `tmp_path` fixtures.

---

## System Architecture & Module Overview

```text
fin_pre_plans/
├── expenses_cli.py     # Prompt management, input validation, dynamic category mapping
├── file_manager.py     # CSV export pipeline and file system handling
├── income.py           # Validated income input parsing and decimal quantisation
├── main.py             # CLI entry point and pipeline orchestrator
├── month_expenses.py   # Core business logic, totals calculation, and override tracking
└── tests/              # Full unit and integration test suite (21 tests)
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Sivuyisile/financial-cli-utility.git](https://github.com/Sivuyisile/financial-cli-utility.git)
cd financial-cli-utility
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage

Run the main CLI script to initiate a monthly tracking session:

```bash
python main.py
```

### Sample Session Flow:
1. Enter monthly income when prompted.
2. Select or create an expense category.
3. Input item details, quantity, and unit price.
4. Review the final summary output and generated CSV file (`expense_tracker_<Month>_<Year>.csv`).

---

## Running Automated Tests

The application is thoroughly tested against edge cases, string inputs, negative values, file operations, and pipeline flows.

To run the complete test suite:

```bash
pytest -v
```

---

## Project Roadmap

- [x] **v1.0:** Core CLI utility with full unit/integration test suite and CSV export.
- [ ] **v2.0 (Phase 1):** JSON/SQLite data persistence and historical multi-month querying.
- [ ] **v3.0 (Phase 2):** Configurable recurring monthly expense templates.
- [ ] **v4.0 (Phase 3):** Category budget thresholds and spending percentage analytics.
- [ ] **v5.0 (Phase 4):** Refactoring core domain logic to Django REST Framework (DRF) backend architecture.