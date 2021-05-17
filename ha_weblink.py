#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#

from cgi import escape as escape_html
from pprint import pprint

import yaml  # pip install pyyaml


yaml_file_name = 'data.yaml'
with open(yaml_file_name, 'r') as stream:
    data = yaml.safe_load(stream)
    data = data['weblink']['entities']
    #print(data)  # DEBUG
    #pprint(data)  # DEBUG
    for weblink in data:
        #pprint(weblink)  # DEBUG
        weblink['name_escaped'] = escape_html(weblink['name']) 
        str_template = '{name}\n{url}'  # FIXME href, use Mustache?
        str_template = '{name}\n<a href="{url}">{url}</a>'  # FIXME cgi escape, use Mustache?
        str_template = '<a href="{url}">{name}</a>'  # FIXME cgi escape, use Mustache?
        str_template = '<a href="{url}">{name_escaped}</a></br>'  # similar to HA Weblink format (ignores icon) - FIXME use Mustache?
        print(str_template.format(**weblink))
        # TODO consider using Font Awesome (e.g. https://fontawesome.com/icons/router)
        # Material Design Icons/MDI
        #   https://materialdesignicon font icons
        #   https://stackoverflow.com/questions/31196980/using-a-glyphicon-as-an-li-bullet-point-bootstrap-3/52439818#52439818  -- https://codepen.io/bbbenji/pen/NLJReq
        #   https://iconify.design/icon-sets/mdi/router-wireless.html)


