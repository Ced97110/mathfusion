import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[16,44,72]
text(ax,44,56,r'on enchaîne $T(g)$ puis $T(g^{-1})$','encre','s')
for y,seq in [(40,'121'),(20,'343')]:
    for i,s in enumerate(seq): disc(ax,xs[i],y,4,'resultat' if i==2 else 'fixe',label=s)
    for i,(rl,lab) in enumerate([('varie',r'$T(g)$'),('autre',r'$T(g^{-1})$')]):
        arrow(ax,(xs[i]+4.5,y),(xs[i+1]-4.5,y),rl)
        text(ax,(xs[i]+xs[i+1])/2,y+4.6,lab,rl,'s')
text(ax,44,5,r'résultat = $T(1)$ : rien ne bouge','resultat','s')
save(fig,'49-104')
