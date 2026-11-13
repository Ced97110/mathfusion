import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 22
f = numberline(ax, 6, 78, y, -10, 5, 1, every=5, arrow_right=False)
line(ax, [(f(0), y - 4), (f(0), y + 24)], 'fixe', dash=True)
text(ax, f(0) + 1.5, y + 27, 'signe gardé', 'fixe', 's', ha='left')
for v, role in [(4, 'sujet'), (1, 'resultat'), (-9, 'autre'), (-1, 'resultat')]:
    disc(ax, f(v), y, 1.8, role)
    text(ax, f(v), y + 5, f'{v}'.replace('-', '−'), role, 'm', weight='bold')
arrow(ax, (f(4), y + 10), (f(1), y + 10), 'varie', curve=0.4)
text(ax, (f(4) + f(1)) / 2, y + 20, r'$\times c^2$, $c=\frac{1}{2}$', 'varie', 's')
arrow(ax, (f(-9), y + 10), (f(-1), y + 10), 'varie', curve=-0.2)
text(ax, (f(-9) + f(-1)) / 2, y + 20, r'$\times c^2$, $c=\frac{1}{3}$', 'varie', 's')
text(ax, 44, 2.5, r'valeur de $H(u,u)$', 'fixe', 's')
save(fig, '75-156')
