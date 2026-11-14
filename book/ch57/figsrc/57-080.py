import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 27, 52, 'coefficient', 'fixe', 's')
text(ax, 68, 52, 'sa règle', 'fixe', 's')
rows = [(34, 'règle 2', r'$5=3+2$', 'tripler + doubler'), (20, 'règle 3', r'$6=3\times 2$', 'tripler ∘ doubler'),
        (6, 'règle 4', '1', 'ne rien changer')]
for y, tag, l, r in rows:
    text(ax, 2, y + 4.5, tag, 'fixe', 's', ha='left')
    box(ax, 15, y, 24, 9, 'varie', label=l)
    arrow(ax, (41, y + 4.5), (49, y + 4.5), 'sujet')
    box(ax, 51, y, 35, 9, 'sujet', label=r)
save(fig, '57-080')
