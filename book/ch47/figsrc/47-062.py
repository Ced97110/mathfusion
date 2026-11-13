import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
cx=[16,44,72]; ys={1:52,2:40,3:28}
heads=['départ',r'après $(1\,2)$',r'après $(1\,3)$']
for c,h in zip(cx,heads): text(ax,c,62,h,'encre','s')
roles=['sujet','fixe','resultat']
for c,r in zip(cx,roles):
    for n in (1,2,3): disc(ax,c,ys[n],3,r,label=str(n),size='s')
m1={1:2,2:1,3:3}; m2={1:3,2:2,3:1}
for n in (1,2,3):
    arrow(ax,(cx[0]+3.3,ys[n]),(cx[1]-3.3,ys[m1[n]]),'varie')
    arrow(ax,(cx[1]+3.3,ys[n]),(cx[2]-3.3,ys[m2[n]]),'sujet')
text(ax,44,16,r'$(1\,3)(1\,2)=(1\,2\,3)$','resultat','l')
text(ax,44,7,r'$(1\,3)K=\{(1\,3),(1\,2\,3)\}$','encre','s')
save(fig,'47-062')
