import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
vals=['23','18','13','8','3','−2']; w=10; g=4; x0=4; y=22
text(ax,x0,46,'on retire 5 à chaque pas','varie','m',ha='left')
for i,v in enumerate(vals):
    x=x0+i*(w+g)
    role='sujet' if i<4 else ('resultat' if i==4 else 'limite')
    box(ax,x,y,w,9,role,label=v,fill=(i<5),dash=(i==5),size='m')
    if i<5: arrow(ax,(x+w,y+4.5),(x+w+g,y+4.5),'varie')
brace(ax,x0,x0+4*(w+g)+w,y-1,'sujet',label=r'ensemble : $23-5\times x\geq 0$')
text(ax,x0+5*(w+g)+w/2-2,y-7,'négatif : écarté','limite','s')
xr=x0+4*(w+g)+w/2
arrow(ax,(xr,37),(xr,y+10),'resultat')
text(ax,xr,39.5,'le plus petit : r = 3','resultat','s')
save(fig,'05-035')
