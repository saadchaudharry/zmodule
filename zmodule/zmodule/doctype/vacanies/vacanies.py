# Copyright (c) 2022, saaad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Vacanies(Document):
	def on_change(self):
		for i in self.table_13:
			frappe.msgprint('teyeye')
			if frappe.db.exists({'doctype': 'application status','vacanies': self.name,'candidate': i.candidate}):
				pass
			else:
				frappe.get_doc(dict(doctype = 'application status',
									vacanies = self.name,
									candidate = i.candidate,
									time = i.time,
									date = i.date,
									status = 'Set up Interview'
								)).insert()


