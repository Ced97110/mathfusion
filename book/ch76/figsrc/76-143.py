import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
k=2.2; y=14
def sq(x,a,role,l):
    s=(a**0.5)*k; poly(ax,[(x,y),(x+s,y),(x+s,y+s),(x,y+s)],role); text(ax,x+s/2,y-4,l,role,'s'); return s
s1=sq(4,1,'sujet','aire 1'); s2=sq(22,13,'varie','aire 13'); s3=sq(46,221,'resultat','aire 221')
arrow(ax,(4+s1+1,y+s1/2),(21,y+s1/2),'fixe'); text(ax,14,y+6,r'$\times 13$','fixe','s')
arrow(ax,(22+s2+1,y+s2/2),(45,y+s2/2),'fixe'); text(ax,34,y+6,r'$\times 17$','fixe','s')
text(ax,44,50,r'$13\times 17=221$','resultat','l')
save(fig,'76-143')
