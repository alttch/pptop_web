#!/usr/bin/env python3

import markdown2
import requests
from bleach import linkify

with open('index.html', 'w') as idx:

    r = requests.get(
        'https://github.com/alttch/pptop/blob/master/README.md?raw=true')
    if not r.ok:
        raise RuntimeError('http code {}'.format(r.code))

    data = markdown2.markdown(r.text)

    with open('tpl/index_header.html') as fh:
        idx.write(fh.read())

    data = ('<p>' +
            data[data.find('ppTOP is'):data.find('p.s. Code in ')].replace(
                '<code>shell', '<code>'))

    for d in data.split('\n'):
        if d.find('"asciicast"') != -1:
            asciinema_id = d.split('"')[1].split('/')[-1]
            d = ((
                '<div class="asciinema-container"><script id="asciicast-{i}" ' +
                'src="https://asciinema.org/a/{i}.js" async></script></div>'
            ).format(i=asciinema_id))
        elif d.find(' href ') == -1 and d.find('https://') != -1:
            d = linkify(d).replace(' rel="nofollow"', '')
        idx.write(d + '\n')

    with open('tpl/index_footer.html') as fh:
        idx.write(fh.read())
