import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
sizes = [1, 3, 2]; roles = ['limite', 'sujet', 'sujet']; heads = ['centre', 'classe de 3', 'classe de 2']
d = 6.4; pad = 2.2; gap = 6
ws = [n * d + 2 * pad for n in sizes]; x = (W - sum(ws) - 2 * gap) / 2; y = 40
for k, n in enumerate(sizes):
    box(ax, x, y - 5, ws[k], 10, roles[k])
    for i in range(n): disc(ax, x + pad + d / 2 + i * d, y, 2.3, roles[k])
    text(ax, x + ws[k] / 2, y + 9, heads[k], roles[k], 's')
    text(ax, x + ws[k] / 2, y - 10, str(n), roles[k], 'l', weight='bold')
    x += ws[k] + gap
text(ax, W / 2, 24, r'$6 = 1 + 3 + 2$ : permutations de 3 objets', 'sujet', 's')
text(ax, W / 2, 15, '3 + 2 = 5 : multiple ni de 2 ni de 3', 'limite', 's')
text(ax, W / 2, 6, r'centre = {1}', 'limite', 'l', weight='bold')
save(fig, '49-190')
