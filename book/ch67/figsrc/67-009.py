import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 70, r'$\mathbb{F}_4$', 'sujet', 26)
text(ax, 28, 56, 'un corps', 'sujet', 's')
text(ax, 62, 56, '4 éléments', 'sujet', 's')
arrow(ax, (44, 62), (44, 47), 'sujet')
box(ax, 4, 28, 80, 19, 'sujet', fill=False, dash=True)
for i, l in enumerate(['0', '1', r'$\alpha$', r'$\alpha+1$']):
    box(ax, 8 + i * 19.5, 31, 16, 12, 'sujet', label=l)
text(ax, 44, 16, r'$\alpha\in\mathbb{F}_4$', 'sujet', 'l')
text(ax, 44, 7, r'$\alpha$ est un élément de $\mathbb{F}_4$', 'encre', 's')
save(fig, '67-009')
