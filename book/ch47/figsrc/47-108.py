import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,2,8,38,48,'sujet'); text(ax,21,50,'classe de 5\nmodulo 12','sujet','s')
for y,l in [(38,'5'),(26,'17'),(14,'29')]: disc(ax,21,y,4.5,'fixe',label=l)
text(ax,66,52,'reste du nom par 5','encre','s')
for y,l in [(38,'0'),(26,'2')]:
    arrow(ax,(26,y),(59,y),'varie'); box(ax,60,y-5,14,10,'limite',label=l,size='l')
text(ax,66,14,'deux réponses','limite','m'); text(ax,66,9,'pour une classe','limite','m')
save(fig,'47-108')
