import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,74,r'$y = 5 - x$ : chaque $x$ donne un $y$','encre','s')
for i,(a,b) in enumerate([(0,5),(1,4),(2,3)]):
    y=54-i*14
    box(ax,4,y,22,9,'sujet',label=f'$x = {a}$'); arrow(ax,(27,y+4.5),(35,y+4.5),'varie')
    box(ax,36,y,22,9,'autre',label=f'$y = {b}$'); arrow(ax,(59,y+4.5),(64,y+4.5),'varie')
    box(ax,65,y,21,9,'resultat',label='2 tickets OK',size='s')
text(ax,44,19,'…','fixe','l')
box(ax,4,2,80,11,'resultat',label=r'$10 = 10$ vrai pour tout $x$ : infinité')
save(fig,'24-072')
