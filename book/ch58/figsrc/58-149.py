import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
n = lambda v: str(v).replace('-', '−')
t2 = lambda t: '(' + ', '.join(n(v) for v in t) + ')'
fams = [((3, 1), (1, 2), 'sujet', 40), ((5, 5), (7, 1), 'autre', 18)]
for v, w, role, y in fams:
    z = (0 * v[0] + 0 * w[0], 0 * v[1] + 0 * w[1])
    assert z == (0, 0)
    box(ax, 2, y, 22, 10, role, label=t2(v))
    text(ax, 27, y + 5, '+', 'encre', 'l')
    box(ax, 30, y, 22, 10, role, label=t2(w))
    arrow(ax, (54, y + 5), (62, y + 5), 'varie')
    text(ax, 58, y + 9.5, r'$0\times$', 'varie', 's')
    box(ax, 64, y, 22, 10, 'resultat', label=t2(z))
text(ax, 44, 57, 'tous les scalaires valent 0', 'varie', 'm')
text(ax, 44, 8, 'même résultat pour n’importe quels vecteurs', 'resultat', 's')
save(fig, '58-149')
