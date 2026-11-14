import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(96)
box(ax,14,82,60,10,'sujet',label=r'$B(x+y,\,x+y)=0$',size='m')
arrow(ax,(44,82),(44,72),'varie'); text(ax,66,77,'bilinéarité','varie','s')
terms=((r'$B(x,x)$','fixe',0),(r'$B(x,y)$','varie',1),(r'$B(y,x)$','varie',2),(r'$B(y,y)$','fixe',3))
for s,r,i in terms:
    x0=2+i*21.5
    box(ax,x0,52,19,10,r,label=s,size='s')
    if r=='fixe': text(ax,x0+9.5,47,r'$=0$','fixe','s')
    arrow(ax,(x0+9.5,70.5),(x0+9.5,62.5),r,lw=0.8) if False else None
line(ax,[(2,70),(86,70)],'fixe',lw=0.6,dash=True)
text(ax,44,66,'quatre termes','fixe','s')
arrow(ax,(44,44),(44,34),'resultat'); text(ax,66,39,'il reste','resultat','s')
box(ax,6,22,76,10,'resultat',label=r'$B(x,y)+B(y,x)=0$',size='m')
arrow(ax,(44,22),(44,12),'resultat')
box(ax,6,2,76,10,'resultat',label=r'$B(y,x)=-B(x,y)$',size='m')
save(fig,'71-095')
