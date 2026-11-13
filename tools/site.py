"""Met à jour le site à partir des chapitres présents dans book/.
Usage (depuis la racine du dépôt) : python3 tools/site.py
Seuls les chapitres qui ont une ligne dans book/JOURNAL.md sont publiés.
Reconstruit le fragment HTML de chaque chapitre de book/chNN, le copie dans public/chapters/,
et met à jour content/toc.json en gardant les chapitres déjà connus."""
import os, sys, subprocess, shutil, glob, json, tempfile
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tmp = tempfile.mkdtemp()
subprocess.run([sys.executable, f'{root}/tools/kit/web.py', f'{root}/book', tmp, f'{root}/content/toc.json'], check=True)
os.makedirs(f'{root}/public/chapters', exist_ok=True)
for p in glob.glob(f'{tmp}/ch*.html'): shutil.copy(p, f'{root}/public/chapters/')
shutil.copy(f'{tmp}/toc.json', f'{root}/content/toc.json')
shutil.rmtree(tmp, ignore_errors=True)  # mkdtemp is never cleaned otherwise and fills the disk
# Only chapters with a row in book/JOURNAL.md are published: a chapter still in progress
# (possibly in another session) stays off the site.
import re
done = set(re.findall(r'^\| [0-9-]+ \| (\w+) — ', open(f'{root}/book/JOURNAL.md').read(), re.M))
toc = json.load(open(f'{root}/content/toc.json'))
for c in toc:
    if c.get('file') and c['key'] not in done:
        p = f"{root}/public/chapters/{c['file']}"
        if os.path.exists(p): os.remove(p)
        c.pop('file'); c.pop('n', None); c.pop('title', None)
json.dump(toc, open(f'{root}/content/toc.json', 'w'), ensure_ascii=False)
toc = json.load(open(f'{root}/content/toc.json'))
print('site à jour :', sum(1 for c in toc if c.get('file')), 'chapitres,', sum(c.get('n', 0) for c in toc), 'fiches')
