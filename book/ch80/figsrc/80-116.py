import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,20,60,'avant','sujet','s'); text(ax,68,60,'après','resultat','s')
box(ax,3,24,34,30,'sujet',label=None); box(ax,51,24,34,30,'resultat',label=None)
for i,(a,b) in enumerate([('$a=2$',"$a'$"),('$b=3$',"$b'$"),('$a+b=5$',"$(a+b)'$")]):
    y=47-i*9; text(ax,20,y,a,'sujet','s'); text(ax,68,y,b,'resultat','s')
arrow(ax,(37,39),(51,39),'varie'); text(ax,44,44,'iso.','varie','s')
box(ax,6,4,76,12,'resultat',label="$(a+b)'=a'+b'$ déduit",size='m')
save(fig,'80-116')
