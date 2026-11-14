import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
O=(50,10);u=8
def P(x,y,z): return iso(x,y,z,O,u)
arrow(ax,P(0,0,0),P(1,0,0),'sujet',lw=1.6)
arrow(ax,P(0,0,0),P(0,3,0),'varie',lw=1.6)
arrow(ax,P(0,0,0),P(0,0,3),'resultat',lw=1.6)
text(ax,P(1,0,0)[0]+2,P(1,0,0)[1]-1,'bras (1, 0, 0)','sujet','s',ha='left')
text(ax,P(0,3,0)[0]-2,P(0,3,0)[1]+1,'force (0, 3, 0)','varie','s',ha='right')
text(ax,P(0,0,3)[0]+1,P(0,0,3)[1]+4,'moment (0, 0, 3)','resultat','s')
text(ax,44,2.5,'bras × force = moment','fixe','s')
save(fig,'78-175')
