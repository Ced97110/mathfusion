import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 30
f = numberline(ax, 6, 76, y, 0, 120, step=60)
line(ax, [(f(0), y), (f(59), y)], 'resultat', lw=2.4)
for v, role in [(56, 'sujet'), (116, 'autre')]:
    disc(ax, f(v), y, 1.7, role)
    text(ax, f(v), y + 5, str(v), role, 'm', weight='bold')
    text(ax, f(v), y + 9.5, '(2, 0, 1)', role, 's')
arrow(ax, (f(56), y + 14), (f(116), y + 14), 'varie', curve=-0.3)
text(ax, (f(56) + f(116)) / 2, y + 22, 'écart de 60', 'varie', 's')
brace(ax, f(0), f(59), 20, 'resultat', label='un seul entier de 0 à 59')
save(fig, '52-245')
