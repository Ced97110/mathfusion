import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [(r'$\langle\sigma\rangle$', r'$\mathbb{Q}(\sqrt{3})$', r'change $\sqrt{2}$, $\sqrt{6}$', r'garde $\sqrt{3}$', 'varie'),
        (r'$\langle\tau\rangle$', r'$\mathbb{Q}(\sqrt{2})$', r'change $\sqrt{3}$, $\sqrt{6}$', r'garde $\sqrt{2}$', 'autre'),
        (r'$\langle\sigma\tau\rangle$', r'$\mathbb{Q}(\sqrt{6})$', r'change $\sqrt{2}$, $\sqrt{3}$', r'garde $\sqrt{6}$', 'sujet')]
for i, (g, k, ch, ga, role) in enumerate(rows):
    c = 58 - 22 * i
    box(ax, 2, c - 8, 20, 16, role, label=g)
    box(ax, 66, c - 8, 20, 16, role, label=k)
    arrow(ax, (23, c), (65, c), role, both=True)
    text(ax, 44, c + 4.5, ch, 'fixe', 's')
    text(ax, 44, c - 4.5, ga, 'resultat', 's')
save(fig, '63-023')
