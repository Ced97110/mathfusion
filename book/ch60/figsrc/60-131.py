import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
bx, bw, bh = 2, 52, 16
ys = [64, 38, 12]
labs = [('départ', r'$g$ d’ordre 4, maximal'.replace('\\u2019', '’'), 'sujet'),
        ('étape décisive', r'$h$ hors de $\langle g\rangle$,' + '\n' + 'd’ordre le plus petit', 'varie'),
        ('arrivée', r'$K$ complète $\langle g\rangle$', 'resultat')]
for y, (tag, lab, role) in zip(ys, labs):
    box(ax, bx, y, bw, bh, role, label=lab, size='s')
    text(ax, bx + 1, y + bh + 2.6, tag, role, 's', ha='left', weight='bold')
for y in ys[:2]:
    arrow(ax, (bx + bw / 2, y - 0.5), (bx + bw / 2, y - 7.5), 'varie')
# right panel: possible h
px, pw = 60, 26
text(ax, px + pw / 2, 78, 'ordre de h', 'fixe', 's')
text(ax, px + pw / 2, 74, 'hors de ⟨g⟩', 'fixe', 's')
data = [((0, 1), 2), ((1, 1), 4), ((2, 1), 2), ((3, 1), 4)]
for k, (c, o) in enumerate(data):
    role = 'varie' if o == 2 else 'fixe'
    box(ax, px, 60 - k * 10.5, pw, 8.5, role, label=f'({c[0]}, {c[1]}) : {o}', size='s', r=0.6)
text(ax, px + pw / 2, 14, 'on prend un', 'varie', 's')
text(ax, px + pw / 2, 9.5, 'ordre 2', 'varie', 's', weight='bold')
save(fig, '60-131')
