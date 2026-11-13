import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
box(ax,12,78,64,10,'sujet',True,r'$-b+\sqrt{D}$  et  $-b-\sqrt{D}$')
arrow(ax,(44,78),(44,72.8),'fixe')
box(ax,14,62,60,10,'varie',True,r'$\sqrt{D}$ existe-t-il ? vaut-il 0 ?',size='s')
cols=[(15,r'$D>0$','différents :\ndeux solutions'),(44,r'$D=0$','égaux :\nune solution'),(73,r'$D<0$',"√D n'existe pas :\naucune solution")]
for i,(cx,h,cap) in enumerate(cols):
    arrow(ax,(44,62),(cx,53.5),'varie')
    text(ax,cx,50,h,'sujet','m')
    line(ax,[(cx-13,34),(cx+13,34)],'fixe')
    if i<2:
        ax.plot([cx,cx],[32.8,35.2],color=COL['fixe'],lw=0.8,zorder=2)
        text(ax,cx,29.5,'$-b$','fixe','s')
    if i==0:
        disc(ax,cx-8,34,2.2,'resultat'); disc(ax,cx+8,34,2.2,'resultat')
    if i==1:
        disc(ax,cx,34,2.2,'resultat')
    text(ax,cx,16,cap,'resultat' if i<2 else 'fixe','s')
save(fig,'23-067')
