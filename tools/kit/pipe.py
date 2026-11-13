"""Pilote du pipeline « une figure par fiche ». Usage (depuis le dossier du kit ou du chapitre) :
  python3 pipe.py setup <chapitre> <pdf> [racine]   -> crée <racine>/chNN, découpe les fiches, fait les lots
  python3 pipe.py adopt <dossier chNN>   -> recopie les scripts du kit dans un chapitre existant (après un clone)
  python3 pipe.py check      -> relance tous les scripts de figures, contrôle la couverture
  python3 pipe.py blind      -> prépare le test à l'aveugle (dossiers blind/Txx, 40 images au plus)
  python3 pipe.py judgein    -> assemble judge/J1.json (attendu / réponse du lecteur)
  python3 pipe.py fixin      -> assemble fix/F1.json à partir de judge/J1_verdicts.json
  python3 pipe.py build      -> construit out.pdf (mise en page + comblement des vides)
"""
import sys, os, json, re, glob, shutil, subprocess, random
KIT=os.path.dirname(os.path.abspath(__file__))
def plain(s):
    s=re.sub(r'<sup>(.*?)</sup>',r'^(\1)',s); s=re.sub(r'<sub>(.*?)</sub>',r'_(\1)',s)
    return re.sub(r'<[^>]+>','',s).strip()
def setup(ch, pdf, root='.'):
    C=json.load(open(f'{KIT}/chapters.json')); keys=list(C); p1=C[ch]; p2=C[keys[keys.index(ch)+1]]
    base=os.path.abspath(os.path.join(root, f'ch{int(ch):02d}' if ch.isdigit() else f'ch{ch}')); os.makedirs(base,exist_ok=True)
    for f in os.listdir(KIT):
        if f.endswith(('.py','.md','.css')): open(f'{base}/{f}','w').write(open(f'{KIT}/{f}').read().replace('__BASE__',base))
        elif f.endswith('.json'): shutil.copy(f'{KIT}/{f}',base)
    for d in 'figs specs figsrc batches blind judge fix private bl'.split(): os.makedirs(f'{base}/{d}',exist_ok=True)
    shutil.copy(f'{base}/test_example.py',f'{base}/figsrc/test.py')
    subprocess.run(['pdftohtml','-xml','-i','-f',str(p1),'-l',str(p2),'-q',pdf,f'{base}/ch1'],check=True)
    subprocess.run([sys.executable,'parse.py'],cwd=base,stdout=subprocess.DEVNULL); print(subprocess.run([sys.executable,'fiches.py'],cwd=base,capture_output=True,text=True).stdout)
    F=json.load(open(f'{base}/fiches.json')); n=16; bs=[F[i:i+n] for i in range(0,len(F),n)]
    if len(bs)>1 and len(bs[-1])<6: bs[-2]+=bs.pop()
    open(f'{base}/titles.txt','w').write('\n'.join(f"{f['code']} — {plain(f['title'])}" for f in F))
    for bi,b in enumerate(bs,1):
        out=[]
        for f in b:
            out.append(f"=== FICHE {f['code']} ===\nTITRE (le concept) : {plain(f['title'])}\nPASSAGE DU LIVRE : {plain(f['passage'])}")
            for k in '123456':
                r=f['rub'][k]; out.append(f"{k}. {r['label']}. "+'\n   '.join(plain(p) for p in r['paras'] if p))
            out.append('')
        open(f'{base}/batches/L{bi:02d}.txt','w').write('\n'.join(out))
    print('dossier',base,'| lots',[len(b) for b in bs])
def adopt(base):
    base=os.path.abspath(base)
    for f in os.listdir(KIT):
        if f.endswith(('.py','.md','.css')) and f not in ('pipe.py',): open(f'{base}/{f}','w').write(open(f'{KIT}/{f}').read().replace('__BASE__',base))
        elif f.endswith('.json'): shutil.copy(f'{KIT}/{f}',base)
    shutil.copy(f'{KIT}/pipe.py',base)
    for d in 'figs specs figsrc batches blind judge fix private bl'.split(): os.makedirs(f'{base}/{d}',exist_ok=True)
    shutil.copy(f'{base}/test_example.py',f'{base}/figsrc/test.py'); print('kit recopié dans',base)
def check():
    F=[f['code'] for f in json.load(open('fiches.json'))]; bad=[]
    for c in F:
        if c=='test': continue
        if not os.path.exists(f'figsrc/{c}.py'): bad.append((c,'script absent')); continue
        r=subprocess.run([sys.executable,f'figsrc/{c}.py'],capture_output=True,text=True)
        if r.returncode or 'OK' not in r.stdout: bad.append((c,(r.stderr or r.stdout)[-160:]))
    S={s['code'] for p in glob.glob('specs/*.json') for s in json.load(open(p))}
    print('échecs',bad,'| figures',sum(os.path.exists(f'figs/{c}.svg') for c in F),'/',len(F),'| légendes manquantes',[c for c in F if c not in S])
def blind(codes=None, prefix='T'):
    F=json.load(open('fiches.json')); byc={f['code']:f for f in F}; codes=codes or [f['code'] for f in F]
    random.seed(5); random.shuffle(codes); key=json.load(open('private/key.json')) if os.path.exists('private/key.json') else {}
    n=40; k=max(1,-(-len(codes)//n)); size=-(-len(codes)//k)
    for ti in range(k):
        t=f'{prefix}{ti+1:02d}'; shutil.rmtree(f'blind/{t}',ignore_errors=True); os.makedirs(f'blind/{t}'); lines=[]
        for j,c in enumerate(codes[ti*size:(ti+1)*size],1):
            nm=f'img{j:02d}'; shutil.copy(f'figs/{c}.png',f'blind/{t}/{nm}.png'); key[f'{t}/{nm}']=c
            lines.append(f"{nm} — cas concret lu juste avant la figure : {plain(' '.join(byc[c]['rub']['1']['paras']))}")
        open(f'blind/{t}/cas.txt','w').write('\n\n'.join(lines)); print('blind/'+t,len(lines))
    json.dump(key,open('private/key.json','w'))
def judgein(prefix='T', out='J1'):
    key=json.load(open('private/key.json')); F={f['code']:f for f in json.load(open('fiches.json'))}
    S={s['code']:s for p in glob.glob('specs/*.json') for s in json.load(open(p))}; rows=[]
    for t in sorted(glob.glob(f'blind/{prefix}*/reponses.json')):
        T=t.split('/')[1]
        for k,v in json.load(open(t)).items():
            c=key[f'{T}/{k}']; rows.append(dict(code=c,concept=plain(F[c]['title']),attendu=S[c]['a_dire'],reponse_lecteur=v.get('idee',''),confiance=v.get('confiance',''),gene=v.get('gene','')))
    rows.sort(key=lambda r:r['code']); json.dump(rows,open(f'judge/{out}.json','w'),ensure_ascii=False,indent=1); print(len(rows),'réponses ->',f'judge/{out}.json')
def fixin():
    V=json.load(open('judge/J1_verdicts.json')); J={r['code']:r for r in json.load(open('judge/J1.json'))}
    S={s['code']:s for p in glob.glob('specs/*.json') for s in json.load(open(p))}
    bad=[v for v in V if v['verdict']!='OK']
    json.dump([dict(spec=S[v['code']],test=dict(reponse_lecteur=J[v['code']]['reponse_lecteur'],gene=J[v['code']]['gene'],manque=v['manque'],correction=v['correction'])) for v in bad],open('fix/F1.json','w'),ensure_ascii=False,indent=1)
    print(len(V),'jugées |',len(bad),'à corriger :',[v['code'] for v in bad])
def build():
    if os.path.exists('slots.json'): os.remove('slots.json')
    subprocess.run(['python3','build_doc.py','--measure']); subprocess.run(['python3','fill.py']); subprocess.run(['python3','blank.py'])
if __name__=='__main__':
    a=sys.argv[1:]
    {'setup':lambda: setup(*a[1:]),'adopt':lambda: adopt(a[1]),'check':check,'blind':blind,'judgein':judgein,'fixin':fixin,'build':build}[a[0]]()
