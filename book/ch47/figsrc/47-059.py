import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,45,64,'un nom par élément','encre','m')
xs=[24,38,52,66]; roles=['varie','fixe','sujet']
for r,(y,role) in enumerate(zip([52,38,24],roles)):
    for k,x in enumerate(xs):
        if r==0: disc(ax,x,y,3.6,role,label=str([1,4,7,10][k]),size='s')
        else: disc(ax,x,y,3.6,role)
text(ax,45,13,'4 noms par ligne','varie','s')
text(ax,45,5,r'$3\times4=12$ noms, 12 éléments','resultat','s')
save(fig,'47-059')
