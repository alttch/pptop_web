#!/usr/bin/env python3

import sys
import markdown2
import requests
from jinja2 import Template
from bleach import linkify

import siteconf

html_context = {'menu': siteconf.menu, 'menu_active': 'Home'}

with open('index.html', 'w') as idx:

    r = requests.get(
        'https://github.com/alttch/pptop/blob/master/README.md?raw=true')
    if not r.ok:
        raise RuntimeError('http code {}'.format(r.code))

    data = markdown2.markdown(r.text)

    with open('tpl/index_header.html') as fh:
        template = Template(fh.read())
        idx.write(template.render(html_context))

    data = ('<p>' +
            data[data.find('ppTOP is'):data.find('p.s. Code in ')].replace(
                '<code>shell', '<code>'))

    for d in data.split('\n'):
        if d.find('"asciicast"') != -1:
            asciinema_id = d.split('"')[1].split('/')[-1]
            d = ((
                '<div class="asciinema-container"><script id="asciicast-{i}" ' +
                'src="https://asciinema.org/a/{i}.js" ' +
                'async data-size="9"></script></div>').format(i=asciinema_id))
        elif d.find(' href ') == -1 and d.find('https://') != -1:
            d = linkify(d).replace(' rel="nofollow"', '')
        d = d.replace('<img src="https://img.shields.io/', '<img style="border: 0px" src="https://img.shields.io/')
        idx.write(d + '\n')

    with open('tpl/index_footer.html') as fh:
        idx.write(fh.read())
