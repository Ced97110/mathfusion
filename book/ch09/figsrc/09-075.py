import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
x0, w = 22, 14
text(ax, 11, 26, '12 %', 'sujet', 'l')
for i, (d, r) in enumerate([('0', 'fixe'), ('1', 'sujet'), ('2', 'sujet')]):
    box(ax, x0 + i * w, 18, w, 14, r, label=d, size='l')
disc(ax, x0 + 3 * w, 14.5, 1.5, 'varie')
text(ax, x0 + 3 * w, 10, 'virgule de 12', 'varie', 's')
disc(ax, x0 + w, 14.5, 1.5, 'resultat')
text(ax, x0 + 3 * w + 8, 26, '12,', 'varie', 'm') if False else None
arrow(ax, (x0 + 3 * w, 34), (x0 + w, 34), 'varie', curve=0.5)
text(ax, x0 + 2 * w, 46, '2 rangs à gauche', 'varie', 'm')
text(ax, x0 + w - 6, 4, '0,12', 'resultat', 'l')
text(ax, x0 + 1.5 * w, 3, 'zéro ajouté devant', 'fixe', 's') if False else None
save(fig, '09-075')
