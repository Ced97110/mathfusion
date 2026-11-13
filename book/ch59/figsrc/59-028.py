import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 38, 66, '1re case', 'fixe', 's'); text(ax, 62, 66, '2e case', 'fixe', 's')
rows = [(52, r'$x$', '10', '10', 'sujet', 'sujet'), (36, r'$5f_1$', '10', '40', 'varie', 'varie'),
        (14, r'$x-5f_1$', '0', '−30', 'resultat', 'resultat')]
for (y, lab, a, b, ra, rb) in rows:
    text(ax, 14, y + 5, lab, ra, 's')
    box(ax, 28, y, 20, 10, ra, label=a, size='m'); box(ax, 52, y, 20, 10, rb, label=b, size='m')
text(ax, 20, 44, '−', 'varie', 'l')
line(ax, [(4, 30), (84, 30)], 'fixe', dash=True)
text(ax, 4, 66, r'$f_1=(2,\,8)$', 'varie', 's', ha='left')
text(ax, 44, 4, r'reste 1 case : rang $n-1$', 'resultat', 's')
save(fig, '59-028')
