import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ys = [68, 46, 24]
for y, t in zip(ys, ['réflexive', 'transitive', 'non symétrique']):
    text(ax, 2, y, t, 'encre', 's', ha='left', weight='bold')
    line(ax, [(2, y - 11), (86, y - 11)], 'fixe', lw=0.4)
# 1) réflexive : a ∣ a
y = ys[0]
disc(ax, 41, y - 1, 3.5, 'sujet', label='a')
arrow(ax, (38.5, y + 2.6), (43.5, y + 2.6), 'resultat', curve=-1.6)
text(ax, 64, y, 'a = a × 1', 'resultat', 's', ha='left')
# 2) transitive : c ∣ b, b ∣ a donc c ∣ a
y = ys[1]
for x, t in [(30, 'c'), (41, 'b'), (52, 'a')]:
    disc(ax, x, y - 2, 3.3, 'sujet', label=t)
arrow(ax, (33.6, y - 2), (37.4, y - 2), 'varie')
arrow(ax, (44.6, y - 2), (48.4, y - 2), 'varie')
arrow(ax, (29, y + 1.2), (53, y + 1.2), 'resultat', curve=-0.5)
text(ax, 64, y, 'donc c ∣ a', 'resultat', 's', ha='left')
# 3) non symétrique : b ∣ a vrai, a ∣ b pas toujours
y = ys[2]
disc(ax, 36, y - 1, 3.3, 'sujet', label='b')
disc(ax, 47, y - 1, 3.3, 'sujet', label='a')
arrow(ax, (39.6, y + 0.5), (43.4, y + 0.5), 'resultat')
arrow(ax, (43.4, y - 2.5), (39.6, y - 2.5), 'limite')
text(ax, 54, y - 1, 'b ∣ a, pas a ∣ b', 'encre', 's', ha='left')
box(ax, 2, 3, 84, 9, 'limite', label='sans 1 (entiers pairs) : 2 ∣ 2 est faux', size='s')
save(fig, '56-027')
