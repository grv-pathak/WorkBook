import frappe
from datetime import datetime

@frappe.whitelist()
def get_current_running_timer():
    user = frappe.session.user
    doc = frappe.get_all("Time Sheet", filters={"status": "Running", "owner": user}, fields=["name", "start_time"])
    if doc:
        start_time = doc[0].start_time
        now = frappe.utils.now_datetime()
        duration = (now - start_time).total_seconds()
        hrs, rem = divmod(duration, 3600)
        mins, secs = divmod(rem, 60)
        return {
            "status": "Running",
            "duration": f"{int(hrs):02}:{int(mins):02}:{int(secs):02}"
        }
    return {"status": "Idle"}
