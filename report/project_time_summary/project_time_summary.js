// Copyright (c) 2025, Gaurav and contributors
// For license information, please see license.txt

frappe.query_reports["Project Time Summary"] = {
    "filters": [
        {
            "fieldname":"project",
            "label": "Project",
            "fieldtype": "Link",
            "options": "Project"
        },
        {
            "fieldname":"employee",
            "label": "Employee",
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
            "fieldname":"from_date",
            "label": "From Date",
            "fieldtype": "Date"
        },
        {
            "fieldname":"to_date",
            "label": "To Date",
            "fieldtype": "Date"
        }
    ]
};

