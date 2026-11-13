import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
m, n, s, x0, y0 = 4, 6, 8.0, 26.0, 14.0
reached = {(k % m, k % n) for k in range(12)}
for i in range(m):
    for j in range(n):
        box(ax, x0 + j * s, y0 + (m - 1 - i) * s, s, s, 'resultat' if (i, j) in reached else 'limite', r=0.6)
text(ax, x0 - 3, y0 + m * s / 2, '4 lignes', 'sujet', 's', ha='right')
text(ax, x0 + n * s / 2, y0 + m * s + 3, '6 colonnes', 'sujet', 's')
box(ax, 3, 4, 10, 6, 'resultat', r=0.6); text(ax, 15, 7, '12 cases atteintes', 'resultat', 's', ha='left')
box(ax, 47, 4, 10, 6, 'limite', r=0.6); text(ax, 59, 7, '12 jamais', 'limite', 's', ha='left')
text(ax, 44, 63, r'$mn/d$ = 24 / 2 = 12 < 24', 'encre', 'm')
save(fig, '45-197')
