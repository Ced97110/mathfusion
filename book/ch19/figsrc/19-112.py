import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
gx = lambda x: 12 + x * 16; gy = lambda y: 8 + y * 8
line(ax, [(gx(-0.5), gy(0)), (gx(2.5), gy(6))], 'sujet', lw=1.3)
line(ax, [(gx(-0.5), gy(4.5)), (gx(4), gy(0))], 'autre', lw=1.3)
disc(ax, gx(1), gy(3), 1.5, 'resultat')
text(ax, gx(1) + 3, gy(3) + 4, r'$(1,\,3)$', 'resultat', 'm', ha='left')
text(ax, 22, gy(5.6), 'pente 2', 'sujet', 's'); text(ax, 70, gy(0.9), 'pente −1', 'autre', 's')
text(ax, 44, 62, 'un seul point commun', 'resultat', 'm')
save(fig, '19-112')
