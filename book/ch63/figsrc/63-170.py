import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
cw, ch = 11, 9
def bar(x, y, labels, role):
    for i, s in enumerate(labels):
        box(ax, x + i * cw, y, cw, ch, role, label=s, size='s')
    return x + len(labels) * cw
# Q(sqrt5) : base 1, sqrt5
x0 = 30
text(ax, 4, 69.5, r'$\mathbb{Q}(\sqrt{5})$', 'autre', 'm', ha='left')
bar(x0, 65, ['1', r'$\sqrt{5}$'], 'autre')
text(ax, x0 + 2 * cw + 3, 69.5, 'degré 2', 'autre', 's', ha='left')
# K : base 1, s
text(ax, 4, 45.5, r'$K$', 'sujet', 'm', ha='left')
bar(x0, 41, ['1', r'$s$'], 'sujet')
text(ax, x0 + 2 * cw + 3, 45.5, 'degré 2', 'sujet', 's', ha='left')
# E : 4 cases
text(ax, 4, 21.5, r'$\mathbb{Q}(\omega)$', 'fixe', 'm', ha='left')
bar(x0, 17, ['', '', '', ''], 'fixe')
text(ax, x0 + 4 * cw + 3, 21.5, 'degré 4', 'fixe', 's', ha='left')
# flèche d'inclusion : sqrt5 = 2s + 1 est dans K
arrow(ax, (x0 + cw * 1.5, 64), (x0 + cw * 1.5, 51), 'varie')
text(ax, x0 + cw * 1.5 + 2, 57.5, r'$\sqrt{5} = 2s + 1$', 'varie', 's', ha='left')
text(ax, x0 + cw * 0.5 - 4, 57.5, r'$=$', 'resultat', 'xl')
text(ax, 44, 33, r'$\neq$', 'limite', 'xl')
text(ax, 44, 8, r'$K = \mathbb{Q}(\sqrt{5})$ : même degré', 'resultat', 'm')
save(fig, '63-170')
