# Copyright (c) 2025, Gaurav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class TimerSession(Document):
    def validate(self):
        self.ensure_one_active_session()
        if self.status == "Stopped":
            self.validate_duration()

    def ensure_one_active_session(self):
        if self.is_active:
            existing = frappe.get_all("Timer Session",
                filters={"user": self.user, "is_active": 1, "name": ["!=", self.name]},
                limit=1)
            if existing:
                frappe.throw("You already have an active timer session running.")

    def validate_duration(self):
        if not self.start_time:
            frappe.throw("Start time is required to stop timer.")
        now = self.get("end_time") or frappe.utils.now_datetime()
        paused = self.paused_time or timedelta()
        effective_time = now - self.start_time - paused
        if effective_time.total_seconds() <= 0:
            frappe.throw("Duration must be greater than zero.")

        # Create Time Log on Stop
        self.create_time_log(effective_time)

    def create_time_log(self, effective_time):
        frappe.get_doc({
            "doctype": "Time Log",
            "task": self.task,
            "user": self.user,
            "start_time": self.start_time,
            "end_time": frappe.utils.now_datetime(),
            "duration": effective_time,
            "is_synced": 1
        }).insert(ignore_permissions=True)

        frappe.msgprint("Time Log created and Timer Stopped.")
