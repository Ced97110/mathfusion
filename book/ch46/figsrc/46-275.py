import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def row(y,titre,card,ords):
    text(ax,4,y+14,titre,'fixe','s',ha='left')
    text(ax,84,y+14,card,'sujet','m',ha='right')
    n=len(ords); w_=11; gap=2; x=4
    for o in ords:
        box(ax,x,y,w_,9,'resultat',label=str(o)); x+=w_+gap
    return
row(34,'Mélanges de 3 cartes',r'$|G|=6$',[1,2,3])
row(8,'Racines douzièmes',r'$|G|=12$',[1,2,3,4,6,12])
text(ax,44,57,r'chaque ordre $o(a)$ divise $|G|$','encre','m')
save(fig,'46-275')
