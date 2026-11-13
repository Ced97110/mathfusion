import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'un facteur $x - a$ par élément $a$', 'sujet', 'm')
for r, q in enumerate((2, 3, 5)):
    y = 54 - r * 14
    text(ax, 11, y, rf'$q = {q}$', 'encre', 'm')
    text(ax, 78, y, f'degré {q}', 'encre', 's')
    for i in range(q):
        role = 'varie' if (q == 5 and i == 3) else 'sujet'
        box(ax, 20 + i * 9.5, y - 4.5, 8, 9, role, r=0.3, label=rf'$x-{i}$' if q == 5 else None, size='s')
arrow(ax, (52.5, 17), (52.5, 21.5), 'varie')
text(ax, 52.5, 13, r'$x - 3$ vaut 0 en 3', 'varie', 's')
save(fig, '55-042')
