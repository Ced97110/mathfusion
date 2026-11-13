import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,52,'chaque chiffre × sa case','varie','s')
heads=['milliers : 1 000','centaines : 100','dizaines : 10','unités : 1']
digs=['4','3','2','9']; res=['4 000','300','20','9']
for c,h,d,r in zip([12.5,33.5,54.5,75.5],heads,digs,res):
    box(ax,c-10,42,20,6,'fixe',label=h,size='s')
    box(ax,c-6,30,12,9,'sujet',label=d,size='l')
    arrow(ax,(c,30),(c,22),'varie')
    box(ax,c-9,15,18,7,'resultat',label=r,size='m')
brace(ax,3.5,84.5,13,'resultat','somme : 4 329',down=True,size='m')
save(fig,'01-062')
