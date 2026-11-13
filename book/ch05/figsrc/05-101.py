import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,14,71,60,10,'sujet',label=r'$a\times u+b\times v$')
text(ax,44,66,r'$a=12$ et $b=18$','fixe','s')
text(ax,16,58,r'$u$ entier','varie','s')
text(ax,36,58,r'$v$ entier','varie','s')
rows=[(1,1,'30'),(2,0,'24'),(-1,1,'6')]
for k,(u,v,res) in enumerate(rows):
    y=42-k*13
    box(ax,8,y,16,9,'varie',label=str(u).replace('-','−'))
    box(ax,28,y,16,9,'varie',label=str(v).replace('-','−'))
    arrow(ax,(46,y+4.5),(58,y+4.5),'fixe')
    box(ax,60,y,20,9,'resultat',label=res)
for dx in (0,4,8):
    pass
for i in range(3):
    disc(ax,18+i*0,1.0,0.0,'fixe') if False else None
for i in range(3):
    ax.add_patch(Circle((44+(i-1)*4,3.2),0.9,ec=COL['fixe'],fc=COL['fixe'],zorder=3))
text(ax,44+10,3.2,'tous les autres','fixe','s',ha='left') if False else None
text(ax,70,3.2,'et tous les autres','fixe','s')
save(fig,'05-101')
