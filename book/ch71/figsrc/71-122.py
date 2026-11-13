import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
tot=['1','2','3','4','0']
for i in range(5):
    x=12+16*i
    disc(ax,x,42,4.5,'sujet',label='1')
    arrow(ax,(x,37),(x,33),'varie')
    box(ax,x-5,24,10,8,'resultat' if i==4 else 'fixe',label=tot[i])
brace(ax,7.5,80.5,49,'sujet','5 termes égaux à 1',down=False)
text(ax,44,16,'somme après chaque terme','fixe','s')
text(ax,44,7,r'$5=0$ : caractéristique $p=5$','resultat','m')
save(fig,'71-122')
