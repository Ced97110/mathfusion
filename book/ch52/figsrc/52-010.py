import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,53,'deux représentants, un même paquet ?','encre','s')
box(ax,56,10,29,36,'resultat'); text(ax,70.5,38,'paquet de','resultat','s'); text(ax,70.5,30,'reste 9','resultat','l',weight='bold')
for y,role,lab,eq in [(36,'varie','choix 1','7 × 3 = 21'),(14,'autre','choix 2','19 × 15 = 285')]:
    box(ax,2,y-6,46,16,role)
    text(ax,25,y+5.5,lab,role,'s'); text(ax,25,y-1,eq,role,'m')
    arrow(ax,(48,y+2),(55.2,28),'resultat')
save(fig,'52-010')
