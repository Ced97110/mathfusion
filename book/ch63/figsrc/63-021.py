import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 26, 14, 12, 'fixe', label=r'$\mathbb{Q}$')
box(ax, 70, 26, 16, 12, 'fixe', label=r'$E$')
mids = [(52, r'$\mathbb{Q}(\sqrt{2})$'), (32, r'$\mathbb{Q}(\sqrt{3})$'), (12, r'$\mathbb{Q}(\sqrt{6})$')]
for cy, lab in mids:
    box(ax, 33, cy - 5.5, 24, 11, 'sujet', label=lab)
    arrow(ax, (17, 32), (32, cy), 'varie')
    arrow(ax, (58, cy), (69, 32), 'varie')
text(ax, 78, 20, r'$\sqrt{2}$ et $\sqrt{3}$', 'fixe', 's')
text(ax, 45, 3, r'$\sqrt{6}=\sqrt{2}\times\sqrt{3}$', 'resultat', 'm')
save(fig, '63-021')
