import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
box(ax,3,62,40,11,'fixe',label='1 · énoncer\n'+r'$E(n)$ : $n$ < 5',size='s')
box(ax,3,48,40,11,'resultat',label='2 · vérifier le départ\n0 < 5 : vrai',size='s')
box(ax,3,34,40,11,'fixe',label='3 · supposer\n'+r'$E(k)$ : $k$ < 5',size='s')
box(ax,3,20,40,11,'limite',lw=1.4,label='4 · montrer le suivant\n'+r'on obtient $k+1$ < 6 seulement',size='s')
box(ax,3,6,40,11,'fixe',fill=False,dash=True,label='5 · conclure\nbloqué',size='s')
for y in (62,48,34,20): arrow(ax,(23,y),(23,y-3),'fixe')
arrow(ax,(43,25.5),(49.5,25.5),'limite',lw=1.4)
line(ax,[(50,25.5),(82,25.5)],'fixe'); arrow(ax,(82,25.5),(85.5,25.5),'fixe')
f=lambda v: 52+5*v
for v in range(7):
    line(ax,[(f(v),24.3),(f(v),26.7)],'fixe',lw=0.8); text(ax,f(v),22.1,str(v),'fixe','s')
box(ax,52,31.5,24,2,'resultat',r=0.5)
text(ax,64,36.5,'< 5','resultat','s')
disc(ax,72,25.5,1.5,'varie'); disc(ax,77,25.5,1.5,'limite')
arrow(ax,(72,27.2),(77,27.2),'limite',curve=-0.9,lw=1.3)
text(ax,67,15,'4 donne 5 : pas < 5','limite','s')
save(fig,'01-142')
