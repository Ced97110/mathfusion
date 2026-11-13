import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for y in (52,32,12):
    numberline(ax,34,84,y,0,12,1,labels=False,arrow_right=False)
    arrow(ax,(84,y),(86.5,y),'fixe',lw=0.9)
text(ax,17,55,r'12 ÷ 4','autre','m'); text(ax,17,49,'défini : 1 réponse','autre','s')
disc(ax,46.5,52,1.4,'resultat'); text(ax,46.5,56,'3','resultat','s')
text(ax,17,35,r'12 ÷ 0','autre','m'); text(ax,17,29,'indéfini : 0 réponse','autre','s')
text(ax,59,36,'aucun nombre','limite','s')
text(ax,17,15,r'0 ÷ 0','sujet','m',weight='bold'); text(ax,17,9,'indéterminé : infinité','sujet','s')
ax.plot([34,84],[12,12],color=COL['resultat'],lw=3,alpha=0.45,zorder=1.2,solid_capstyle='butt')
text(ax,59,16,'tous les nombres','resultat','s')
save(fig,'03-107')
