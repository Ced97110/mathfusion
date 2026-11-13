import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,4,16,30,26,'sujet'); text(ax,10,37,'A','sujet','l')
disc(ax,22,32,3,'sujet',label='2'); disc(ax,22,22,3,'sujet',label='5')
box(ax,54,16,30,26,'fixe',fill=False,dash=True)
text(ax,69,34,r'$\emptyset$','fixe','l'); text(ax,69,23,'rien dedans','fixe','s')
for y in (32,22):
    arrow(ax,(26,y),(38,y),'limite'); text(ax,46,y,r'$\times$ non','limite','s')
box(ax,18,2,52,9,'resultat',label=r'$A\cap\emptyset=\emptyset$')
save(fig,'42-145')
