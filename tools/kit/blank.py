import subprocess,glob,os,sys
from PIL import Image
import numpy as np
os.makedirs('bl',exist_ok=True); [os.remove(f) for f in glob.glob('bl/*')]
subprocess.run(['pdftoppm','-r','20','-gray','-png','out.pdf','bl/p'],stderr=subprocess.DEVNULL)
tot=0;big=[]
fs=sorted(glob.glob('bl/p-*.png'))
for i,f in enumerate(fs,1):
    a=np.array(Image.open(f)); h=a.shape[0]; body=a[:int(h*0.925)]  # hors pied de page
    rows=np.where(body.min(axis=1)<200)[0]; last=rows.max() if len(rows) else 0
    gap=(body.shape[0]-last)/h*178; tot+=gap
    if gap>45: big.append((i,round(gap)))
print('pages',len(fs),'vide moyen mm',round(tot/len(fs),1),'pages avec >45mm vides',len(big),big[:12])
