import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(104)
bx,bw=4,56
text(ax,64,93,'1 départ','fixe','s',ha='left')
box(ax,bx,88,bw,10,'sujet',label=r'$d=au+bv$')
text(ax,32,83,r'la plus petite, $d>0$','sujet','s')
text(ax,64,87,r'ex. : $d=6$ pour 12 et 18','sujet','s',ha='left') if False else None
steps=[(64,r'$a=d\times q+r$'),(49,r'$r=a-d\times q$'),(34,r'$r$ : combinaison de $a$ et $b$'),(19,r'$r<d$, donc $r=0$')]
# cadre de l'étape décisive
ax.add_patch(Rectangle((1.5,16),61,57,ec=COL['varie'],fc='none',lw=1.4,ls='--',zorder=1))
arrow(ax,(32,78),(32,74.5),'fixe')
for i,(y,t) in enumerate(steps):
    box(ax,bx,y,bw,9,'varie',label=t,size='s',lw=1.6 if i==3 else 0.8)
    if i<3: arrow(ax,(32,y-1),(32,y-5),'fixe')
text(ax,64,58,'2 étape décisive','varie','s',ha='left',weight='bold')
text(ax,64,23.5,r'$12=6\times 2+0$','varie','s',ha='left')
arrow(ax,(32,15.2),(32,13.4),'fixe') if False else None
arrow(ax,(32,15.5),(32,13.5),'fixe')
box(ax,bx,3,bw,10,'resultat',label=r'$d\mid a$, $d\mid b$ : PGCD',size='s')
text(ax,64,8,'3 arrivée','fixe','s',ha='left')
save(fig,'05-104')
