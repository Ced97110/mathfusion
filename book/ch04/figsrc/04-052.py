import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
# écriture sans barre : trois signes cerclés
text(ax,24,58,'sans barre : 3 signes','fixe','s')
text(ax,8,40,'(','encre','l')
text(ax,16.5,40,'6 + 4','encre','l')
text(ax,25,40,')','encre','l')
text(ax,31,40,'÷','encre','l')
text(ax,37,40,'2','encre','l')
for x in (8,25,31):
    disc(ax,x,40,2.6,'autre',fill=False)
# écriture avec barre
text(ax,68,58,'avec barre : 1 signe','encre','s')
text(ax,66,46,'6 + 4','encre','l')
line(ax,[(58,40),(74,40)],'sujet',lw=1.4)
text(ax,66,34,'2','encre','l')
# flèche et résultats
arrow(ax,(40,20),(60,37),'varie')
text(ax,30,14,'( , ) et ÷ → une barre','varie','s')
text(ax,45,40,'= 5','resultat','l')
text(ax,80,40,'= 5','resultat','l')
save(fig,'04-052')
