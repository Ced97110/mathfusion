import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for cx, role, sym, nom in [(20, 'sujet', r'$U$', 'Judson'), (68, 'autre', r'$S$', 'Jacobson')]:
    box(ax, cx - 16, 14, 32, 34, role, lw=1.0)
    text(ax, cx, 42, sym, role, 'l', weight='bold')
    for dx in (-8, 0, 8):
        disc(ax, cx + dx, 30, 2.5, 'fixe')
    box(ax, cx - 12, 25, 16, 10, 'fixe', fill=False, dash=True)
    text(ax, cx, 19, 'partie', 'fixe', 's')
    text(ax, cx, 8, nom, role, 'm')
text(ax, 44, 31, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 55, 'le même tout, deux lettres', 'encre', 'm')
save(fig, '42-130')
