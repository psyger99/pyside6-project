# 🧮 Employee Data Generator (PySide6 + Pandas)

A simple desktop application built with **PySide6**, **Faker**, and **Pandas** that generates synthetic employee data, exports it to Excel, and logs every export automatically.

---

## 🚀 Features

✅ **User-friendly GUI** built with PySide6  
✅ **Generates synthetic employee data** (emp_id, full_name, department, salary, hire_date)  
✅ **Exports to Excel** with:
   - `Employees` sheet (full dataset)
   - `Summary` sheet (average salary per department)

✅ **Auto-logs every export** with timestamp and file path  
✅ **Daily log files** stored under `/export_logs`  
✅ **Export history panel** to view all exports made today  

---

## 🧩 Tech Stack

- **PySide6** – for the GUI  
- **Pandas** – for Excel file creation  
- **Faker** – for generating realistic names and dates  
- **OpenPyXL** – for Excel I/O support  

## 📦 Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/psyger99/pyside6-project.git
   cd employee-data-generator
   ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate     # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## 🖥️ Usage

1. Run the app:
    ```bash
    python app.py
    ```
2. In the Employee Data Generator window:
    - Enter the number of employees to generate
    - Click Select Folder to choose where to save the Excel file
    - Click Generate Data to create the dataset
    - Click Export to Excel to export the data and view confirmation
    - See the Export History (Today) section for logs of your exports

## 📁 File Structure
```bash
employee-data-generator/
│
├── app.py                # Entry point
├── ui_main.py            # Main PySide6 GUI
├── data_generator.py     # Synthetic data creation
├── excel_exporter.py     # Excel export logic
├── export_logs/          # Daily log files (auto-created)
└── README.md             # Project documentation
```

## 📖 Author
```bash
© Rainer Alano | Data Engineering Practitioner
```
