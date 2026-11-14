import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,3,10,82,40,'fixe',fill=False,dash=True)
text(ax,10,54,r'$S$','encre','m')
box(ax,7,14,34,32,'sujet'); box(ax,47,14,34,32,'autre')
text(ax,24,40,'pairs','sujet','m'); text(ax,64,40,'impairs','autre','m')
for k in range(6):
    disc(ax,12+(k%3)*10,30-(k//3)*8,1.5,'sujet')
    disc(ax,52+(k%3)*10,30-(k//3)*8,1.5,'autre')
text(ax,44,30,'|','limite','xl')
text(ax,44,5,'aucun point dans les deux ; tous dans un','resultat','s')
save(fig,'42-296')
