import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
w_,h_=17.5,14; xs=[2.25+i*(w_+4.5) for i in range(4)]; y=24
labs=[r'$\sin A$'+'\n0,8','carré\n0,64','reste\n0,36',r'$\cos A$'+'\n0,6']
roles=['sujet','fixe','varie','resultat']
for x,l,r in zip(xs,labs,roles): box(ax,x,y,w_,h_,r,label=l,size='s')
for i in range(3): arrow(ax,(xs[i]+w_+0.3,y+h_/2),(xs[i+1]-0.3,y+h_/2),'fixe')
for x,v in zip(xs[1:],['au carré','1 moins 0,64','racine carrée']):
    text(ax,x+w_/2,y-3.5,v,'varie','s')
text(ax,44,y+h_+6,'une seule mesure suffit','encre','m')
text(ax,44,5,'aucun autre côté mesuré','fixe','s')
save(fig,'26-042')
