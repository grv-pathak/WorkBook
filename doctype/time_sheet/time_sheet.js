// Copyright (c) 2025, Gaurav and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Time Sheet", {
// 	refresh(frm) {

// 	},
// });let startTime = null;
//
//frappe.call({
//    method: "workbook.api.create_time_log",
//    args: {
//        user: frappe.session.user,
//        time_sheet: frm.doc.name,
//        start_time: frm.doc.start_time,
//        end_time: frappe.datetime.now_datetime(),  // capture current time as end time
//        project: frm.doc.project,
//        duration: frm.doc.total_duration || 0
//    },
//    callback: function(r) {
//        if (!r.exc) {
//            frappe.msgprint("Time Log created successfully.");
//        }
//   }
//});
