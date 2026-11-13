import re, json, html
d=json.load(open('lines.json')); fonts=d['fonts']; lines=d['lines']
import os
words=set(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'words.json'))))
def F(it): return fonts[it['f']]
def kind(l):
    f=F(l[0]); 
    if f['size']==22: return 'chap'
    if f['size']==18 and f['color']=='#1f4e79': return 'title'
    return 'body'
def render(l, main=None):
    # returns html for a visual line
    if main is None:
        main=max(F(it)['size'] for it in l)
    out=[]; prev=None
    for it in sorted(l,key=lambda x:x['left']):
        f=F(it); t=it['t']
        math='Math' in f['fam']
        small=f['size']<main-2
        if small:
            mainits=[x for x in l if F(x)['size']>=main-2]
            mb=max(x['top']+x['h'] for x in mainits) if mainits else it['top']+it['h']
            tag='sup' if (it['top']+it['h'])<mb-2 else 'sub'
            piece=f'<{tag}>{t}</{tag}>'
        else: piece=t
        if math: piece=f'<m>{piece}</m>'
        gap = (it['left']-prev) if prev is not None else 0
        sep = '' if prev is None else (' ' if gap>2.5 else '')
        out.append(sep+piece); prev=it['left']+it['w']
    s=''.join(out)
    for tg in ('b','i'):
        s=re.sub(r'</%s>(\s*)<%s>'%(tg,tg),r'\1',s)
    s=s.replace('</m><m>','').replace('</m> <m>',' ')
    return s
def join(a,b):
    if not a: return b
    m=re.search(r"([A-Za-zÀ-ÿœ]+)-$",re.sub(r'<[^>]+>','',a))
    n=re.match(r"\s*(?:<[^>]+>)*([a-zà-ÿœ]+)",b)
    if m and n:
        w=(m.group(1)+n.group(1)).lower()
        if w in words: return a[:-1]+b   # soft hyphen
        return a+b                       # real hyphen
    return a+' '+b
fiches=[]; cur=None; chap_meta=[]; chap_title=[]; state='pre'
RUB=re.compile(r'^<b>([1-6])\. ([^<]+?)\.?</b>\s*(.*)$')
for l in lines:
    k=kind(l); s=render(l); plain=re.sub(r'<[^>]+>','',s)
    if k=='chap':
        if fiches: break
        chap_title.append(plain); continue
    if k=='title':
        if cur is None or cur['state']!='title':
            cur=dict(title=s,meta='',passage='',rub={},state='title',flag='',page=l[0]['p']); fiches.append(cur)
        else: cur['title']=join(cur['title'],s)
        continue
    if cur is None: chap_meta.append(plain); continue
    if any(F(it)['color']=='#b20000' for it in l): cur['flag']=join(cur['flag'],plain); continue
    if cur['state']=='title' or (cur['state']=='meta' and not plain.startswith('Passage') and not s.startswith('<b>') and not s.startswith('<i>')):
        if F(l[0])['color']=='#b20000' or any(F(it)['color']=='#b20000' for it in l): cur['flag']=join(cur['flag'],plain); cur['state']='meta'; continue
        cur['meta']=join(cur['meta'],plain); cur['state']='meta'; continue
    if plain.startswith('Passage :'): cur['state']='passage'; cur['passage']=s; continue
    m=RUB.match(s)
    if m:
        cur['state']=m.group(1); cur['rub'][m.group(1)]=dict(label=m.group(2),paras=[m.group(3)]); continue
    if cur['state']=='passage': cur['passage']=join(cur['passage'],s); continue
    if cur['state'] in '123456':
        r=cur['rub'][cur['state']]
        if plain.startswith('•'): r['paras'].append(s)
        else: r['paras'][-1]=join(r['paras'][-1],s)
for f in fiches:
    m=re.search(r'Fiche (\S+)',f['meta']); f['code']=m.group(1) if m else '?'
    f['title']=re.sub(r'</?b>','',f['title'])
    f['passage']=re.sub(r'</?i>','',f['passage']); f['passage']=re.sub(r'^Passage :\s*','',f['passage'])
    del f['state']
json.dump(fiches,open('fiches.json','w'),ensure_ascii=False,indent=1)

t=' '.join(chap_title); num=re.match(r'\s*(\S+)',t).group(1); title=re.sub(r'^\s*\S+\s+','',t)
meta=' '.join(chap_meta); i=meta.find('Extrait de'); src=meta[i:] if i>=0 else ''
src=re.sub(r'\s*\d+ fiches pour.*$','',src)
json.dump(dict(num=num,title=title,sources=src,n=len(fiches)),open('meta.json','w'),ensure_ascii=False)
bad=[f['code'] for f in fiches if sorted(f['rub'])!=list('123456') or not f['passage']]
print(len(fiches),'fiches | chapitre',num,'|',title,'| anomalies',bad)
