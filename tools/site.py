"""Met à jour le site à partir des chapitres présents dans book/.
Usage (depuis la racine du dépôt) : python3 tools/site.py
Reconstruit le fragment HTML de chaque chapitre de book/chNN, le copie dans public/chapters/,
et met à jour content/toc.json en gardant les chapitres déjà connus."""
import os, sys, subprocess, shutil, glob, json, tempfile
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tmp = tempfile.mkdtemp()
subprocess.run([sys.executable, f'{root}/tools/kit/web.py', f'{root}/book', tmp, f'{root}/content/toc.json'], check=True)
os.makedirs(f'{root}/public/chapters', exist_ok=True)
for p in glob.glob(f'{tmp}/ch*.html'): shutil.copy(p, f'{root}/public/chapters/')
shutil.copy(f'{tmp}/toc.json', f'{root}/content/toc.json')
toc = json.load(open(f'{root}/content/toc.json'))
print('site à jour :', sum(1 for c in toc if c.get('file')), 'chapitres,', sum(c.get('n', 0) for c in toc), 'fiches')
