// Copyright (c) 2016, saaad and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["application status"] = {
	"filters": [{
    fieldname: "sdate_filter",
    label: "Date Filter",
    fieldtype: "Date",
    //Note the following default attribute, which contains an API call
    default: frappe.datetime.get_today()
},
{
    fieldname: "edate_filter",
    label: "Date Filter",
    fieldtype: "Date",
    //Note the following default attribute, which contains an API call
    default:frappe.datetime.get_today()
},
{
    fieldname: "Company",
    label: "Company",
    fieldtype: "Link",
    options:'Company'
    //Note the following default attribute, which contains an API call
    // default:frappe.datetime.get_today()
}

	]
};
