import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
def dots(x, yc, k, role):
    return [(x, yc + ((k - 1) / 2 - i) * 7) for i in range(k)]
def row(yc, kl, kr, rl, rr, ll, lr, cap, role, links, both=False, caprole=None):
    box(ax, 8, yc - 12, 18, 24, rl); box(ax, 62, yc - 12, 18, 24, rr)
    text(ax, 4, yc, ll, rl, 'm'); text(ax, 84, yc, lr, rr, 'm')
    L, R = dots(17, yc, kl, rl), dots(71, yc, kr, rr)
    for p in L + R: disc(ax, p[0], p[1], 1.8, rl if p in L else rr)
    for a, b in links: arrow(ax, (L[a][0] + 2.5, L[a][1]), (R[b][0] - 2.5, R[b][1]), role, both=both)
    text(ax, 44, yc + 11, cap, caprole or role, 's')
row(84, 3, 3, 'sujet', 'autre', r'$S$', r'$T$', 'bijection : on peut revenir', 'resultat', [(0, 0), (1, 1), (2, 2)], both=True)
row(52, 2, 3, 'sujet', 'autre', r'$S$', r'$T$', 'injection : aller possible', 'varie', [(0, 0), (1, 1)])
row(20, 3, 2, 'autre', 'sujet', r'$T$', r'$S$', 'retour impossible', 'limite', [(0, 0), (1, 0), (2, 1)])
save(fig, '43-105')
