import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
rows = [(60, 'sujet', r'$[e,x]=x$ pour tout $x$', 'départ'),
        (41, 'varie', r'on prend $x=e$ : $[e,e]=e$', 'étape qui compte'),
        (22, 'resultat', r'mais $[e,e]=0$, donc $e=0$', 'règle $[x,x]=0$'),
        (3, 'resultat', r'$x=[0,x]=0$ pour tout $x$', 'arrivée')]
for i, (y, role, lab, side) in enumerate(rows):
    box(ax, 2, y, 58, 13, role, label=lab)
    text(ax, 63, y + 6.5, side, 'encre', 's', ha='left')
    if i: arrow(ax, (31, y + 19), (31, y + 13), 'fixe')
save(fig, '78-050')
