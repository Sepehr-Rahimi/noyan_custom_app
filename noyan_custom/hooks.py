app_name = "noyan_custom"
app_title = "Noyan Custom"
app_publisher = " "
app_description = " "
app_email = "n@n.n"
app_license = "mit"


fixtures = [
    "Client Script",
    "Server Script",
    "Custom Field",
    "Property Setter",
    {
        "doctype": "DocType",
        "filters": [["module", "=", "Noyan Custom"]]
    }
]

# override_doctype_dashboards = {
#     "Customer Projects": "noyan_custom.dashboard_overrides.get_dashboard_data"
# }

