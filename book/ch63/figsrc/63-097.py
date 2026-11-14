import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
labs = ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$']

def row(y, n, cap, crole):
    box(ax, 12, y, 66, 22, 'sujet')
    for i, l in enumerate(labs):
        disc(ax, 22 + i * 15, y + 11, 4.5, 'encre', label=l, size='s')
    x_end = 22 + 15 * (n - 1) + 6.5
    box(ax, 15, y + 4, x_end - 15, 14, 'autre', fill=False, lw=1.6)
    text(ax, 6, y + 18, r'$G$', 'sujet', 'm')
    text(ax, 6, y + 8, r'$H$', 'autre', 'm')
    text(ax, 44, y + 29, cap, crole, 'm')

row(52, 4, r'$|H| = [E:\mathbb{Q}] = 4$ : $H = G$', 'resultat')
row(8, 2, r'$|H| = 2 \neq 4$ : $H \neq G$', 'limite')
save(fig, '63-097')
