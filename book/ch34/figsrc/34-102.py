import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
ys = [80, 60, 40, 20]; x = 20; w = 46; h = 10
labs = ['cos 60° = 0,5', '1,5', '0,75', '± 0,866']
roles = ['sujet', 'fixe', 'fixe', 'resultat']
for y, l, r in zip(ys, labs, roles): box(ax, x, y, w, h, r, label=l, size='l' if r == 'resultat' else 'm', weight='bold' if r == 'resultat' else 'normal')
ops = ['1. + 1', '2. ÷ 2', '3. racine, signe ±']
for i, o in enumerate(ops):
    arrow(ax, (x + w / 2, ys[i]), (x + w / 2, ys[i + 1] + h), 'varie')
    text(ax, x + w / 2 + 4, ys[i] - 5, o, 'varie', 's', ha='left')
text(ax, x - 2, ys[0] + 5, '$\\theta$ = 60°', 'sujet', 's', ha='right')
text(ax, x - 2, ys[3] + 5, '$\\theta/2$', 'resultat', 's', ha='right')
text(ax, x + w / 2, 12, '4. choisir + ou −', 'varie', 'm', weight='bold')
text(ax, x + w / 2, 6, 'selon le quadrant de $\\theta/2$', 'varie', 's')
save(fig, '34-102')
