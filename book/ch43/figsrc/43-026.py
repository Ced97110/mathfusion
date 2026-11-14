import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'si $a\ E\ b$ et $b\ E\ c$, alors $a\ E\ c$', 'sujet', 's')
for y, name, ns, ok in ((50, 'même chiffre des unités', ('3', '13', '23'), True),
                        (14, 'distance au plus 1', ('0', '1', '2'), False)):
    text(ax, 3, y + 20, name, 'fixe', 's', ha='left')
    xs = (16, 44, 72)
    for x, n in zip(xs, ns): disc(ax, x, y, 5, 'sujet', label=n)
    arrow(ax, (xs[0]+5.5, y), (xs[1]-5.5, y), 'resultat')
    arrow(ax, (xs[1]+5.5, y), (xs[2]-5.5, y), 'resultat')
    role = 'resultat' if ok else 'limite'
    arrow(ax, (xs[0], y+5.5), (xs[2], y+5.5), role, curve=-0.45)
    text(ax, 44, y + 19.5, 'oui' if ok else 'non', role, 's')
save(fig, '43-026')
