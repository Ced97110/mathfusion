import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def diamond(cx, labels, role):
    P = {'b': (cx, 16, labels[0]), 'l': (cx - 11, 40, labels[1]), 'r': (cx + 11, 40, labels[2]), 't': (cx, 64, labels[3])}
    for a, b in [('b', 'l'), ('b', 'r'), ('l', 't'), ('r', 't')]:
        line(ax, [(P[a][0], P[a][1] + 4), (P[b][0], P[b][1] - 4)], 'fixe', lw=1.0)
    for x, y, s in P.values():
        box(ax, x - 8, y - 4, 16, 8, role, label=s, size='s')
diamond(21, ['{0, 6}', r'$\langle 3\rangle$', r'$\langle 2\rangle$', r'$\mathbb{Z}/12\mathbb{Z}$'], 'sujet')
diamond(68, [r'$\{\bar 0\}$', r'$\langle\bar 3\rangle$', r'$\langle\bar 2\rangle$', r'$\mathbb{Z}/6\mathbb{Z}$'], 'autre')
text(ax, 21, 76, r'contiennent $K$', 'sujet', 's')
text(ax, 68, 76, r'sous-groupes de $G/K$', 'autre', 's')
text(ax, 44, 40, r'$=$', 'resultat', 'xl')
text(ax, 44, 28, 'même forme', 'resultat', 's')
save(fig, '48-099')
