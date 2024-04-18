def generate_frontend(names):
    page_content = "Names List\n"
    page_content += "-------------\n"
    for name in names:
        page_content += "- {}\n".format(name)
    page_content += "\n"
    page_content += "Add a name:\n"
    page_content += "<form action='/add_name' method='POST'>\n"
    page_content += "<input type='text' name='name' required>\n"
    page_content += "<input type='submit' value='Add'>\n"
    page_content += "</form>\n"
    return page_content
