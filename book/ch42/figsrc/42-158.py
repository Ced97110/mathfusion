import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
for k in range(40):
    disc(ax,6+(k%10)*5,40-(k//10)*5,1.8,'resultat')
text(ax,29,50,r'$n=0$ à $39$ : 40 réussites','resultat','s')
text(ax,29,15,'tous premiers','resultat','s')
disc(ax,70,36,5,'limite'); text(ax,70,36,'40','limite','l')
text(ax,70,25,r'$40^2+40+41$','limite','s'); text(ax,70,19,r'$=41\times41$','limite','s')
text(ax,70,11,'pas premier','limite','s',weight='bold')
save(fig,'42-158')
