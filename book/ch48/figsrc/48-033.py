import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 4, 12, 30, 36, 'sujet')
text(ax, 19, 43, r'paquet $aK$', 'sujet', 's')
ys = [34, 28, 22]
for y, n in zip(ys, ['3', '7', '11']):
    disc(ax, 14, y, 3.4, 'sujet', label=n, size='s')
    arrow(ax, (17.6, y), (63.6, 30 + (y - 28) * 0.35), 'fixe', lw=0.7)
text(ax, 48, 17, r'$f$', 'fixe', 'm')
disc(ax, 70, 30, 6, 'resultat', label='3', size='m')
text(ax, 70, 19, 'position 3', 'resultat', 's')
arrow(ax, (19, 48.8), (68, 36.8), 'varie', lw=1.3, curve=-0.3)
text(ax, 44, 58, r'$\bar{f}$', 'varie', 'l')
text(ax, 44, 6, r'$\bar{f}(aK) = f(a)$', 'encre', 'l')
save(fig, '48-033')
