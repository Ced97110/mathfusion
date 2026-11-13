import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(66)
f=numberline(ax,14,70,35,0,3,arrow_right=False,size='m')
text(ax,42,22,'dimension','fixe','s')
arrow(ax,(f(0),39),(f(2),39),'limite',curve=-0.35)
text(ax,f(1),50,'saut de 2 : pas une marche','limite','s')
for i in range(3):
    arrow(ax,(f(i),28),(f(i+1),28),'resultat',curve=0.5)
    text(ax,(f(i)+f(i+1))/2,18,'+1','resultat','m')
text(ax,42,8,'chaîne maximale : +1 par marche','resultat','s')
save(fig,'80-076')
