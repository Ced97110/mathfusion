import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
for y,n,r in ((34,0,'fixe'),(14,1,'sujet')):
    box(ax,4,y,22,12,r,label=rf'$x={n}$',size='l')
    arrow(ax,(28,y+6),(36,y+6),'varie')
    box(ax,38,y,46,12,'resultat',label=rf'${n}\times{n}={n}$',size='l')
text(ax,44,5,r'deux valeurs seulement : donc $x^2=x$','encre','s')
text(ax,44,48,'ce que donne un nombre fois lui-même','encre','s')
save(fig,'80-018')
