# Copyright (c) 2025, Gaurav and contributors
# For license information, please see license.txt

# import frappe
#from frappe import _

'''
def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Column 1"),
			"fieldname": "column_1",
			"fieldtype": "Data",
		},
		{
			"label": _("Column 2"),
			"fieldname": "column_2",
			"fieldtype": "Int",
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return [
		["Row 1", 1],
		["Row 2", 2],
	]
    '''
# Copyright (c) 2025
# License: MIT

import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 180},
        {"label": "Total Duration (Hours)", "fieldname": "total_hours", "fieldtype": "Float", "width": 200},
    ]

    data = frappe.db.sql("""
        SELECT
            employee,
            SUM(duration) / 60 AS total_hours
        FROM `tabTime Log`
        WHERE employee IS NOT NULL
        GROUP BY employee
        ORDER BY total_hours DESC
    """, as_dict=True)

    return columns, data


