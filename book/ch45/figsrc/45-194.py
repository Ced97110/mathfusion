import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
m, n, s, x0, y0 = 2, 3, 9.0, 26.0, 12.0
for i in range(m):
    for j in range(n):
        box(ax, x0 + j * s, y0 + (m - 1 - i) * s, s, s, 'resultat', r=0.6)
brace(ax, x0, x0 + n * s, y0 + m * s + 1, 'varie', label=r'$n$ = 3 colonnes', down=False)
text(ax, x0 - 3, y0 + m * s / 2, r'$m$ = 2', 'sujet', 'm', ha='right')
text(ax, x0 - 3, y0 + m * s / 2 - 4.5, 'lignes', 'sujet', 's', ha='right')
text(ax, x0 + n * s / 2, y0 - 4, r'$mn$ = 2 × 3 = 6 cases', 'resultat', 'm')
text(ax, 44, 51, r'$mn$ = $m$ fois $n$', 'encre', 'l')
save(fig, '45-194')
