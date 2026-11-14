import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
yn = 12.0
f = numberline(ax, 14, 66, yn, -2, 2, 1)
text(ax, 44, 69, r'$M/N$ : les classes (droites)', 'sujet', 's')
text(ax, 80, 6, r'$\mathbb{Z}$', 'resultat', 'm')
for c in range(-2, 3):
    xc = f(c); yc = 42.0
    line(ax, [(xc - 6, yc - 3), (xc + 6, yc + 3)], 'sujet', lw=1.3)
    arrow(ax, (xc, yc - 8), (xc, yn + 4), 'fixe', lw=0.8)
    disc(ax, xc, yn, 1.2, 'resultat')
for (c, lab) in [(0, r'$(2\,;\,1)$'), (2, r'$(4\,;\,1)$')]:
    xc = f(c)
    disc(ax, xc, 42.0, 1.4, 'varie')
    text(ax, xc, 54, lab, 'varie', 's')
text(ax, 30, 3.5, r'$(x\,;\,y)\mapsto x-2y$', 'encre', 's')
text(ax, f(2) + 8, 30, r'$\mapsto 2$', 'varie', 's')
text(ax, f(0) + 8, 30, r'$\mapsto 0$', 'varie', 's')
save(fig, '57-149')
