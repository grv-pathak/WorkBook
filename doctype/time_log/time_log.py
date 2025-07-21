# Copyright (c) 2025, Gaurav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class TimeLog(Document):
	def validate(self):
		start = datetime.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
		end = datetime.strptime(self.end_time, "%Y-%m-%d %H:%M:%S")

		duration_seconds = (end - start).total_seconds() / 3600  # Convert seconds to hours
		self.duration = round(duration_seconds/60, 2)  # Round to two decimal places
		
	
