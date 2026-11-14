import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, 'sous-groupes (taille)', 'encre', 's')
text(ax, 66, 64, 'corps fixes', 'encre', 's')
left = [r'$G$ (4)', r'$\langle\sigma\rangle$ (2)', r'$\{1\}$ (1)']
right = [r'$\mathbb{Q}$', r'$\mathbb{Q}(\sqrt{3})$', r'$E$']
for i in range(3):
    c = 50 - 18 * i
    box(ax, 9, c - 6, 26, 12, 'sujet', label=left[i])
    box(ax, 53, c - 6, 26, 12, 'autre', label=right[i])
    arrow(ax, (36, c), (52, c), 'fixe')
arrow(ax, (4, 12), (4, 56), 'varie')
arrow(ax, (85, 56), (85, 12), 'varie')
text(ax, 44, 3, 'le groupe monte, le corps descend', 'varie', 's')
save(fig, '63-024')
