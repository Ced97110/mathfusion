import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
items = [('b', r'$h$', 'varie', 8), ('t', '=', None, 4), ('b', '20', 'fixe', 9), ('t', 'sin', None, 6),
         ('b', r'$\pi/4$', 'fixe', 10), ('t', '(', None, 3), ('b', r'$t$', 'varie', 7), ('t', '−', None, 4),
         ('b', '2', 'fixe', 7), ('t', ')) +', None, 8), ('b', '22', 'fixe', 9)]
gap = 0.6
total = sum(w for *_, w in items) + gap * (len(items) - 1)
x = (W - total) / 2
for kind, s, role, w in items:
    if kind == 'b': box(ax, x, 28, w, 9, role, label=s, size='m')
    else: text(ax, x + w / 2, 32.5, s, 'encre', 'l')
    x += w + gap
box(ax, 4, 12, 38, 9, 'varie', label=r'change : $h$ et $t$', size='s')
box(ax, 46, 12, 38, 9, 'fixe', label='fixes : ils décrivent la roue', size='s')
text(ax, 44, 3.5, 'même formule pour tous les temps', 'resultat', 's')
save(fig, '30-134')
