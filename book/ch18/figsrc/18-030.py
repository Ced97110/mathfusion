import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
steps=[('lire : 6 × 4 + 6 × 7','fixe'),('le 6 devant : 6 × ( … )','varie'),('chaque terme ÷ 6 : 4 et 7','varie'),('on obtient 6 × (4 + 7)','resultat')]
for i,(s,r) in enumerate(steps):
    y=52-16*i
    disc(ax,6,y+5.5,3.2,r,label=str(i+1),size='m')
    box(ax,12,y,72,11,r,label=s,size='m')
    if i<3: arrow(ax,(48,y),(48,y-5),'fixe')
save(fig,'18-030')
