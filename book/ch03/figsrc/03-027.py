import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

fig,ax=canvas(68)
text(ax,14,63,'3','sujet','l',weight='bold'); text(ax,20.5,63,'×','encre','l'); text(ax,27,63,'5','sujet','l',weight='bold')
for i in range(3):
    for j in range(5): box(ax,8+5*j,26+5*i,5,5,'sujet',lw=0.5,r=0.2)
for i in range(5):
    for j in range(3): box(ax,60+5*j,26+5*i,5,5,'autre',lw=0.5,r=0.2)
text(ax,4.5,33.5,'3 rangées','varie','s',rot=90)
arrow(ax,(12.5,61),(5,40.5),'varie',curve=0.3)
brace(ax,8,33,42,'varie',label=None,down=False); text(ax,20.5,46.5,'5 carreaux','varie','s')
arrow(ax,(27,61),(22,48.5),'varie',curve=0.3)
text(ax,67.5,63,'5 × 3','autre','l')
brace(ax,60,75,52,'autre',label=None,down=False); text(ax,67.5,56.5,'3 carreaux','autre','s')
text(ax,56,38.5,'5 rangées','autre','s',rot=90)
text(ax,20.5,21,'15 carreaux','resultat','s'); text(ax,67.5,21,'15 carreaux','resultat','s')
text(ax,44,12,'même total, autre dessin','encre','s')
save(fig,'03-027')
