import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
xs=[3,24,45,66]; cx=[12.5,33.5,54.5,75.5]
for x,d,c,n in zip(xs,'4329',cx,['milliers','centaines','dizaines','unités']):
    last = d=='9'
    box(ax,x,40,19,9,'sujet' if last else 'fixe',label=d,size='l',lw=1.4 if last else 0.8)
    text(ax,c,53,n,'sujet' if last else 'fixe','s')
text(ax,33.5,35,'= 100 unités','fixe','s')
text(ax,54.5,35,'= 10 unités','fixe','s')
for x in [71.5,75.5,79.5]:
    for y in [35,31,27]: disc(ax,x,y,1.2,'sujet')
text(ax,75.5,21,'9 × 1 = 9','resultat','m')
text(ax,86,14,r'1$^{\mathrm{re}}$ case, tout à droite','sujet','s',ha='right')
save(fig,'01-064')
