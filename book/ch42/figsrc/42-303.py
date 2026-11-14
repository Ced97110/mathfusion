import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
box(ax,3,14,30,40,'autre'); box(ax,55,14,30,40,'sujet')
for j in range(3):
    for i in range(2):
        y=46-j*12; xl=12+i*12; xr=64+i*12
        disc(ax,xl,y,1.7,'autre'); disc(ax,xr,y,1.7,'sujet')
        line(ax,[(xl+2.2,y),(xr-2.2,y)] if False else [(xl+2.2,y+(0 if i else 0)),(xl+2.2,y)],'fixe')
for j in range(3):
    y=46-j*12
    arrow(ax,(35,y),(53,y),'varie',lw=0.8)
text(ax,18,60,'un groupe\nde 6 éléments','autre','s')
text(ax,70,60,'bijections de 3 éléments\n: 6 éléments','sujet','s')
text(ax,44,6,'isomorphisme : même structure','varie','s')
save(fig,'42-303')
