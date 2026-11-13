import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
for x in (22,70): line(ax,[(x,14),(x,70)],'fixe',dash=True,lw=0.7)
text(ax,22,74,'16 000','fixe','s'); text(ax,70,74,'17 000','fixe','s')
def ticks(y):
    for x in (22,70): line(ax,[(x,y-1.2),(x,y+1.2)],'fixe',lw=0.8)
# ligne 1
y=64; ticks(y)
line(ax,[(22,y),(70,y)],'fixe'); line(ax,[(22,y),(46,y)],'resultat',lw=1.6)
disc(ax,46,y,1.0,'autre',label=None); text(ax,11,y,'16 499','autre','m')
text(ax,34,67.5,'499','resultat','s'); text(ax,58,67.5,'501','fixe','s')
disc(ax,22,y,1.4,'resultat'); text(ax,79,y,'plus proche','resultat','s')
# ligne 2
y=42; box(ax,3,35,82,14,'sujet'); ticks(y)
line(ax,[(22,y),(46,y)],'fixe',lw=1.2); line(ax,[(46,y),(70,y)],'fixe',lw=1.2)
disc(ax,46,y,1.3,'sujet'); text(ax,11,y,'16 500','sujet','m')
text(ax,34,38.5,'500','fixe','s'); text(ax,58,38.5,'500','fixe','s')
arrow(ax,(47.5,43.5),(69,43.5),'varie',curve=-0.3)
disc(ax,70,y,1.4,'varie'); text(ax,77,38.5,'convention','varie','s')
# ligne 3
y=20; ticks(y)
line(ax,[(22,y),(70,y)],'fixe'); line(ax,[(46,y),(70,y)],'resultat',lw=1.6)
disc(ax,46,y,1.0,'autre'); text(ax,11,y,'16 501','autre','m')
text(ax,34,23.5,'501','fixe','s'); text(ax,58,23.5,'499','resultat','s')
disc(ax,70,y,1.4,'resultat'); text(ax,79,16.5,'plus proche','resultat','s')
save(fig,'01-110')
