import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

fig,ax=canvas(70)
line(ax,[(41,4),(41,68)],'fixe',lw=0.6)
for x0,r,sym,sx in [(6,'autre','+',18),(48,'sujet','$\\times$',60)]:
    box(ax,x0,50,8,8,r,label='3',size='l'); text(ax,sx,54,sym,'encre','l'); box(ax,x0+16,50,8,8,r,label='5',size='l')
    arrow(ax,(x0+4,49),(x0+20,49),'resultat',curve=0.375,both=True)
    brace(ax,x0,x0+24,37,r,label=None)
text(ax,18,42,'même somme : 8','resultat','m'); text(ax,60,42,'même produit : 15','resultat','m')
text(ax,18,32.5,'termes','autre','m'); text(ax,60,32.5,'facteurs','sujet','m',weight='bold')
text(ax,60,25,'un nom commun aux deux','sujet','s')
text(ax,52,64,'multiplicateur','fixe','s'); text(ax,74,64,'multiplicande','fixe','s')
line(ax,[(52,62.6),(52,58.3)],'fixe',lw=0.6); line(ax,[(74,62.6),(68,58.3)],'fixe',lw=0.6)
save(fig,'03-023')
