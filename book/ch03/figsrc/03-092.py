import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,4,56,38,10,'limite',label='4 : par 2, pas par 6',size='s')
box(ax,46,56,38,10,'limite',label='9 : par 3, pas par 6',size='s')
text(ax,44,48,'multiples de 3','sujet','s')
xs=[4+13.6*i for i in range(6)]
for i,(x,l) in enumerate(zip(xs,[3,6,9,12,15,18])):
    box(ax,x,32,12,10,'resultat' if i%2 else 'fixe',label=str(l),size='l')
cx=[x+6 for i,x in enumerate(xs) if i%2]
for x in cx: line(ax,[(x,32),(x,20)],'resultat')
line(ax,[(cx[0],20),(cx[-1],20)],'resultat')
text(ax,50.8,15,'pairs : multiples de 6','resultat','m')
text(ax,50.8,7,'6 = 2 × 3','resultat','s')
save(fig,'03-092')
