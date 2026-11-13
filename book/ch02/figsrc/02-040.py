import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for i in range(9):
    disc(ax,12+8*i,60,2.5,'resultat' if i<5 else 'sujet')
brace(ax,9.5,46.5,56,'resultat',label='d = 5 : il reste')
brace(ax,49.5,78.5,56,'sujet',label='s = 4 : on rend')
numberline(ax,8,76,22,0,10,1,labels=False,role='fixe')
f=lambda v:8+6.8*v
disc(ax,f(9),22,1.2,'fixe'); text(ax,f(9),18,'m = 9','fixe','s')
for i in range(4):
    arrow(ax,(f(9-i),23),(f(9-i-1),23),'sujet',curve=0.5)
text(ax,55.6,33,'s = 4 : longueur du recul','sujet','s')
disc(ax,f(5),22,1.4,'resultat'); text(ax,f(5),18,'d = 5 : arrivée','resultat','s')
save(fig,'02-040')
