import sys
from PIL import Image
codes=sys.argv[2:]; ims=[Image.open(f'figs/{c}.png') for c in codes]
cols=3; w=max(i.width for i in ims); rows=[ims[i:i+cols] for i in range(0,len(ims),cols)]
H=sum(max(i.height for i in r)+12 for r in rows); m=Image.new('RGB',(cols*(w+12),H),'#777'); y=0
for r in rows:
    for j,i in enumerate(r): m.paste(i,(j*(w+12),y))
    y+=max(i.height for i in r)+12
m.thumbnail((2000,2000)); m.save(sys.argv[1])
