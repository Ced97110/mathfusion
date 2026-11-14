import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,'valeur de la somme des carrés','encre','s')
y=34
arrow(ax,(4,y),(83,y),'fixe',lw=0.9)
box(ax,3,36.5,20,8,'limite',label='jamais < 0',size='s')
box(ax,27,36.5,53,8,'resultat')
ax.plot([24],[y],'o',ms=6,mfc=FILL['fixe'],mec=COL['fixe'],zorder=6)
ax.plot([69],[y],'o',ms=6,mfc=FILL['resultat'],mec=COL['resultat'],zorder=6)
text(ax,24,49,'seul $x=0$','fixe','s'); text(ax,56,49,r'$x$ non nul : somme $>0$','resultat','s')
text(ax,69,28.5,'9','resultat','m'); text(ax,69,24,'$x=(1,2,0,2)$','resultat','s')
for x,w_,l in ((2,20,'$x$ non nul'),(30,24,'somme $>0$'),(62,24,'$x$ a un inverse')):
    box(ax,x,5,w_,10,'sujet' if x<30 else 'resultat',label=l,size='s')
arrow(ax,(23,10),(29,10),'fixe'); arrow(ax,(55,10),(61,10),'fixe')
save(fig,'51-188')
