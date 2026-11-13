import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(75)
def solid(x,y,r,role):
    ax.add_patch(Circle((x,y),r,fc=COL[role],ec=COL[role],lw=0.5,zorder=3))
text(ax,24,64,'2','fixe','l'); text(ax,44,64,'<','sujet','l',weight='bold'); text(ax,64,64,'4','fixe','l')
text(ax,24,57,'il reste 2','encre','s'); text(ax,44,51,'strictement plus petit que','encre','s'); text(ax,64,57,'un paquet : 4','encre','s')
for x in (12,18): solid(x,40,1.5,'sujet')
for x in (24,30): ax.add_patch(Circle((x,40),1.5,fc='none',ec=COL['sujet'],lw=0.7,ls='--',zorder=3))
for x in (12,18,24,30): solid(x,33,1.5,'fixe')
text(ax,60,37,'vrai : on ne peut plus','resultat','s')
line(ax,[(4,26),(84,26)],'fixe',lw=0.6)
text(ax,22,16,'4 < 4','limite','l')
text(ax,62,19,'faux : 4 est égal à 4','limite','s'); text(ax,62,12,'on enlève encore : reste 0','limite','s')
save(fig,'03-053')
