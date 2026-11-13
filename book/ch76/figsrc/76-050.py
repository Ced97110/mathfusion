import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for cA, lab, vq, rq, cap in [(50, '(1 ; 1)', '1', 'resultat', r'dans $S$'), (16, '(1 ; 0)', '0', 'limite', r'hors de $S$')]:
    box(ax, 3, cA - 6, 26, 12, 'fixe', label=lab)
    text(ax, 16, cA - 11, cap, 'fixe', 's')
    arrow(ax, (30, cA + 2), (53, cA + 8), 'sujet'); arrow(ax, (30, cA - 2), (53, cA - 8), 'autre')
    box(ax, 54, cA + 3, 30, 10, 'resultat', label=r'$p$ donne 1')
    box(ax, 54, cA - 13, 30, 10, rq, label=r'$q$ donne ' + vq)
save(fig, '76-050')
