import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,3,6,82,52,'sujet',fill=False,dash=True)
text(ax,44,53,r'seuls idéaux : $\{0\}$ et tout','sujet','m')
box(ax,7,12,36,32,'resultat'); box(ax,45,12,36,32,'autre')
text(ax,25,36,'commutatif','resultat','m'); text(ax,63,36,'non commutatif','autre','m')
text(ax,25,25,'corps','resultat','l',weight='bold'); text(ax,63,25,'anneau simple','autre','m',weight='bold')
text(ax,25,17,r'ex. $\mathbb{Z}/5$','resultat','s'); text(ax,63,17,r'ex. $M_2(\mathbb{R})$','autre','s')
save(fig,'52-280')
