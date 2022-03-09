# Copyright (c) 2022, saaad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.share import add


class applicationstatus(Document):
	def after_insert(self):
		vacancy = frappe.get_doc('Vacanies',self.vacanies)
		add('application status', self.name, vacancy.owner, 1, 1, 0, 0)

	def on_update(self):
		frappe.msgprint("YOOO")
		if self.status == "Selected":
			vacancy = frappe.get_doc('Vacanies',self.vacanies)
			company = frappe.get_doc('Company',vacancy.company)

			if company.invoice_type == "mixed":
				if frappe.db.exists({'doctype': 'Invoice','company': vacancy.company,'docstatus':0}):
					# doc = frappe.get_last_doc({'doctype': 'Invoice','company': vacancy.company,'docstatus':0})
					# # yah pe select ke if dall ni hai 
					doc= frappe.db.get_value('Invoice', {'company': vacancy.company,'docstatus':0}, ['name'])

					frappe.msgprint(f'{doc}-ddddddd')


					if frappe.db.exists({'doctype': 'Invoice Child Doc','parent': doc, 'parentfield': 'table_3', 'parenttype': 'Invoice', "product": self.candidate }):
						frappe.db.set_value('Invoice Child Doc',{'parent': doc,
							'parentfield': 'table_3',
							'parenttype': 'Invoice',
							"product": self.candidate},{
							"amount":self.payout,
							"doj": self.date_of_joining,
							'data_4': self.employee_id, 
							'data_5': None
							})
					else:
						doc3=frappe.get_doc({'doctype': 'Invoice Child Doc','parent': doc,
							'parentfield': 'table_3',
							'parenttype': 'Invoice', 
							"product": self.candidate,
							"amount":self.payout,
							"doj": self.date_of_joining,
							'data_4': self.employee_id, 
							'data_5': None
							})
						doc3.save()

				else:
					frappe.msgprint('else wala wala')
					doc = frappe.get_doc({'doctype': 'Invoice','company': vacancy.company,'docstatus':0})
					# yah pe select ke if dall ni hai 
					doc.append("table_3",{
						"product": self.candidate,
						"doj": self.date_of_joining,
						"amount":self.payout,
						'data_4': self.employee_id, 
						})
					doc.insert()


			elif company.invoice_type == "per jd":
				if frappe.db.exists({'doctype': 'Invoice','vacanies':vacancy.name,'company': vacancy.company,'docstatus':0}):
					# doc = frappe.get_last_doc({'doctype': 'Invoice','company': vacancy.company,'docstatus':0})
					# # yah pe select ke if dall ni hai 
					doc= frappe.db.get_value('Invoice', {'company': vacancy.company,'vacanies':vacancy.name,'docstatus':0}, ['name'])

					frappe.msgprint(f'{doc}-ddddddd')


					if frappe.db.exists({'doctype': 'Invoice Child Doc','parent': doc, 'parentfield': 'table_3', 'parenttype': 'Invoice', "product": self.candidate }):
						frappe.db.set_value('Invoice Child Doc',{'parent': doc,
							'parentfield': 'table_3',
							'parenttype': 'Invoice',
							"product": self.candidate},{
							"amount":self.payout,
							"doj": self.date_of_joining,
							'data_4': self.employee_id, 
							'data_5': None
							})
					else:
						doc3=frappe.get_doc({'doctype': 'Invoice Child Doc','parent': doc,
							'parentfield': 'table_3',
							'parenttype': 'Invoice', 
							"product": self.candidate,
							"amount":self.payout,
							"doj": self.date_of_joining,
							'data_4': self.employee_id, 
							'data_5': None
							})
						doc3.save()

				else:
					frappe.msgprint('else wala wala')
					doc = frappe.get_doc({'doctype': 'Invoice','vacanies':vacancy.name,'company': vacancy.company,'docstatus':0})
					# yah pe select ke if dall ni hai 
					doc.append("table_3",{
						"product": self.candidate,
						"doj": self.date_of_joining,
						"amount":self.payout,
						'data_4': self.employee_id, 
						})
					doc.insert()

		if self.status == "Leave":
			vacancy = frappe.get_doc('Vacanies',self.vacanies)
			company = frappe.get_doc('Company',vacancy.company)
			if frappe.db.exists({'doctype': 'Invoice','vacanies':vacancy.name,'company': vacancy.company,'docstatus':0}):
					doc= frappe.db.get_value('Invoice', {'company': vacancy.company,'vacanies':vacancy.name,'docstatus':0}, ['name'])
					frappe.msgprint(f'{doc}-ddddddd')
					if frappe.db.exists({'doctype': 'Invoice Child Doc','parent': doc, 'parentfield': 'table_3', 'parenttype': 'Invoice', "product": self.candidate }):
						frappe.db.delete('Invoice Child Doc',{'parent': doc,
							'parentfield': 'table_3',
							'parenttype': 'Invoice',
							"product": self.candidate})





					# frappe.msgprint('if wala wala')
					# doc.append("table_3",{
					# 	"product": self.candidate,
					# 	"doj": self.date_of_joining,
					# 	"amount":self.payout
					# 	})
					# doc.save()