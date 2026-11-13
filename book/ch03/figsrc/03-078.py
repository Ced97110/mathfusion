import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,39.8,55,r'$a \times$','encre','l',ha='right')
text(ax,47.3,55,r'$(b + c)$','encre','l')
box(ax,41.0,52.6,12.6,4.8,'resultat',fill=False,lw=0.9)
arrow(ax,(47.3,52.3),(44,36.6),'resultat')
text(ax,50,45,'largeur avant la coupe','resultat','s',ha='left')
for r in range(3):
    for c in range(6):
        box(ax,29+5*c,14+5*r,5,5,'sujet' if c<4 else 'varie',r=0.3,lw=0.5)
brace(ax,29,59,30.5,'resultat',label=r'$b + c$ = 6',down=False,size='m')
brace(ax,29,49,12.5,'sujet',label=r'$b$ = 4',down=True,size='s')
brace(ax,49.3,59,12.5,'varie',label=r'$c$ = 2',down=True,size='s')
line(ax,[(26.5,14),(26.5,29)],'fixe'); line(ax,[(25.8,14),(27.2,14)],'fixe'); line(ax,[(25.8,29),(27.2,29)],'fixe')
text(ax,25,21.5,r'$a$ = 3','encre','s',ha='right')
text(ax,73.5,26.5,r'somme entière × $a$','encre','s')
text(ax,73.5,21.5,'3 × 6 = 18','resultat','m')
save(fig,'03-078')
