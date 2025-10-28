# ─────────────────────────────────────────────────────────────
# excel_exporter.py — Handles Excel writing and summary creation
# ─────────────────────────────────────────────────────────────

import pandas as pd

def export_to_excel(df: pd.DataFrame, folder_path: str) -> str:
    """
    Export the employee data DataFrame to an Excel file with a summary sheet.

    Args:
        df (pd.DataFrame): The DataFrame containing employee data.
        folder_path (str): The directory path where the Excel file will be saved.

    Returns:
        str: The full file path of the exported Excel file.
    """

    # Ensure the folder path is valid and construct file path
    file_path = f"{folder_path}/employees.xlsx"

    # Create Excel file with two sheets
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        # Sheet1: Employee data
        df.to_excel(writer, sheet_name="Employees", index=False)

        # Sheet 2: Summary (e.g., average salary per department)
        summary = (
            df.groupby("department")["salary"]
            .mean()
            .reset_index()
            .rename(columns={"salary": "ave_salary"}) # Rename `salary` column
        )
        summary["ave_salary"] = summary["ave_salary"].map(lambda x: f"{x:,.2f}")

        # Export to excel
        summary.to_excel(writer, sheet_name="Summary", index=False)
    
    return str(file_path)