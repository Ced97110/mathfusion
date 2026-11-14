import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
names=['commutativité','associativité','distributivité','éléments neutres','compléments']
text(ax,44,75,'cinq règles, cinq noms courts','fixe','s')
for i,n in enumerate(names):
    y=62-i*12
    box(ax,6,y-5,16,10,'sujet',label='A%d'%(i+1),weight='bold')
    arrow(ax,(23,y),(33,y),'varie')
    text(ax,36,y,n,'encre','m',ha='left')
text(ax,44,2.5,'dans une preuve : « par A3 »','varie','s')
save(fig,'80-148')
