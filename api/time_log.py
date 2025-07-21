# apps/workbook/workbook/api/time_log.py

import frappe

@frappe.whitelist()
def create_time_log(task, from_time, to_time, duration):
    log = frappe.new_doc("Time Log")
    log.task = task
    log.from_time = from_time
    log.to_time = to_time
    log.duration = duration
    log.insert()
    return log.name
