# ─────────────────────────────────────────────────────────────
# ui_main.py — UI setup using PySide6 widgets/layouts
# ─────────────────────────────────────────────────────────────

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, 
    QPushButton, QLabel, QFileDialog, 
    QMessageBox, QTextEdit
)
from src.data_generator import generate_employee_data
from src.excel_exporter import export_to_excel
from datetime import datetime
import os

class EmployeeApp(QWidget):
    """
    Main application window for the Employee Data Generator.

    Features:
    - Numeric input for number of employees
    - Folder selection
    - Data generation and Excel export
    - Real-time export logging (GUI + file-based)
    """

    def __init__(self):
        super().__init__() # Initialize parent widget

        # Initialize log directory and file (daily)
        self.log_dir = os.path.join("data", "export_logs") 
        self.ensure_log_directory()
        self.log_file = self.get_daily_log_file()  # ← sets the log file for the current date

        # Initialize data attributes
        self.data = None
        self.folder_path = ""

        # Build UI
        self.init_ui()

    def ensure_log_directory(self):
        """Ensures the export log directory exists."""
        os.makedirs(self.log_dir, exist_ok=True)

    def get_daily_log_file(self) -> str:
        """Returns the file path for today's log file."""
        today = datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.log_dir, f"{today}.log")

    def load_existing_logs(self) -> None:
        """Loads and displays logs from the current day's log file."""
        self.log_view.clear()
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as file:
                self.log_view.setPlainText(file.read())

    def log_export(self, file_path: str) -> None:
        """Appends a new export entry to the daily log file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Exported file: {file_path}\n"

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(log_entry)

        # Refresh log view
        self.load_existing_logs()

    def init_ui(self):
        """Sets up all UI elements (widgets) and layout."""
        self.setWindowTitle("Employee Data Generator")  # Window title
        self.setGeometry(200, 200, 400, 300)            # Window position and size (x, y, width, height)
        self.layout = QVBoxLayout()  # Vertical layout to stack widgets

        # --- Input field ---
        self.num_input = QLineEdit()  
        self.num_input.setPlaceholderText("Enter number of employees")  # Hint text

        # --- Buttons ---
        self.select_button = QPushButton("Select Folder")   # Button to choose where to save the Excel file
        self.generate_button = QPushButton("Generate Data") # Button to create synthetic data
        self.export_button = QPushButton("Export to Excel") # Button to save the generated data to Excel

        # Labels and log area
        self.status_label = QLabel("")
        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setPlaceholderText("Export logs will appear here...")

        # --- Add widgets to the layout ---
        self.layout.addWidget(self.num_input)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.export_button)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(QLabel("📜 Export History (Today):"))
        self.layout.addWidget(self.log_view)

        # Apply layout to main window
        self.setLayout(self.layout)

        # --- Connect button actions to methods ---
        self.select_button.clicked.connect(self.select_folder)
        self.generate_button.clicked.connect(self.generate_data)
        self.export_button.clicked.connect(self.export_data)

        # --- Load Previous Logs on Startup ---
        self.load_existing_logs()

    def select_folder(self):
        """Opens a dialog for selecting a folder and stores its path."""
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_path = folder
            self.status_label.setText(f"Folder Selected: {folder}")  # Display selected folder path

    def generate_data(self):
        """Generates synthetic employee data based on user input."""
        text = self.num_input.text().strip()

        # Validate input
        if not text.isdigit() or int(text) <= 0:
            QMessageBox.warning(self, "Error", "Please enter a valid positive number!")
            return

        n = int(text)
        self.data = generate_employee_data(n)
        self.status_label.setText(f"Generated {n} employee(s).")

    def export_data(self):
        """Exports generated data to Excel and logs the event."""
        if self.data is None:
            QMessageBox.warning(self, "Error", "No data to export!")
            return

        if not self.folder_path:
            QMessageBox.warning(self, "Error", "Please select a folder first!")
            return

        try:
            file_path = export_to_excel(self.data, self.folder_path)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # --- Update Status and Show Dialog ---
            self.status_label.setText(f"✅ File Generated Successfully at {timestamp}")
            QMessageBox.information(self, "Success", f"File saved at:\n{file_path}\n\nExported at: {timestamp}")

            # --- Log the Export ---
            self.log_export(file_path)

        except Exception as exc:
            QMessageBox.critical(self, "Export Error", f"Failed to export Excel file:\n{exc}")
