import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(y, sym, sub, labs, role):
    text(ax, 16, y + 7, sym, role, 'l'); text(ax, 16, y - 0.5, sub, role, 's')
    for i, l in enumerate(labs):
        box(ax, 36 + i * 9.5, y, 8, 12, role, label=l, size='s', dash=(l == '⋯'), fill=(l != '⋯'))
row(60, r'$\mathbb{Q}$', 'infini', ['0', '1', '2', '3', '⋯'], 'autre')
row(36, r'$\mathbb{Z}/5\mathbb{Z}$', '5 éléments', ['0', '1', '2', '3', '4'], 'sujet')
row(12, r'$\mathbb{F}_4$', '4 éléments', ['0', '1', r'$\alpha$', r'$\alpha+1$'], 'sujet')
save(fig, '67-020')
