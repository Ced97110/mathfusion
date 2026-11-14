import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def blk(y, n, g, txt):
    text(ax, 2, y + 16, txt, 'encre', 'm', ha='left')
    for j, lab in enumerate(['générateurs', f'premiers avec {n}']):
        yy = y + 8 - j * 8
        text(ax, 2, yy + 2.1, lab, 'fixe', 's', ha='left')
        for k in range(1, n + 1):
            ok = k in g
            box(ax, 26 + (k - 1) * 4.8, yy, 4.2, 4.2, 'resultat' if ok else 'fixe', fill=ok, dash=not ok, r=0.5)
    for k in g: line(ax, [(28.1 + (k - 1) * 4.8, y + 8), (28.1 + (k - 1) * 4.8, y + 4.2)], 'resultat', lw=0.6)
    text(ax, 12, y + 6, '=', 'encre', 'l')
blk(50, 12, [1, 5, 7, 11], r'horloge à 12 heures : $\varphi$(12) = 4')
blk(14, 6, [1, 5], r'horloge à 6 heures : $\varphi$(6) = 2')
save(fig, '46-133')
