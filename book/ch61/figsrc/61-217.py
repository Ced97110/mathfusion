import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
steps = [('sujet', 'réel constructible', None), ('varie', 'tour quadratique sur ℚ', None),
         ('varie', r'degré $2^k$ : fini', r'$\sqrt{2}$ : $2^1$'), ('varie', 'annule un polynôme', r'$x^2-2=0$'),
         ('resultat', 'algébrique sur ℚ', None)]
h, g = 9, 5.5
for i, (r, t, tag) in enumerate(steps):
    y = 74 - 4 - h - i * (h + g)
    box(ax, 4, y, 54, h, r, label=t, size='s', weight='bold' if i in (0, 4) else 'normal')
    if tag: text(ax, 62, y + h / 2, tag, r, 's', ha='left')
    if i: arrow(ax, (31, y + h + g), (31, y + h), 'fixe')
save(fig, '61-217')
