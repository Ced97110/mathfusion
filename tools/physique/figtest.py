"""Check the interactive figures of the physics book in headless Chrome. Zero tokens.

Usage (from the repo root): python3 tools/physique/figtest.py [shots_dir] [id ...]
Without ids, tests every id of public/physique/fig/index.json.
For each figure: no JS error, an SVG is drawn, no NaN/Infinity, the drawing changes whenever the
sliders move (50 random settings) and with rotation (3D). Writes <shots_dir>/<id>_{default,alt}.png.
Exit code 1 if a figure fails.
"""
from __future__ import annotations

import functools
import http.server
import json
import os
import re
import subprocess
import sys
import tempfile
import threading

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def serve(site: str) -> int:
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args: object) -> None:
            pass

    handler = functools.partial(Quiet, directory=site)
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv.server_address[1]


def chrome(args: list[str]) -> str:
    cmd = [CHROME, '--headless', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=6000', *args]
    for _ in range(2):  # headless Chrome sometimes hangs: one retry
        try:
            return subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout
        except subprocess.TimeoutExpired:
            continue
    return ''


def main() -> None:
    shots = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else tempfile.mkdtemp()
    os.makedirs(shots, exist_ok=True)
    ids = sys.argv[2:] or json.load(open(f'{ROOT}/public/physique/fig/index.json'))
    site = tempfile.mkdtemp()
    os.symlink(f'{ROOT}/public/physique', f'{site}/physique')
    os.symlink(f'{ROOT}/tools/physique/figtest.html', f'{site}/figtest.html')
    os.symlink(f'{ROOT}/app/globals.css', f'{site}/site.css')
    base = f'http://127.0.0.1:{serve(site)}/figtest.html'
    failed = 0
    for fid in ids:
        dom = chrome(['--dump-dom', f'{base}?id={fid}&mode=check'])
        m = re.search(r'<pre id="out">(.*?)</pre>', dom, re.S)
        r = json.loads(m.group(1).replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')) if m and m.group(1) else {'errors': ['no report']}
        ok = (not r.get('errors') and r.get('svg', 0) > 0 and not r.get('nan') and not r.get('nanAfter')
              and (r.get('sliders', 0) == 0 or (r.get('changes', 0) > 0 and r.get('stuck', 1) == 0)) and r.get('rotates', True))
        failed += not ok
        print('OK   ' if ok else 'ÉCHEC', fid, json.dumps({k: v for k, v in r.items() if k != 'id'}, ensure_ascii=False))
        name = fid.replace('/', '_')
        for mode in ('default', 'alt'):
            chrome([f'--screenshot={shots}/{name}_{mode}.png', '--window-size=760,900', f'{base}?id={fid}&mode={mode}'])
    print(f'{len(ids) - failed}/{len(ids)} figures valides ; captures dans {shots}')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
