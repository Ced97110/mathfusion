import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 8, 58, 72, 10, role='sujet', label='f = x⁴ + x³ + x² + x + 1 irréductible sur ℚ', size='s')
box(ax, 1, 22, 86, 28, role='resultat', fill=False, dash=True)
text(ax, 44, 45, 'E = ℚ(ω) contient les 4 racines', 'resultat', 's')
xs = [3, 25, 47, 69]
for x, t in zip(xs, ['ω', 'ω²', 'ω³', 'ω⁴']):
    box(ax, x, 26, 16, 11, role='sujet', label=t)
for i in range(3):
    arrow(ax, (xs[i] + 16.6, 31.5), (xs[i + 1] - 0.6, 31.5), 'varie')
    text(ax, xs[i] + 19, 35.5, '×ω', 'varie', 's')
text(ax, 44, 16, 'ω² = ω×ω, ω³ = ω×ω×ω, ω⁴ = ω×ω×ω×ω', 'encre', 's')
text(ax, 44, 7, 'f irréductible : [E:ℚ] = degré de f = 4', 'resultat', 's', weight='bold')
save(fig, '63-158')
