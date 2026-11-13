"""Construit le site du livre (un artifact à plusieurs fichiers).
Usage : python3 web.py <racine contenant les dossiers chNN> <dossier de sortie> [toc.json déjà publié]
Écrit <sortie>/index.html (lecteur), <sortie>/toc.json (sommaire) et un fragment <sortie>/chNN.html par chapitre présent.
Si le toc.json déjà publié est donné, les chapitres qu'il connaît sont conservés dans le sommaire."""
import sys, os, re, json, glob, subprocess, html
root, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]); os.makedirs(out, exist_ok=True)
KIT = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(f'{KIT}/chapters.json')); keys = [k for k in C if k != 'FIN']
done = {}
for d in sorted(glob.glob(f'{root}/ch*/')):
    if not os.path.exists(d + 'fiches.json') or not os.path.exists(d + 'build_doc.py'): continue
    slots = d + 'slots.json'
    if os.path.exists(slots): os.rename(slots, slots + '.pdf')          # sur écran : figure à sa place normale
    subprocess.run([sys.executable, 'build_doc.py', '--html-only'], cwd=d, capture_output=True)
    if os.path.exists(slots + '.pdf'): os.rename(slots + '.pdf', slots)
    s = open(d + 'out.html', encoding='utf8').read(); body = s[s.index('<body>') + 6:s.rindex('</body>')]
    body = re.sub(r'<section class="guide">.*?</section>', '', body, flags=re.S)
    m = os.path.join(d, 'meta.json'); n = len(json.load(open(d + 'fiches.json')))
    if os.path.exists(m): M = json.load(open(m)); key, title = str(M['num']), M['title']
    else:
        key = re.search(r'<div class="cn">Chapitre (\S+?)</div>', body).group(1); title = html.unescape(re.sub(r'<[^>]+>', '', re.search(r'<h1 class="ct">(.*?)</h1>', body, re.S).group(1)))
    name = f'ch{int(key):02d}.html' if key.isdigit() else f'ch{key}.html'
    open(f'{out}/{name}', 'w', encoding='utf8').write(body); done[key] = dict(file=name, title=title, n=n)
    print(name, n, 'fiches', os.path.getsize(f'{out}/{name}') // 1024, 'Ko')
prev = {str(c['key']): c for c in json.load(open(sys.argv[3])) if c.get('file')} if len(sys.argv) > 3 else {}
allc = {**prev, **{k: dict(key=k, **v) for k, v in done.items()}}
toc = [allc[k] if k in allc else dict(key=k) for k in keys]
json.dump(toc, open(f'{out}/toc.json', 'w'), ensure_ascii=False)
css = open(f'{KIT}/style.css').read()
shell = open(f'{KIT}/web_shell.html', encoding='utf8').read().replace('/*CSS*/', css)
open(f'{out}/index.html', 'w', encoding='utf8').write(shell)
print('index.html + toc.json :', sum(1 for c in toc if c.get('file')), 'chapitres sur', len(keys))
