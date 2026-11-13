import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
for i in range(1,12):
    ok=i in (1,5,7,11)
    box(ax,2.6+(i-1)*7.6,34,6.8,9,'resultat' if ok else 'fixe',label=str(i),size='s',r=0.5)
text(ax,44,26,'vert : pgcd avec 12 égal à 1','resultat','s')
text(ax,44,19,'gris : pgcd plus grand que 1','fixe','s')
text(ax,44,7,r'$\varphi(12)=4$','resultat','xl')
save(fig,'52-089')
