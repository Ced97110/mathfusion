import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
text(ax,44,86,r'$a-b=a+(-b)$','encre','l')
text(ax,44,76,'ancienne : retirer 5 de 3','fixe','s')
for i in range(5):
    disc(ax,18+13*i,64,4.5,'sujet' if i<3 else 'limite',fill=i<3,lw=0.8)
text(ax,44,52,r'$3-5$ : impossible','limite','s')
y=26
f=numberline(ax,8,68,y,-3,4,every=1)
arrow(ax,(f(3),y+6),(f(-2),y+6),'varie')
disc(ax,f(3),y,1.5,'sujet'); disc(ax,f(-2),y,1.7,'resultat')
text(ax,44,y+17,r'nouvelle : ajouter $-5$','varie','s')
text(ax,44,y-8,r'$3-5=3+(-5)=-2$','resultat','s')
save(fig,'13-063')
