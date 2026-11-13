import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
f=numberline(ax,5,83,12,0,13,1,labels=False,arrow_right=False)
arrow(ax,(83,12),(86,12),'fixe',lw=0.9)
for v,r in [(0,'fixe'),(5,'fixe'),(8,'fixe'),(13,'resultat')]:
    text(ax,f(v),8,str(v),r,'s')
box(ax,f(0),38,f(8)-f(0),6,'sujet',label='8',size='s'); box(ax,f(8),38,f(13)-f(8),6,'autre',label='5',size='s')
text(ax,14,47.5,'8 + 5','encre','m')
box(ax,f(0),22,f(5)-f(0),6,'autre',label='5',size='s'); box(ax,f(5),22,f(13)-f(5),6,'sujet',label='8',size='s')
text(ax,14,31.5,'5 + 8','encre','m')
line(ax,[(83,10),(83,49)],'resultat',lw=1.2,dash=True)
text(ax,70,51.5,'même bout : 13','resultat','s')
save(fig,'02-058')
