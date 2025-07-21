# time_per_task.py

import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {
            "label": _("Task"),
            "fieldname": "task",
            "fieldtype": "Link",
            "options": "Task",
            "width": 200
        },
        {
            "label": _("Total Time (in minutes)"),
            "fieldname": "total_time",
            "fieldtype": "Float",
            "width": 180
        }
    ]

    data = frappe.db.sql("""
        SELECT
            task as task,
            SUM(duration) as total_time
        FROM `tabTime Log`
        WHERE task IS NOT NULL
        GROUP BY task
    """, as_dict=1)

    return columns, data
