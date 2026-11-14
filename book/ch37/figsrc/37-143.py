import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
k = 0.9; x0 = 8
text(ax, 44, 56, '3 restes, somme 75', 'fixe', 'm')
x = x0
for v, role in ((35, 'sujet'), (25, 'varie'), (15, 'autre')):
    box(ax, x, 40, v * k, 7, role, label=str(v), size='m'); x += v * k
text(ax, 44, 35, 'côtés 40 ; 50 ; 60', 'fixe', 's')
text(ax, 44, 29.5, 'produit 13 125 → Δ ≈ 992,2', 'sujet', 's')
for i in range(3): box(ax, x0 + i * 25 * k, 16, 25 * k, 7, 'resultat', label='25', size='m')
text(ax, 44, 11, 'côtés 50 ; 50 ; 50', 'fixe', 's')
text(ax, 44, 5.5, 'produit 15 625 → Δ ≈ 1 082,5', 'resultat', 's')
save(fig, '37-143')
