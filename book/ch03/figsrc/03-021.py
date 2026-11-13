import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

fig,ax=canvas(70)
# écriture : 3 × 4 € = 12 €
text(ax,28,62,'3','varie','l')
text(ax,36,62,'×','encre','l')
text(ax,46,62,'4 €','sujet','l')
text(ax,56,62,'=','encre','l')
text(ax,67,62,'12 €','resultat','l')
# noms des trois nombres
text(ax,22,55,'multiplicateur','varie','s')
text(ax,46,55,'multiplicande','sujet','s')
text(ax,67,55,'produit','resultat','s')
# le multiplicande répété : trois places à 4 €
for x in (24,38,52):
    box(ax,x,36,12,7,'sujet',label='4 €',size='m')
line(ax,[(46,52.5),(44,43)],'sujet',lw=0.6)
# le multiplicateur : accolade
brace(ax,24,64,34,'varie',down=True)
text(ax,44,29,'3 fois, sans unité','varie','s')
# l'unité passe au produit
text(ax,44,18,'l’unité € passe au produit','resultat','s')
arrow(ax,(66,21),(67,52.5),'resultat',curve=0.2)
save(fig,'03-021')
