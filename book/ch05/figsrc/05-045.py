import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
y=22; P=[2,3,5,7,11,13,17,19,23]
f=numberline(ax,6,74,y,2,25,step=1,labels=False,arrow_right=True)
for p in P:
    disc(ax,f(p),y,1.4,'resultat'); text(ax,f(p),y-4.5,str(p),'resultat','s')
for a,b in zip(P,P[1:]): arrow(ax,(f(a),y+2),(f(b),y+2),'varie',lw=0.7,curve=-0.7)
text(ax,f(13),y+11,'écarts : 1 2 2 4 2 4 2 4','varie','s')
text(ax,84,y,'?','limite','l')
text(ax,44,6,'ni règle, ni fin visibles','limite','m')
save(fig,'05-045')
