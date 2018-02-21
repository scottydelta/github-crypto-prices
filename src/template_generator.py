#! ../env/bin/python
# -*- coding: utf-8 -*-

import json
from jinja2 import Template

if __name__=="__main__":
    config_json = json.loads(open("config.json", "r").read())
    icons_json = json.loads(open("icons.json", "r").read())
    raw_template = open("template.jinja2", "r+").read()
    load_template = Template(raw_template)
    render_template = load_template.render(sources=config_json, icons=icons_json)
    output = open("../README.md", "w")
    output.write(render_template)
    output.close()