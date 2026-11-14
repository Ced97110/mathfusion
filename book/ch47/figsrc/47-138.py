import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def blocks(y, items):
    out = []
    for x, l, r in items:
        box(ax, x - 7, y - 5, 14, 10, r, label=l); out.append(x)
    return out
text(ax, 44, 76, r'$ab=g\,n_{1}\,h\,n_{2}$', 'encre', 'm')
blocks(52, [(14, r'$g$', 'fixe'), (34, r'$n_{1}$', 'varie'), (54, r'$h$', 'fixe'), (74, r'$n_{2}$', 'sujet')])
arrow(ax, (34, 58), (54, 58), 'varie', curve=-0.9)
text(ax, 44, 63.5, '', 'varie', 's')
text(ax, 44, 40, r'$n_{1}$ passe de l’autre côté de $h$', 'varie', 's')
blocks(26, [(14, r'$g$', 'fixe'), (34, r'$h$', 'fixe'), (54, r'$n_{3}$', 'varie'), (74, r'$n_{2}$', 'sujet')])
brace(ax, 44, 81, 19, 'sujet', r'dans $N$')
brace(ax, 7, 41, 19, 'fixe', r'$gh$')
save(fig, '47-138')
