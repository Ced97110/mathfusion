import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,15,72,'exemple','autre','l'); text(ax,44,72,'propriété','sujet','l'); text(ax,72,72,'convention','autre','l')
ys=[40+4.5*j for j in range(5)]
for i in range(5):
    for y in ys:
        disc(ax,6+4.5*i,y,0.9,'fixe')
disc(ax,15,58,1.4,'autre')
text(ax,15,63,'18 et 34','autre','s')
for i in range(5):
    for y in ys:
        disc(ax,35+4.5*i,y,1.4,'sujet')
box(ax,32,37,24,24,'sujet',fill=False)
line(ax,[(72,38),(72,60)],'fixe')
for y in (38,49,60): line(ax,[(71,y),(73,y)],'fixe')
text(ax,79,38,'16 000','fixe','s'); text(ax,79,60,'17 000','fixe','s')
disc(ax,72,49,1.2,'autre'); text(ax,64,49,'16 500','autre','s')
arrow(ax,(72,50.5),(72,58.5),'varie',lw=1.4)
text(ax,15,33,'vérifié une fois','autre','s'); text(ax,44,33,'vrai pour tous','sujet','s'); text(ax,72,33,'arrondi vers le haut','autre','s')
text(ax,44,28,'à prouver','sujet','s'); text(ax,72,28,'un choix','autre','s')
brace(ax,6,53,22,'fixe',label='diffère par la portée',down=True)
brace(ax,35,85,11,'fixe',label="diffère par l'origine",down=True)
save(fig,'02-056')
