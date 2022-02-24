# Copyright (c) 2022, saaad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.share import add


class applicationstatus(Document):
	def after_insert(self):
		vacancy = frappe.get_doc('Vacanies',self.vacanies)
		add('application status', self.name, vacancy.owner, 1, 1, 0, 0)
