# ─────────────────────────────────────────────────────────────
# ui_main.py — UI setup using PySide6 widgets/layouts
# ─────────────────────────────────────────────────────────────

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, 
    QPushButton, QLabel, QFileDialog, 
    QMessageBox
)
from data_generator import generate_employee_data
from excel_exporter import export_to_excel
from datetime import datetime

class EmployeeApp(QWidget):
    """
    Main application window for the Employee Data Generator.

    Provides:
    - a numeric input for number of employees (with validator),
    - folder selection,
    - generate data button (produces a pandas.DataFrame),
    - export
    """

    def __init__(self):
        super().__init__()  # Initialize parent QWidget
        self.init_ui()      # Build and configure the user interface
        self.data = None    # Placeholder for generated employee DataFrame
        self.folder_path = ""  # Stores the folder path chosen by the user

    def init_ui(self):
        """Sets up all UI elements (widgets) and their layout."""
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

        # --- Label for status messages ---
        self.status_label = QLabel("")  # Displays info like "File Generated" or "Folder Selected"

        # --- Add widgets to the layout ---
        self.layout.addWidget(self.num_input)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.export_button)
        self.layout.addWidget(self.status_label)

        # Apply layout to main window
        self.setLayout(self.layout)

        # --- Connect button actions to methods ---
        self.select_button.clicked.connect(self.select_folder)
        self.generate_button.clicked.connect(self.generate_data)
        self.export_button.clicked.connect(self.export_data)

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
        self.status_label.setText(f"Generated {n} employees.")

    def export_data(self):
        """Exports the generated data to an Excel file."""
        # Check if data exists
        if self.data is None:
            QMessageBox.warning(self, "Error", "No data to export!")
            return

        # Check if user selected a folder
        if not self.folder_path:
            QMessageBox.warning(self, "Error", "Please select a folder first!")
            return

        try:
            file_path = export_to_excel(self.data, self.folder_path)
            self.status_label.setText("✅ File Generated Successfully!")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            QMessageBox.information(self, "Success", f"File saved at:\n{file_path}\n\nExported at: {timestamp}")

        except Exception as exc:
            QMessageBox.critical(self, "Export Error", f"Failed to export Excel file:\n{exc}")
