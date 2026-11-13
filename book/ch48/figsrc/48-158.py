import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
disc(ax,32,32,20,'sujet',fill=False,lw=1.2); disc(ax,56,32,16,'autre',fill=False,lw=1.2)
text(ax,20,56,'$H$','sujet','l'); text(ax,66,52,'$N$','autre','l')
for lab,x,y,r in [('4',24,40,'sujet'),('8',24,24,'sujet'),('6',63,32,'autre'),('0',46,32,'resultat')]:
    disc(ax,x,y,3.6,r,label=lab,size='m')
text(ax,46,41,'commun','resultat','s')
box(ax,22,2,44,9,'resultat'); text(ax,44,6.5,r'$H\cap N=\{0\}$','resultat','m')
save(fig,'48-158')
