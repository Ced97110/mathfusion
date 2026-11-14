import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
formules = [
    r'$p = 5$ et $q = 11$',
    r'$n = 5\times11 = 55$',
    r'$\varphi(n) = 4\times10 = 40$',
    r'$e = 3$, PGCD$(3, 40) = 1$',
    r'$d = 27$ : $3\times27 = 2\times40 + 1$',
]
for i in range(6):
    y = 80 - i * 13
    disc(ax, 7, y + 5, 4, 'varie', label=str(i + 1))
    if i < 5:
        box(ax, 14, y, 72, 10, 'sujet' if i < 3 else 'autre', label=formules[i])
    else:
        box(ax, 14, y, 35, 10, 'resultat', label='publie (55, 3)')
        box(ax, 51, y, 35, 10, 'fixe', label='garde 27')
save(fig, '53-083')
