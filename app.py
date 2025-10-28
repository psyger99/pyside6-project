# ─────────────────────────────────────────────────────────────
# app.py — Entry point, launches the GUI
# ─────────────────────────────────────────────────────────────

import sys
from PySide6.QtWidgets import QApplication
from ui_main import EmployeeApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeApp()
    window.show()

    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        print("\nProgram terminated by user!")