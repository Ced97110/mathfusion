import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
w_,h_=17,15; xs=[4+i*(w_+4.5) for i in range(4)]; y=34
labs=[r'$\frac{a^2}{c^2}+\frac{b^2}{c^2}$',r'$\frac{a^2+b^2}{c^2}$',r'$\frac{c^2}{c^2}$','1']
roles=['sujet','sujet','varie','resultat']
for x,l,r in zip(xs,labs,roles): box(ax,x,y,w_,h_,r,label=l,size='s')
for i in range(3): arrow(ax,(xs[i]+w_+0.4,y+h_/2),(xs[i+1]-0.4,y+h_/2),'varie' if i==1 else 'fixe')
text(ax,xs[0]+w_/2,y+h_+3,'départ','sujet','s')
text(ax,xs[2]+w_/2,y+h_+3,'étape décisive','varie','s')
text(ax,xs[3]+w_/2,y+h_+3,'arrivée','resultat','s')
text(ax,(xs[1]+xs[2]+w_)/2,y-4,r'$a^2+b^2=c^2$ (Pythagore)','varie','s')
text(ax,44,14,r'triangle 2, 3, 4 : $2^2+3^2=13$','limite','s')
text(ax,44,7,r'mais $4^2=16$ : $\frac{13}{16}\neq1$','limite','s')
save(fig,'26-040')
