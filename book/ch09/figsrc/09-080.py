import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 16, 76, 'De', 'sujet', 's', weight='bold'); text(ax, 72, 76, 'Vers', 'resultat', 's', weight='bold')
pairs = [(52, '12 %', '0,12', 'virgule 2 rangs à gauche', 'virgule 2 rangs à droite'),
         (22, r'$\frac{3}{5}$', '60 %', 'diviser, virgule à droite', 'sur 100, puis réduire')]
for y, a, b, up, dn in pairs:
    box(ax, 4, y, 24, 14, 'sujet', label=a, size='l')
    box(ax, 60, y, 24, 14, 'resultat', label=b, size='l')
    arrow(ax, (30, y + 10), (58, y + 10), 'varie')
    text(ax, 44, y + 14, up, 'varie', 's')
    arrow(ax, (58, y + 4), (30, y + 4), 'autre')
    text(ax, 44, y - 0.5, dn, 'autre', 's')
line(ax, [(4, 42), (84, 42)], 'fixe', lw=0.5)
arrow(ax, (4, 7), (16, 7), 'varie'); text(ax, 18, 7, 'geste', 'varie', 's', ha='left')
arrow(ax, (50, 7), (38, 7), 'autre'); text(ax, 52, 7, 'geste contraire', 'autre', 's', ha='left')
save(fig, '09-080')
