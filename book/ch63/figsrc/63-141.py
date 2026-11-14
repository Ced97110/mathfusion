import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ys = [52, 32, 12]
left = ['{1} : 1 élément', 'H = ⟨σ⟩ : 2', 'G : 4 éléments']
right = ['E', 'ℚ(√3)', 'ℚ']
for y, l, r in zip(ys, left, right):
    box(ax, 2, y, 26, 10, role='sujet', label=l)
    box(ax, 60, y, 26, 10, role='autre', label=r)
for i in range(2):
    line(ax, [(15, ys[i] - 0.8), (15, ys[i + 1] + 10.8)], 'fixe')
    line(ax, [(73, ys[i] - 0.8), (73, ys[i + 1] + 10.8)], 'fixe')
text(ax, 44, 47, '|H| = 2 = [E:ℚ(√3)]', 'resultat', 's')
text(ax, 44, 27, '[G:H] = 2 = [ℚ(√3):ℚ]', 'resultat', 's')
arrow(ax, (28.8, 37), (59.2, 37), 'varie')
text(ax, 44, 40.3, 'Inv', 'varie', 's')
save(fig, '63-141')
