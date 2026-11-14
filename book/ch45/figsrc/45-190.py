import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
P=[(0,0),(0,1),(1,0),(1,1)]
text(ax,32,60,'+ lui-même','varie','s')
for i,p in enumerate(P):
    y=46-i*11.5
    box(ax,4,y,18,7,'fixe' if i==0 else 'sujet',label=rf'$({p[0]},{p[1]})$',size='s')
    arrow(ax,(24,y+3.5),(40,y+3.5),'varie')
    box(ax,42,y,18,7,'resultat',label=r'$(0,0)$',size='s')
    text(ax,64,y+3.5,'ordre 1' if i==0 else 'ordre 2','encre','s',ha='left')
save(fig,'45-190')
