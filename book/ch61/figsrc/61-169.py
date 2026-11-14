import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 22, 66, 'tour quadratique', 'resultat', 's'); text(ax, 66, 66, 'degré 3 : pas quadratique', 'limite', 's')
L = [r'$\mathbb{Q}$', r'$\mathbb{Q}(\sqrt{2})$', r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$']
for i, l in enumerate(L):
    box(ax, 3, 4 + 20 * i, 38, 10, 'fixe' if i == 0 else 'resultat', label=l)
    if i: arrow(ax, (12, 14 + 20 * (i - 1)), (12, 4 + 20 * i), 'varie'); text(ax, 17, 14 + 20 * (i - 1) + 3, 'degré 2', 'varie', 's', ha='left')
box(ax, 47, 4, 38, 10, 'fixe', label=r'$\mathbb{Q}$')
box(ax, 47, 24, 38, 10, 'limite', label=r'$\mathbb{Q}(\sqrt[3]{2})$')
arrow(ax, (56, 14), (56, 24), 'limite'); text(ax, 61, 19, 'degré 3', 'limite', 's', ha='left')
save(fig, '61-169')
