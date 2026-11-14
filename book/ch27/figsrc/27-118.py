import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0 = 20; sc = 2.4
rows = [('φ = 0°', 20, '20°'), ('φ = 50°', 12.70, '12,70°'), ('φ = 90°', 0, '0°')]
for i, (lab, a, t) in enumerate(rows):
    y = 38 - i*13
    text(ax, 10, y, lab, 'autre', 's')
    if a > 0: box(ax, x0, y-4, a*sc, 8, 'varie')
    text(ax, x0 + a*sc + 2, y, 'α = ' + t, 'varie', 's', ha='left')
line(ax, [(x0+20*sc, 10), (x0+20*sc, 50)], 'sujet', dash=True, lw=1.2)
text(ax, x0+20*sc, 53, 'θ = 20°', 'sujet', 's')
line(ax, [(x0, 10), (x0, 50)], 'fixe')
text(ax, 46, 4, 'aucune barre ne dépasse θ', 'resultat', 's')
save(fig, '27-118')
