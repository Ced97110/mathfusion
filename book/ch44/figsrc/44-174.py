import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, 'élément × lui-même', 'sujet', 's')
for i, (e, p) in enumerate([(1, '1'), (3, '9'), (5, '25'), (7, '49')]):
    y = 46 - i * 12
    box(ax, 4, y, 38, 9, 'sujet', label=rf'${e}\times{e}={p}$', size='m')
    arrow(ax, (42, y + 4.5), (60, 30), 'resultat')
disc(ax, 68, 30, 7, 'resultat', label='1')
text(ax, 68, 20, 'reste 1 modulo 8', 'resultat', 's')
text(ax, 68, 40, 'le neutre', 'resultat', 's')
save(fig, '44-174')
