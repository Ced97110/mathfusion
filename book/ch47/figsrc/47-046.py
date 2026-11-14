import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,68,'la différence est-elle un multiple de 12 ?','fixe','s')
rows=[(r'$14\equiv 2$',r'$14-2=12=1\times 12$','resultat'),(r'$26\equiv 2$',r'$26-2=24=2\times 12$','resultat'),('14 et 3',r'$14-3=11$','limite')]
for i,(a,b,role) in enumerate(rows):
    y=44-i*22+10
    box(ax,3,y-8,26,16,role,label=a,size='s'); arrow(ax,(30,y),(34,y),role)
    box(ax,35,y-8,50,16,role,label=b,size='s')
text(ax,44,5,'différence multiple de 12 : congrus','resultat','s') if False else None
save(fig,'47-046')
