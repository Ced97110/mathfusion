import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw, ch, ytop = 14, 9, 62
H_left = {(0, 1)}
H_right = {(1, 1), (3, 1)}
def grid(x0, hset, bad, labels):
    for i in range(4):
        for j in range(2):
            if j == 0 and (i, j) in bad:
                role = 'limite'
            elif j == 0:
                role = 'sujet'
            elif (i, j) in hset:
                role = 'varie'
            else:
                role = 'fixe'
            lab = f'({i}, {j})' if (i, j) in labels else None
            box(ax, x0 + j * cw, ytop - (i + 1) * ch, cw, ch, role, label=lab, size='s', r=0.5)
ALL = {(i, j) for i in range(4) for j in range(2)}
grid(8, H_left, set(), ALL)
grid(52, H_right, {(2, 0)}, ALL)
text(ax, 22, 72, r'$H = \langle (0, 1)\rangle$', 'varie', 'm')
text(ax, 66, 72, r'$H = \langle (1, 1)\rangle$', 'varie', 'm')
text(ax, 22, 20, 'commun : (0, 0) seul', 'resultat', 's')
text(ax, 22, 14, 'somme directe', 'resultat', 's', weight='bold')
text(ax, 66, 20, 'commun : (0, 0), (2, 0)', 'limite', 's')
text(ax, 66, 14, 'somme non directe', 'limite', 's', weight='bold')
disc(ax, 8 + 2, 6, 2.0, 'sujet'); text(ax, 14, 6, r'$\langle g\rangle$, $g = (1, 0)$', 'sujet', 's', ha='left')
save(fig, '60-128')
