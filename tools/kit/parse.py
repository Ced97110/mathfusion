import re, json, html, sys
import xml.etree.ElementTree as ET
src=open('ch1.xml',encoding='utf8').read()
src=re.sub(r'<!DOCTYPE[^>]*>','',src)
root=ET.fromstring(src)
fonts={}
lines=[]  # (page, top, left, fontid, htmltext)
for page in root.iter('page'):
    pn=int(page.get('number'))
    for fs in page.iter('fontspec'):
        fonts[fs.get('id')]=dict(size=int(fs.get('size')),fam=fs.get('family'),color=fs.get('color'))
    items=[]
    for t in page.iter('text'):
        top=int(t.get('top'));left=int(t.get('left'));w=int(t.get('width'));h=int(t.get('height'))
        inner=ET.tostring(t,encoding='unicode',method='xml')
        inner=re.sub(r'^<text[^>]*>','',inner); inner=re.sub(r'</text>\s*$','',inner)
        inner=re.sub(r'<a [^>]*>','',inner).replace('</a>','')
        if top>740: continue  # page number
        items.append(dict(p=pn,top=top,left=left,w=w,h=h,f=t.get('font'),t=inner))
    # anchors = non-math, main-size items; cluster by vertical centre
    def ctr(it): return it['top']+it['h']/2
    anch=[it for it in items if 'Math' not in fonts[it['f']]['fam']]
    rest=[it for it in items if 'Math' in fonts[it['f']]['fam']]
    anch.sort(key=ctr); groups=[]
    for it in anch:
        if groups and abs(ctr(it)-groups[-1]['c'])<=6: groups[-1]['its'].append(it)
        else: groups.append(dict(c=ctr(it),its=[it]))
    rest.sort(key=lambda it:(-fonts[it['f']]['size'],ctr(it)))
    for it in rest:
        best=min(groups,key=lambda g:abs(g['c']-ctr(it))) if groups else None
        if best and abs(best['c']-ctr(it))<=10: best['its'].append(it)
        else: groups.append(dict(c=ctr(it),its=[it]))
    groups.sort(key=lambda g:g['c'])
    for g in groups: lines.append(sorted(g['its'],key=lambda d:d['left']))
json.dump(dict(fonts=fonts,lines=lines),open('lines.json','w'),ensure_ascii=False)
print(len(lines)); 
from collections import Counter
c=Counter()
for l in lines:
    for it in l: c[(fonts[it['f']]['size'],fonts[it['f']]['fam'].split('+')[1],fonts[it['f']]['color'])]+=1
for k,v in sorted(c.items(),key=lambda x:-x[1]): print(v,k)
