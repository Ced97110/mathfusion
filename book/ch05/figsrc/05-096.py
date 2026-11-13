import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(98)
box(ax,2,52,84,40,'resultat',fill=True,lw=1.0)
text(ax,44,86,r'$a$ et $b$ non tous deux nuls','resultat','m',weight='bold')
yy=72
for x,s,r in [(14,r'$d$','resultat'),(24,'=','encre'),(34,r'$a$','sujet'),(44,r'$\times$','encre'),(54,r'$u$','varie'),(64,'+','encre'),(72,r'$b$','autre'),(80,r'$\times$','encre')]:
    pass
glyphs=[(10,r'$d$','resultat'),(19,'=','encre'),(28,r'$a$','sujet'),(36,r'$\times$','encre'),(44,r'$u$','varie'),(53,'+','encre'),(62,r'$b$','autre'),(70,r'$\times$','encre'),(78,r'$v$','varie')]
for x,s,r in glyphs: text(ax,x,yy,s,r,16)
text(ax,61,59,'entiers, parfois négatifs','varie','s')
box(ax,2,2,84,42,'limite',lw=1.0)
text(ax,44,38,r'$a=0$ et $b=0$ : pas de $d$','limite','m',weight='bold')
text(ax,44,24,r'$0\times u+0\times v=0$','limite','l')
text(ax,44,12,'jamais un PGCD positif','limite','m')
save(fig,'05-096')
