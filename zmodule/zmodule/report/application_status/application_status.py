# Copyright (c) 2013, saaad and contributors
# For license information, please see license.txt

import frappe
import datetime

def execute(filters=None):
	sdate=datetime.datetime.strptime(filters.get('sdate_filter'),"%Y-%m-%d")
	edate=datetime.datetime.strptime(filters.get('edate_filter'),"%Y-%m-%d")
	columns=[
				  {
				   "fieldname": "candidate",
				   "fieldtype": "Link",
				   "label": "Candidate",
				   "options": "Candidate"
				  },
				  {
				   "fieldname": "vacanies",
				   "fieldtype": "Link",
				   "label": "Vacanies",
				   "options": "Vacanies"
				  },
				  {
				   "default": "Today",
				   "fieldname": "date",
				   "fieldtype": "Date",
				   "label": "Date"
				  },
				  {
				   "fieldname": "time",
				   "fieldtype": "Data",
				   "label": "Time"
				  },
				  {
				   "fieldname": "status",
				   "fieldtype": "Select",
				   "label": "status",
				   "options": "\nSet up Interview\nSelected\nReplied\nHold\nRejected\nLeave"
				  },
				  {
				   "fieldname": "employee_id",
				   "fieldtype": "Data",
				   "label": "Employee id ",
				  },
				  {
				   "fieldname": "payout",
				   "fieldtype": "Currency",
				   "label": "Payout",
				  },
				  {
				   "fieldname": "date_of_joining",
				   "fieldtype": "Date",
				   "label": "Date of joining",
				  },
				  {
				   "fieldname": "date_of_leaving",
				   "fieldtype": "Date",
				   "label": "Date of leaving",
				  },
				  {
				   "fieldname": "work_day",
				   "fieldtype": "Data",
				   "label": "Work day",
				  },
				  {
				   "fieldname": "company",
				   "fieldtype": "Link",
				   "label": "Company",
				   "options": "Company",
				  }
				 ]

	# , [
	# 		    {'fieldname':'site_name','label':'Site','fieldtype':'Data','width':220},
	# 	        {'fieldname':'test1','label':'Name','fieldtype':'Data','width':220},
	# 	        {'fieldname':'count(*)','label':'Present Days','fieldtype':'Int','width':220},	        
	# 	        {'fieldname':'Sum(human_normal_working_hours)','label':'Normal hour','fieldtype':'Float','width':220},	        
	# 	        {'fieldname':'Sum(human_extra_hours)','label':'Extra hour','fieldtype':'Float','width':220},	        
	# 	        {'fieldname':'max(basic_salary)','label':'Basic salary','fieldtype':'Float','width':220},
	# 	        {'fieldname':'Earned_salary','label':'Earned salary','fieldtype':'Float','width':220},
	# 	        {'fieldname':'Per_hour_salary','label':'Per hour salary','fieldtype':'Float','width':220},	                
	# 	        {'fieldname':'Extra_hour_salary','label':'Extra hour salary','fieldtype':'Float','width':220},	                
	# 	        {'fieldname':'max(travel_allowance)','label':'Travel allowance','fieldtype':'Float','width':220},	                
	# 	        {'fieldname':'max(advance_from_company)','label':'Advance from company','fieldtype':'Float','width':220},	                
	# 	        {'fieldname':'max(advance_from_site)','label':'Advance from site','fieldtype':'Float','width':220},	                
	# 	        {'fieldname':'final_salary','label':' Final salary','fieldtype':'Float','width':220},	                
	# 	        {'fieldname':'total_days','label':'Total days','fieldtype':'data','width':220},	        

 #         ]
	data =frappe.db.get_list('application status', filters=[['date', 'between', [f'{sdate}', f'{edate}']]],fields=[
						  "candidate",
						  "date",
						  "time",
						  "vacanies",
						  "status",
						  "date_of_joining",
						  "date_of_leaving",
						  "employee_id",
						  "payout",
						  "work_day"
						 ])
	if filters.get('Company') != None:
			data =frappe.db.get_list('application status', filters=[['date', 'between', [f'{sdate}', f'{edate}']],['company','=',filters.get('Company')]],fields=[
						  "candidate",
						  "date",
						  "time",
						  "vacanies",
						  "status",
						  "date_of_joining",
						  "date_of_leaving",
						  "employee_id",
						  "payout",
						  "work_day"
						 ])

	return columns, data
