import subprocess,json,glob,os,re
import numpy as np
from PIL import Image
H=json.load(open('heights.json')); slots={}; tries={}; cursor=1; builds=0
def build():
    global builds; builds+=1
    json.dump(slots,open('slots.json','w')); subprocess.run(['python3','build_doc.py'],capture_output=True)
def npages(): return int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo','out.pdf'],capture_output=True,text=True).stdout).group(1))
def gap(p):
    subprocess.run(['pdftoppm','-r','20','-gray','-png','-f',str(p),'-l',str(p),'-singlefile','out.pdf','bl/x'],stderr=subprocess.DEVNULL)
    a=np.array(Image.open('bl/x.png')); h=a.shape[0]; body=a[:int(h*0.925)]
    rows=np.where(body.min(axis=1)<200)[0]; last=rows.max() if len(rows) else 0
    return (body.shape[0]-last)/h*178
build(); N=npages()
while cursor<N:
    g=gap(cursor)
    if g<=30: cursor+=1; continue
    t=subprocess.run(['pdftotext','-f',str(cursor+1),'-l',str(cursor+1),'out.pdf','-'],capture_output=True,text=True).stdout.strip()
    m=re.match(r'FIGURE (\d\d-\d\d\d)',t)
    if not m: cursor+=1; continue
    c=m.group(1); s=slots.get(c,2)
    if s>=6 or tries.get(c,0)>=3: cursor+=1; continue
    acc=0; t2=s
    while t2<6 and acc<g-4: acc+=H[c][t2]; t2+=1
    slots[c]=t2; tries[c]=tries.get(c,0)+1; build(); N=npages()
    cursor=max(1,cursor-1)
print('builds',builds,'pages',N,'figures déplacées',len(slots))
