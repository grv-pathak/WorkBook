# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):
    filters = filters or {}

    conditions = []
    if filters.get("employee"):
        conditions.append(f"employee = '{filters['employee']}'")
    if filters.get("project"):
        conditions.append(f"project = '{filters['project']}'")
    if filters.get("from_date") and filters.get("to_date"):
        conditions.append(f"start_time BETWEEN '{filters['from_date']}' AND '{filters['to_date']}'")

    condition_str = " AND ".join(conditions)
    if condition_str:
        condition_str = "WHERE " + condition_str

    data = frappe.db.sql(f"""
        SELECT
            project, task, employee, start_time, end_time, duration / 60 as duration
        FROM `tabTime Log`
        {condition_str}
        ORDER BY start_time DESC
    """, as_dict=True)
    columns = [
        {"label": "Project", "fieldname": "project", "fieldtype": "Link", "options": "Project", "width": 150},
        {"label": "Task", "fieldname": "task", "fieldtype": "Link", "options": "Task", "width": 150},
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 120},
        {"label": "Start Time", "fieldname": "start_time", "fieldtype": "Datetime", "width": 150},
        {"label": "End Time", "fieldname": "end_time", "fieldtype": "Datetime", "width": 150},
        {"label": "Duration (Hours)", "fieldname": "duration", "fieldtype": "Float", "width": 130},
    ]

    data = frappe.db.get_all("Time Log",
        fields=["project", "task", "employee", "start_time", "end_time", "duration"],
        order_by="start_time desc"
    )

    # Convert minutes to hours
    for row in data:
        row["duration"] = flt(row["duration"]) / 60  # assuming duration is in minutes

    return columns, data
