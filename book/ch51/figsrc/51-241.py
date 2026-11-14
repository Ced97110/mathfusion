import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def rows(ytop, ybot, n, role_d, role_p, dots):
    for k in range(n):
        x = 30 + 9 * k
        disc(ax, x, ytop, 2.6, role_d)
        box(ax, x - 2.8, ybot - 2.8, 5.6, 5.6, role_p)
        arrow(ax, (x, ytop - 2.6), (x, ybot + 2.8), 'varie')
    if dots:
        x = 30 + 9 * n
        text(ax, x, ytop, '…', role_d, 'l'); text(ax, x, ybot, '…', role_p, 'l')
text(ax, 2, 68, 'Fini', 'resultat', 'l', ha='left', weight='bold')
text(ax, 2, 58, 'départs', 'sujet', 'm', ha='left'); text(ax, 2, 47, 'places', 'sujet', 'm', ha='left')
rows(58, 47, 6, 'sujet', 'sujet', False)
brace(ax, 27.2, 75.8, 42.5, 'resultat', label=r'$m = 6$', size='m')
text(ax, 2, 31, 'Infini', 'limite', 'l', ha='left', weight='bold')
text(ax, 2, 22, 'départs', 'sujet', 'm', ha='left'); text(ax, 2, 11, 'places', 'sujet', 'm', ha='left')
rows(22, 11, 5, 'sujet', 'sujet', True)
text(ax, 54, 3.2, r'pas de nombre $m$ à compter', 'limite', 'm')
save(fig, '51-241')
