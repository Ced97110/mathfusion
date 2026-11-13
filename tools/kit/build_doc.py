import json, re, os, sys, html, glob, asyncio
B=os.path.dirname(os.path.abspath(__file__))
F=json.load(open(f'{B}/fiches.json'))
specs={}
for p in sorted(glob.glob(f'{B}/specs/*.json')):
    try:
        for s in json.load(open(p)): specs[s['code']]=s
    except Exception as e: print('spec illisible',p,e)
for p in sorted(glob.glob(f'{B}/fix/F*_textes.json')):
    for c,t in json.load(open(p)).items():
        if c in specs: specs[c].update({k:v for k,v in t.items() if k in ('lecture','a_voir')})
codes={f['code'] for f in F}
print('fiches',len(F),'specs',len(specs),'sans figure',[c for c in codes if not os.path.exists(f'{B}/figs/{c}.svg')])
def clean(s):
    s=s.replace('<m>','<span class="m">').replace('</m>','</span>')
    s=re.sub(r'</span>»','</span> »',s)
    s=re.sub(r' ([:;?!»])',r'&nbsp;\1',s); s=s.replace('« ','«&nbsp;')
    return s
def plain(s): return re.sub(r'<[^>]+>','',s)
def link(s):
    def rep(m):
        c=m.group(1)
        return f'<a href="#f{c}">fiche {c}</a>' if c in codes else m.group(0)
    return re.sub(r'fiche (\d\d-\d\d\d)',rep,s,count=1)
def svg_inline(code):
    p=f'{B}/figs/{code}.svg'
    if not os.path.exists(p): return None
    s=open(p,encoding='utf8').read()
    s=s[s.index('<svg'):]
    s=re.sub(r'<metadata>.*?</metadata>','',s,flags=re.S)
    # ids uniques par figure
    s=re.sub(r'id="([^"]+)"',lambda m:f'id="{code}_{m.group(1)}"',s)
    s=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#{code}_{m.group(1)})',s)
    s=re.sub(r'xlink:href="#([^"]+)"',lambda m:f'xlink:href="#{code}_{m.group(1)}"',s)
    s=re.sub(r'(<svg[^>]*?) width="[^"]+" height="[^"]+"',r'\1',s,count=1)
    return s
RCLS={'1':'cas','2':'signes','3':'question','4':'reponse','5':'limite','6':'lien'}
def rub(f,k):
    r=f['rub'][k]; paras=[p for p in r['paras'] if p.strip()]
    head=f'<h3 class="r {RCLS[k]}"><span class="n">{k}</span>{html.escape(r["label"])}</h3>'
    if k=='2':
        items=[p for p in paras if plain(p).startswith('•')]
        if not items: return f'<div class="rub {RCLS[k]}">{head}<p class="none">Aucun signe nouveau dans cette fiche.</p></div>'
        rows=[]
        for it in items:
            it=re.sub(r'^\s*•\s*','',it)
            parts=re.split(r'\s:\s',it,maxsplit=1)
            if len(parts)==2: rows.append(f'<div class="sg"><div class="sy">{clean(parts[0])}</div><div class="sd">{clean(parts[1])}</div></div>')
            else: rows.append(f'<div class="sg"><div class="sd full">{clean(it)}</div></div>')
        return f'<div class="rub {RCLS[k]}">{head}{"".join(rows)}</div>'
    body=''.join(f'<p>{clean(link(p) if k=="6" else p)}</p>' for p in paras)
    if k=='3': body=re.sub(r'</?i>','',body)
    return f'<div class="rub {RCLS[k]}">{head}{body}</div>'
def figure(code):
    s=specs.get(code); svg=svg_inline(code)
    if not svg: return ''
    cap=''
    if s:
        lect=''.join(f'<li>{clean(html.escape(x))}</li>' for x in s.get('lecture',[]))
        cap=(f'<figcaption><div class="ft"><span class="fl">Figure {code}</span>{clean(html.escape(s.get("legende_titre","")))}</div>'
             f'<ul class="lect">{lect}</ul><p class="voir"><b>À voir.</b> {clean(html.escape(s.get("a_voir","")))}</p></figcaption>')
    return f'<figure>{svg}{cap}</figure>'
def body(f):
    slot=str(SLOTS.get(f['code'],2)); out=''
    for k in '123456':
        out+=rub(f,k)
        if k==slot: out+=figure(f['code'])
    return out
def section_of(f):
    m=re.search(r'›\s*(.*?)\s*›\s*\S+\.?\s*(\d+)\s*$',f['meta']); 
    return (m.group(1).strip() if m else ''), (m.group(2) if m else '')
CH=json.load(open(f'{B}/meta.json'))['num']
only=[a for a in sys.argv[1:] if not a.startswith('--')]
SLOTS=json.load(open(f'{B}/slots.json')) if os.path.exists(f'{B}/slots.json') else {}
out=[]; cur=None; toc=[]
for f in F:
    if only and f['code'] not in only: continue
    sec,pg=section_of(f); sec=re.sub(r'^\d+\.\s*','',sec)
    if sec!=cur:
        cur=sec; sid=f's{len(toc)+1}'; toc.append((sid,sec,f['code']))
        out.append(f'<section class="sec" id="{sid}"><div class="sk">Chapitre {CH} · partie {len(toc)}</div><h1>{html.escape(sec)}</h1></section>')
    flag='<div class="flag">Fiche non validée : elle n’a pas passé tous les contrôles du livre.</div>' if f['flag'] else ''
    out.append(f'''<article class="fiche" id="f{f['code']}">
<div class="code"><span class="cid">Fiche {f['code']}</span><span class="src">livre, p.&nbsp;{pg}</span></div>
<h2>{clean(f['title'])}</h2>{flag}
<blockquote><span class="pl">Le passage du livre</span>{clean(f['passage'])}</blockquote>
{body(f)}
</article>''')
tochtml=''.join(f'<li><a href="#{sid}">{html.escape(sec)}</a></li>' for sid,sec,c in toc)
M=json.load(open(f'{B}/meta.json'))
front=f'''<section class="cover"><div class="ck">Des nombres aux structures</div><div class="cn">Chapitre {M['num']}</div>
<h1 class="ct">{html.escape(M['title'])}</h1>
<p class="cs">{M['n']} fiches, {M['n']} concepts, une figure par concept.</p>
<p class="cx">{html.escape(M['sources'])}</p></section>
<section class="guide"><h1>Comment lire une figure</h1>
<p>Chaque fiche contient une figure, placée après la lecture des signes, ou un peu plus bas dans la fiche quand la page le demande. La figure reprend les nombres du cas concret. Sous la figure, la rubrique «&nbsp;lecture&nbsp;» dit ce que chaque élément représente.</p>
<p>Dans toutes les figures, une couleur garde le même rôle&nbsp;:</p>
<div class="roles">
<div><i style="background:#d6e4f2;border-color:#1f4e79"></i><b style="color:#1f4e79">Bleu</b> l’objet que la fiche définit</div>
<div><i style="background:#fbe3cf;border-color:#b8500a"></i><b style="color:#b8500a">Orange</b> ce qui change, l’action</div>
<div><i style="background:#eceef1;border-color:#5f6773"></i><b style="color:#5f6773">Gris</b> ce qui ne change pas</div>
<div><i style="background:#d5eedd;border-color:#1a7445"></i><b style="color:#1a7445">Vert</b> ce qu’on obtient, ce qui est vrai</div>
<div><i style="background:#f8d9d6;border-color:#b3261e"></i><b style="color:#b3261e">Rouge</b> ce qui est faux, le contre-exemple</div>
<div><i style="background:#e6daf3;border-color:#6d3fa0"></i><b style="color:#6d3fa0">Violet</b> un second objet, comparé au premier</div>
</div>
<p>Les six rubriques d’une fiche portent les mêmes couleurs&nbsp;: la question en orange, la réponse en vert, la limite en rouge.</p></section>
<section class="toc"><h1>Les parties du chapitre</h1><ol>{tochtml}</ol></section>'''
css=open(f'{B}/style.css').read()
doc=f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Des nombres aux structures — fiches illustrées</title><style>{css}</style></head><body>{"" if only else front}{"".join(out)}</body></html>'
open(f'{B}/out.html','w',encoding='utf8').write(doc)
if '--html-only' in sys.argv: sys.exit(0)
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(**(dict(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']) if os.path.exists('/usr/bin/google-chrome') else {}))
        pg=await b.new_page(); errs=[]
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        await pg.goto('file://'+f'{B}/out.html'); await pg.evaluate('document.fonts.ready')
        # débordements horizontaux
        over=await pg.evaluate('''()=>{const W=document.documentElement.clientWidth;return [...document.querySelectorAll('article *')].filter(e=>e.getBoundingClientRect().right>W+1).slice(0,20).map(e=>e.closest('article').id+':'+e.tagName)}''')
        if '--measure' in sys.argv:
            await pg.set_viewport_size(dict(width=378,height=800))
            hs=await pg.evaluate('''()=>{const o={};document.querySelectorAll('article').forEach(a=>{o[a.id.slice(1)]=[...a.querySelectorAll('.rub')].map(r=>r.getBoundingClientRect().height*25.4/96+4)});return o}''')
            json.dump(hs,open(f'{B}/heights.json','w'))
        await pg.pdf(path=f'{B}/out.pdf',width='100mm',height='178mm',print_background=True,outline=True,tagged=True,
            display_header_footer=True,header_template='<span></span>',
            footer_template='<div style="font:7pt Inter,sans-serif;color:#5f6773;width:100%;text-align:center"><span class="pageNumber"></span></div>',
            margin=dict(top='9mm',bottom='11mm',left='0mm',right='0mm'))
        print('console errors',errs[:5],'overflow',over); await b.close()
asyncio.run(main())
