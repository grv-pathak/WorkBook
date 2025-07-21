# Copyright (c) 2025, Gaurav and contributors
# For license information, please see license.txt

#import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import get_datetime

class TimeSheet(Document):
    pass
'''
    def before_save(self):
        # If start and end times exist, calculate duration
        if self.start_time and self.end_time:
            start = get_datetime(self.start_time)
            end = get_datetime(self.end_time)
            duration = (end - start).total_seconds() / 60   # duration in minutes

            # Avoid duplicate Time Logs on every save
            if not frappe.db.exists("Time Log", {"time_sheet": self.name}):
                time_log = frappe.new_doc("Time Log")
                time_log.time_sheet = self.name
                time_log.task = self.task
                time_log.project = self.project
                time_log.from_time = self.start_time
                time_log.to_time = self.end_time
                time_log.duration = duration
                time_log.status = "Completed"
                time_log.employee = self.employee
                time_log.insert(ignore_permissions=True)
                frappe.msgprint("Time Log created successfully.")
		
'''