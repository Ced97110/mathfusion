import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 6, 82, 26, -9, 9, labels=False, arrow_right=False)
line(ax, [(f(0), 12), (f(0), 46)], 'sujet', lw=1.2, dash=True)
text(ax, f(0), 50, 'le pli passe par 0', 'sujet')
text(ax, f(0), 21, '0', 'sujet', weight='bold')
for v, r, y, c in [(3, 'autre', 31, 0.45), (8, 'fixe', 31, 0.3)]:
    for s in (v, -v):
        disc(ax, f(s), 26, 1.7, r)
        text(ax, f(s), 21, f'{s}'.replace('-', '−'), r)
arrow(ax, (f(-3), 28.5), (f(3), 28.5), 'autre', curve=-0.5, both=True)
arrow(ax, (f(-8), 28.5), (f(8), 28.5), 'fixe', curve=-0.35, both=True)
text(ax, f(0), 8, 'symétriques par rapport à 0', 'encre', 's')
save(fig, '13-034')
