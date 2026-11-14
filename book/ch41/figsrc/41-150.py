import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# 0,5 mm par unité : force 50 N -> 25 mm ; déplacement 100 m -> 50 mm
x0, y0 = 8, 14
arrow(ax, (x0, y0), (x0 + 50, y0), 'autre', lw=1.4)
arrow(ax, (x0, y0), (x0, y0 + 25), 'sujet', lw=1.4)
line(ax, [(x0 + 3, y0), (x0 + 3, y0 + 3), (x0, y0 + 3)], 'fixe', lw=0.6)
text(ax, x0 + 25, y0 - 5, 'déplacement : 100 m', 'autre', 's')
text(ax, x0 + 2, y0 + 30, 'force : 50 N', 'sujet', 's', ha='left')
text(ax, x0 + 9.5, y0 + 6.5, '90°', 'fixe', 's')
box(ax, 54, 38, 30, 24, 'resultat')
text(ax, 69, 56, r'$50\times 100\times 0$', 'resultat', 's')
text(ax, 69, 49, r'$\cos 90^\circ = 0$', 'resultat', 's')
text(ax, 69, 42.5, 'travail : 0 J', 'resultat', 's', weight='bold')
save(fig, '41-150')
