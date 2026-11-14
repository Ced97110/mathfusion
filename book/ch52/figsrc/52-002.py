import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,3,40,82,20,'fixe')
text(ax,44,55,'les entiers ℤ','fixe','m')
text(ax,44,45,'…  −1  0  1  2  3  4  5  6  7  …','fixe','s')
rs=['sujet','varie','resultat','autre']; mem=['0, 4, 8','1, 5, 9','2, 6, 10','3, 7, 11']
for i in range(4):
    x=3+i*21
    box(ax,x,18,19,16,rs[i])
    text(ax,x+9.5,29,f'reste {i}',rs[i],'s'); text(ax,x+9.5,22.5,mem[i],rs[i],'s')
    arrow(ax,(x+9.5,40),(x+9.5,34.8),'fixe')
text(ax,44,10,'paquet + paquet = paquet ?','varie','m')
text(ax,44,3,'paquet × paquet = paquet ?','varie','m')
save(fig,'52-002')
