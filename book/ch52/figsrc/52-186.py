import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$m\,s = 4 \times 4 = 16$', 'sujet', 'l')
box(ax, 8, 31, 32, 19, 'fixe', fill=False, dash=True)
for i in range(16):
    r, c = divmod(i, 5)
    role = 'fixe' if r < 3 else 'resultat'
    disc(ax, 13 + c * 6, 46 - r * 6, 2.2, role)
text(ax, 62, 40, '3 paquets de 5', 'fixe', 's')
text(ax, 62, 28, 'reste 1', 'resultat', 's')
arrow(ax, (50, 28), (20, 28), 'resultat')
text(ax, 44, 14, r'$m\,s \equiv 1 \ (\mathrm{mod}\ 5)$', 'sujet', 'm')
text(ax, 44, 6, 's = 4 : inverse de 4 par 5', 'varie', 's')
save(fig, '52-186')
