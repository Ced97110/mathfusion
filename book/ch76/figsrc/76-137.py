import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
box(ax,4,34,32,9,'sujet',label=r'$v_1=e_1+e_2$',size='m'); box(ax,4,20,32,9,'sujet',label=r'$v_2=e_2+e_3$',size='m')
text(ax,20,48,'un plan : deux flèches','sujet','s')
arrow(ax,(37,34),(46,28),'varie'); arrow(ax,(37,29),(46,28),'varie')
text(ax,42,41,r'$v_1\wedge v_2$','varie','m')
labs=[r'$e_{12}$',r'$e_{13}$',r'$e_{23}$']
for i,l in enumerate(labs):
    x=50+i*12
    box(ax,x,12,10,5,'fixe',label=l,size='s')
    box(ax,x,18,10,10,'resultat',label=None)
    text(ax,x+5,23,'1','resultat','m')
text(ax,68,48,'trois nombres','resultat','m')
brace(ax,50,82,30,'resultat',down=False)
save(fig,'76-137')
