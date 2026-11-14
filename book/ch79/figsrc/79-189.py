import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
o = (26, 34); u = 13
I = lambda x, y, z: iso(x, y, z, o, u)
poly(ax, [I(-1,-1,0), I(1,-1,0), I(1,1,0), I(-1,1,0)], 'sujet', fill=False, lw=1.4)
poly(ax, [I(-1,0,-1), I(1,0,-1), I(1,0,1), I(-1,0,1)], 'autre', fill=False, lw=1.4)
line(ax, [I(-1,0,0), I(1,0,0)], 'resultat', lw=2.6)
text(ax, *I(-1,1.15,0), r'$U$', 'sujet', 'l')
text(ax, I(1,0,1)[0]+3, I(1,0,1)[1]+1, r'$W$', 'autre', 'l')
text(ax, 62, 56, r'$\dim U=2$', 'sujet', 's'); text(ax, 62, 47, r'$\dim W=2$', 'autre', 's')
text(ax, 62, 36, r'$\dim(U+W)=3$', 'fixe', 's'); text(ax, 62, 27, r'$\dim(U\cap W)=1$', 'resultat', 's')
text(ax, 62, 14, r'$3+1=2+2$', 'encre', 'l', weight='bold')
save(fig, '79-189')
