import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
# grande règle : pas de 7 mm
f=numberline(ax,8,78,58,0,10,labels=False,arrow_right=False,role='fixe')
arrow(ax,(78,58),(84,58),'fixe',lw=0.9)
for v in (7,10): text(ax,f(v),55,f'{v}','fixe','s')
brace(ax,f(0),f(1),60,'sujet','1 pas',down=False)
brace(ax,f(7),f(10),52,'resultat','3 pas',down=True)
# petite règle : pas de 4 mm
g=numberline(ax,8,48,34,0,10,labels=False,arrow_right=False,role='fixe')
arrow(ax,(48,34),(52,34),'fixe',lw=0.9)
for v in (7,10): text(ax,g(v),31,f'{v}','fixe','s')
brace(ax,g(0),g(1),36,'sujet','1 pas',down=False)
brace(ax,g(7),g(10),28,'resultat','3 pas',down=True)
# écarts inégaux
xs=[8,11,17,20,29,33,35,44,47,58,62]
line(ax,[(8,12),(62,12)],'limite')
for x in xs: line(ax,[(x,10.8),(x,13.2)],'limite',lw=0.8)
text(ax,xs[7],9,'7','limite','s'); text(ax,xs[10],9,'10','limite','s')
brace(ax,xs[7],xs[10],14.5,'limite','3 pas ?',down=False)
text(ax,75,19,'écarts inégaux','limite','s')
save(fig,'01-013')
