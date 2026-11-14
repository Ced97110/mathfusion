import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'des noms, pas des nombres', 'fixe', 's')
rows = [(r'$\sigma$', r'$\sqrt{2}\mapsto-\sqrt{2}$ ; $\sqrt{3}\mapsto\sqrt{3}$'),
        (r'$\tau$', r'$\sqrt{2}\mapsto\sqrt{2}$ ; $\sqrt{3}\mapsto-\sqrt{3}$'),
        (r'$\eta$', r'$\sqrt{2}\mapsto-\sqrt{2}$ ; $\sqrt{3}\mapsto-\sqrt{3}$')]
for i, (n, d) in enumerate(rows):
    y = 48 - 14 * i
    disc(ax, 12, y, 5, 'sujet', label=n, size='l')
    arrow(ax, (18, y), (23, y), 'fixe')
    text(ax, 25, y, d, 'encre', 's', ha='left')
text(ax, 44, 7, r'$\eta(a)$ : l’image de $a$ par $\eta$', 'sujet', 'm')
save(fig, '63-037')
