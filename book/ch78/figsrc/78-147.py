import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
rows=[('sujet',r'$Q(x)$',62),('autre',r'$Q(y)$',46),('resultat',r'$Q(xy)$',30)]
for role,lab,y in rows:
    text(ax,8,y+4,lab,role,'m')
    for i in range(8): box(ax,18+i*8.5,y,7.5,8,role)
text(ax,48,56,r'$\times$','encre','l')
text(ax,48,40,r'$=$','encre','l')
brace(ax,18,18+8*8.5-1,30,'resultat',label=r'8 carrés de coordonnées',down=True)
box(ax,6,2,76,10,'resultat',label=r'$Q(xy)=Q(x)\,Q(y)$')
save(fig,'78-147')
