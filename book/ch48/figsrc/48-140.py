import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx = [14, 44, 74]; top = ['échange 1 2', 'échange 1 3', 'circulaire']
roles = ['sujet', 'sujet', 'resultat']; sg = ['−1', '−1', '1']
for c, t, r, s in zip(cx, top, roles, sg):
    box(ax, c - 11, 36, 22, 10, r, label=t, size='s')
    arrow(ax, (c, 36), (c, 23), 'varie')
    box(ax, c - 8, 12, 16, 10, 'autre', label=s, size='m')
text(ax, 29, 41, '∘', 'encre', 'l'); text(ax, 59, 41, '=', 'encre', 'l')
text(ax, 29, 17, '×', 'encre', 'l'); text(ax, 59, 17, '=', 'encre', 'l')
text(ax, 44, 52, 'permutations de S₃', 'sujet', 's'); text(ax, 44, 5, 'signatures, dans {1, −1}', 'autre', 's')
text(ax, 25, 29.5, 'sg', 'varie', 's')
save(fig, '48-140')
