import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
rows = [(56, 'monôme\n1 terme', [(r'$4x^2$', 'fixe')]),
        (36, 'binôme\n2 termes', [(r'$4x^2$', 'sujet'), (r'$-\,7x$', 'varie')]),
        (16, 'trinôme\n3 termes', [(r'$4x^2$', 'fixe'), (r'$-\,7x$', 'fixe'), (r'$+\,3$', 'fixe')])]
for y, lab, chips in rows:
    text(ax, 3, y + 5, lab, 'sujet' if 'binôme' in lab else 'fixe', 's', ha='left')
    for i, (t, r) in enumerate(chips): box(ax, 28 + i * 19, y, 17, 10, r, label=t)
text(ax, 44, 6, r'le signe $-$ reste collé à $7x$', 'varie', 's')
save(fig, '15-059')
