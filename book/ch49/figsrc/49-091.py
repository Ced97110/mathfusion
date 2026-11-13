import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$G=\langle x,\,y\ |\ x,\ y\rangle$','encre','l')
text(ax,44,53,'chaque lettre vaut 1','limite','s')
labs=['1',r'$x$',r'$y$',r'$xy$']
box(ax,3,10,28,36,'sujet')
tgt=(66,28)
for i in range(4):
    cy=39-i*9; disc(ax,14,cy,3.8,'sujet',label=labs[i],size='s')
    p=(17.8,cy); q=(tgt[0]-9,tgt[1]+(cy-28)*0.25)
    arrow(ax,p,q,'varie',lw=0.9)
disc(ax,tgt[0],tgt[1],8,'resultat',label='1',size='l')
text(ax,17,6,'mots libres','sujet','s')
text(ax,66,15,'un seul élément','resultat','s')
text(ax,66,41,'K = FG','varie','s')
save(fig,'49-091')
