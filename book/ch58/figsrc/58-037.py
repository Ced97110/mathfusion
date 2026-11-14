import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# la liste (5, 4) : deux cases ; la condition (2+3) fois la liste se vérifie dans chaque case
v = (5, 4)
for x in v:
    assert 5 * x == 2 * x + 3 * x
text(ax, 44, 61, r'condition : $(2+3)\times(5,\,4)$', 'encre', 'm', weight='bold')
text(ax, 44, 55, r'$= 2\times(5,\,4) + 3\times(5,\,4)$', 'encre', 'm', weight='bold')
line(ax, [(44, 8), (44, 47)], 'fixe', lw=0.6, dash=True)
for cx, x, nom in [(23, v[0], 'case 1'), (65, v[1], 'case 2')]:
    box(ax, cx - 8, 36, 16, 10, 'sujet', label=str(x), size='l', weight='bold')
    text(ax, cx, 32, nom, 'sujet', 's')
    text(ax, cx, 24.5, rf'${5}\times{x} = 2\times{x} + 3\times{x}'.replace('{5}', '5') + '$', 'varie', 's')
    arrow(ax, (cx, 21), (cx, 17), 'varie', lw=0.9)
    box(ax, cx - 14, 6, 28, 10, 'resultat', label=rf'${5 * x} = {2 * x} + {3 * x}$', size='m')
save(fig, '58-037')
