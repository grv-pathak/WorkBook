import frappe
from frappe.utils import now_datetime
from frappe import _

@frappe.whitelist(allow_guest=False)
def sync_offline_queue(queue_data):
    """
    queue_data: JSON list of actions from local queue
    Example:
    [
        {
            "user": "gaurav@example.com",
            "task": "TASK-001",
            "action_type": "Start",
            "action_timestamp": "2025-07-19 13:45:00"
        },
        ...
    ]
    """

    import json
    if isinstance(queue_data, str):
        queue_data = json.loads(queue_data)

    results = []

    for action in queue_data:
        try:
            task_id = action.get("task")
            user = action.get("user")
            action_type = action.get("action_type")
            timestamp = action.get("action_timestamp")

            if not (task_id and user and action_type):
                continue

            # Route action to correct backend logic
            if action_type == "Start":
                start_timer_backend(task_id, user, timestamp)
            elif action_type == "Pause":
                pause_timer_backend(task_id, user, timestamp)
            elif action_type == "Resume":
                resume_timer_backend(task_id, user, timestamp)
            elif action_type == "Stop":
                stop_timer_backend(task_id, user, timestamp)

            # Optional: log success
            results.append({ "task": task_id, "action": action_type, "status": "success" })

        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Offline Queue Sync Failed")
            results.append({ "task": action.get("task"), "action": action.get("action_type"), "status": "error", "error": str(e) })

    return results

def start_timer_backend(task_id, user, timestamp):
    # Your custom logic (can also reuse from API)
    doc = frappe.get_doc({
        "doctype": "Time Session",
        "user": user,
        "task": task_id,
        "status": "Running",
        "start_time": timestamp,
        "is_active": 1
    })
    doc.insert()

def pause_timer_backend(task_id, user, timestamp):
    session = get_active_session(user, task_id)
    session.last_paused_at = timestamp
    session.status = "Paused"
    session.save()

def resume_timer_backend(task_id, user, timestamp):
    session = get_active_session(user, task_id)

    if not session.last_paused_at:
        raise Exception("Pause time missing.")

    paused_duration = frappe.utils.time_diff_in_seconds(timestamp, session.last_paused_at)
    session.paused_time = (session.paused_time or 0) + paused_duration
    session.status = "Running"
    session.save()

def stop_timer_backend(task_id, user, timestamp):
    session = get_active_session(user, task_id)

    effective_time = frappe.utils.time_diff_in_seconds(timestamp, session.start_time) - (session.paused_time or 0)
    if effective_time <= 0:
        raise Exception("Duration must be positive")

    # Create Time Log
    frappe.get_doc({
        "doctype": "Time Log",
        "task": task_id,
        "user": user,
        "duration": effective_time,
        "from_time": session.start_time,
        "to_time": timestamp
    }).insert()

    session.status = "Stopped"
    session.is_active = 0
    session.save()

def get_active_session(user, task):
    return frappe.get_doc("Time Session", {
        "user": user,
        "task": task,
        "is_active": 1
    })
