import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 44, '⟨3⟩ = {0, 3, 6, 9}', 'sujet', 'l')
xc = lambda i: 4.2 + 6.6 * i + 3
for h in range(12):
    hot = h % 3 == 0
    box(ax, 4.2 + 6.6 * h, 18, 6, 8, 'sujet' if hot else 'fixe', label=str(h), size='s', r=0.4)
for h in (0, 3, 6):
    arrow(ax, (xc(h) + 1, 27.5), (xc(h + 3) - 1, 27.5), 'varie', curve=-0.5)
text(ax, 44, 8, '4 éléments : |3| = 4', 'resultat', 'm')
save(fig, '60-089')
