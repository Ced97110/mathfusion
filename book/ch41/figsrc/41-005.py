import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# Le signe : nombre + unité
text(ax, 31, 56, '50', 'sujet', 'xl')
text(ax, 44, 56, 'N', 'varie', 'xl')
text(ax, 31, 47, 'nombre', 'sujet', 's')
text(ax, 55, 47, 'unité : le newton', 'varie', 's')
line(ax, [(31, 52), (31, 49.5)], 'sujet', lw=0.7)
line(ax, [(44, 52), (50, 49.5)], 'varie', lw=0.7)
# Repère : 5 kg demandent 50 N, soit 10 N par kilogramme
text(ax, 44, 36, 'chaque kilogramme ≈ 10 N', 'fixe', 's')
n, w, g = 5, 14, 2
x0 = (88 - (n * w + (n - 1) * g)) / 2
for i in range(n):
    box(ax, x0 + i * (w + g), 20, w, 11, 'sujet', label='10 N')
brace(ax, x0, x0 + n * w + (n - 1) * g, 18, 'resultat', label='5 kg ≈ 50 N')
save(fig, '41-005')
