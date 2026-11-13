import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
for c,s in zip([12,33,54,75],['1 704 €','1 705 €','1 706 €','1 707 €']):
    text(ax,c,48,s,'encre','m'); box(ax,c-9.5,32,19,8,'fixe',label='426 places',size='s')
brace(ax,2.5,84.5,30,'fixe',label='même quotient : 426',down=True,size='s')
for x in [33,52.5,55.5,72,75,78]: disc(ax,x,19.5,1.2,'varie')
for c,k in zip([12,33,54,75],range(4)): text(ax,c,13,f'reste {k}','varie','s')
box(ax,48,16.5,12,6,'resultat',fill=False,dash=True)
brace(ax,2.5,84.5,10,'varie',label='le reste les distingue',down=True,size='s')
save(fig,'03-086')
