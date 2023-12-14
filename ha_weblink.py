#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#

try:
    # py3 - 3.8+
    from html import escape as escape_html
except ImportError:
    # py2 (and <py3.8)
    from cgi import escape as escape_html

from pprint import pprint
import sys

import yaml  # pip install pyyaml


template_head = """<!DOCTYPE html>
<html lang="en">
<! -- from https://www.reddit.com/r/selfhosted/comments/hjk2qd/heimdall_organizr_or_muximux_which_is_the_best/fwqvcyy/  -->
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width" />
		<title>Startpage</title>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <! -- svg from https://www.svgrepo.com/svg/13695/star License: Public Domain CC0 1.0 Universal PD Dedication -->
        <! --
        link rel="icon" type="image/svg+xml" href="ha_weblink.svg"
        -->
        <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3C%3Fxml version='1.0' encoding='us-ascii'%3F%3E%3Csvg height='800px' width='800px' version='1.1' id='star' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 47.94 47.94' xml:space='preserve'%3E%3Cpath style='fill:%23ED8A19;' d='M26.285,2.486l5.407,10.956c0.376,0.762,1.103,1.29,1.944,1.412l12.091,1.757%0Ac2.118,0.308,2.963,2.91,1.431,4.403l-8.749,8.528c-0.608,0.593-0.886,1.448-0.742,2.285l2.065,12.042%0Ac0.362,2.109-1.852,3.717-3.746,2.722l-10.814-5.685c-0.752-0.395-1.651-0.395-2.403,0l-10.814,5.685%0Ac-1.894,0.996-4.108-0.613-3.746-2.722l2.065-12.042c0.144-0.837-0.134-1.692-0.742-2.285l-8.749-8.528%0Ac-1.532-1.494-0.687-4.096,1.431-4.403l12.091-1.757c0.841-0.122,1.568-0.65,1.944-1.412l5.407-10.956%0AC22.602,0.567,25.338,0.567,26.285,2.486z'/%3E%3C/svg%3E">
        <! -- embed svg see https://yoksel.github.io/url-encoder/ -->
		<style>
		:root {
			--base03:  #002b36;
			--base02:  #073642;
			--base01:  #586e75;
			--base00:  #657b83;
			--base0:   #839496;
			--base1:   #93a1a1;
			--base2:   #eee8d5;
			--base3:   #fdf6e3;
			--orange:  #cb4b16;
			--blue:    #268bd2;


			--background: var(--base3);
			--background-highlight: var(--base2);
			--background-secondary: var(--base1);	
			--background-emphasized: var(--base01);
			--text: var(--base00);
			--background-inverse: var(--base03);
		}
		:root .dark {
			--background: var(--base03);
			--background-highlight: var(--base02);
			--background-secondary: var(--base01);	
			--content-emphasized: var(--base1);
			--text: var(--base0);
			--background-inverse: var(--base3);
		}
		body {
			font-family: sans-serif;
			max-width: 800px;
			margin: 5em auto;
			background: var(--background);
			color: var(--text);
			padding: 1em;
		}

		@media (max-width: 600px) {
			body {
				margin: 0.5em auto;
			}
		}

		input {
			background-color: var(--background-highlight);
			border-style: solid;
			border-width: 2px;
			border-color: var(--content-emphasized);
			color: var(--text);
			padding: 1em;
			outline: none;
		}

		input:focus {
			border-color: var(--orange);
		}

		h1, h2, h3, h4, h5, h6 {
			text-align: center;
			color: var(--base01);
		}

		a {
			color: var(--blue);
			outline: none;
		}
		a:active {
			color: var(--orange);
		}
		:focus {
			text-decoration-color: var(--orange);
		}

		ul.site-list {
			padding-left: 0;
			columns: auto;
			list-style: none;
			columns: 200px;
		}
		ul.site-list li {
			padding-top: 0.2em;
			padding-bottom: 0.2em;
		}
		ul.site-list li .favicon {
			height: 2em;
			vertical-align: middle;
			margin-right: 0.5em;
		}
		ul.site-list li .favicon.bg-fix {
			background: var(--base3);
		}
		</style>
		<script>
			window.addEventListener("DOMContentLoaded", (ev) => {
				let date = new Date();
				let hours = date.getHours();
				if (hours >= 20 || hours <= 6) {
					document.body.classList.add("dark");
				}
			});
		</script>
	</head>
	<body>
		<h1>Startpage</h1>
		<form action="https://www.duckduckgo.com" aria-label="Search form">
			<input style="width: 100%;" name="q" type="search" placeholder="DuckDuckGo Search query" autofocus />
		</form>
		<h1>My services</h1>
		<ul class="site-list">
"""

template_tail = """
		</ul>
    Generated with
    <a href="https://github.com/clach04/ha_weblink/">
    https://github.com/clach04/ha_weblink/
    </a>
	</body>
</html>
"""

try:
    # dumb argument parsing
    argv = sys.argv
    yaml_file_name = argv[1]
except IndexError:
    yaml_file_name = 'data.yaml'
with open(yaml_file_name, 'r') as stream:
    data = yaml.safe_load(stream)
    data = data['weblink']['entities']
    #print(data)  # DEBUG
    #pprint(data)  # DEBUG
    print(template_head)
    for weblink in data:
        #pprint(weblink)  # DEBUG
        weblink['name_escaped'] = escape_html(weblink['name'])
        weblink['favicon_url'] = weblink['url']
        if not weblink['favicon_url'].endswith('/'):
            weblink['favicon_url'] += '/'
        weblink['favicon_url'] += 'favicon.ico'
        str_template = '                        <li><img class="favicon" src="{favicon_url}"/><a href="{url}">{name_escaped}</a></li>'  # similar to HA Weblink format (ignores icon) - FIXME use Mustache?
        if '@' in weblink['url'] and weblink.get('icon') is None:
            # looks like URL might have authentication information, do not attempt favicon loading for safety reasons (might leak user on connection attempt)
            weblink['icon'] = 'mdi:vpn lock'
        if weblink.get('icon'):
            if weblink['icon'].startswith('https://') or weblink['icon'].startswith('http://'):
                weblink['favicon_url'] = weblink['icon']
            else:
                if weblink['icon'].startswith('text:'):
                    weblink['icon'] = weblink['icon'][len('text:'):]
                    # span class with some CSS?
                    str_template = '                        <li><span>{icon}</span> <a href="{url}">{name_escaped}</a></li>'
                else:
                    # either icon name of MDI icon name
                    if weblink['icon'].startswith('mdi:'):
                        weblink['icon'] = weblink['icon'][len('mdi:'):]
                    weblink['icon'] = weblink['icon'].replace('-', ' ')
                    if weblink['icon'] == 'harddisk':  # does not appear to be in https://fonts.google.com/icons?icon.category=Hardware
                        weblink['icon'] = 'save'  # not a great match
                    str_template = '                        <li><span class="material-icons">{icon}</span><a href="{url}">{name_escaped}</a></li>'  # similar to HA Weblink format
        print(str_template.format(**weblink))
        # TODO consider using Font Awesome (e.g. https://fontawesome.com/icons/router)
        # Material Design Icons/MDI
        #   https://materialdesignicon font icons
        #   https://stackoverflow.com/questions/31196980/using-a-glyphicon-as-an-li-bullet-point-bootstrap-3/52439818#52439818  -- https://codepen.io/bbbenji/pen/NLJReq
        #   https://iconify.design/icon-sets/mdi/router-wireless.html)
    print(template_tail)


