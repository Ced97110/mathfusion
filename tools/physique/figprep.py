"""Prepare a batch of physics figures for an interactive-figure agent. Zero tokens.

Usage (from the repo root): python3 tools/physique/figprep.py <batch_dir> <chapter> [<chapter> ...]
Writes <batch_dir>/figures.json  [{id, chapter, page, ref}] and <batch_dir>/ref/<id>.png
(the book figure rendered at 740 px). Skips figures that already have a module in public/physique/fig/.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    batch = os.path.abspath(sys.argv[1])
    os.makedirs(f'{batch}/ref', exist_ok=True)
    out = []
    for ch in sys.argv[2:]:
        key = f'{int(ch):03d}'
        page = open(f'{ROOT}/public/physique/c{key}.html', encoding='utf8').read()
        for m in re.finditer(r'<img class="vf" src="/physique/img/(c\d+/(p(\d+)_\d+))\.svg"', page):
            fid, pdf_page = m.group(1), int(m.group(3))
            if os.path.exists(f'{ROOT}/public/physique/fig/{fid}.js'):
                continue
            name = fid.replace('/', '_')
            html = f'{batch}/ref/{name}.html'
            with open(html, 'w', encoding='utf8') as f:
                f.write(f"<body style=margin:0><img src='file://{ROOT}/public/physique/img/{fid}.svg' "
                        "style='width:740px;display:block'>")
            subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                            '--window-size=740,700', f'--screenshot={batch}/ref/{name}.png', f'file://{html}'],
                           capture_output=True, timeout=60)
            os.remove(html)
            out.append({'id': fid, 'chapter': int(ch), 'page': pdf_page, 'ref': f'{batch}/ref/{name}.png'})
    json.dump(out, open(f'{batch}/figures.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(len(out), 'figures ->', f'{batch}/figures.json')


if __name__ == '__main__':
    main()
