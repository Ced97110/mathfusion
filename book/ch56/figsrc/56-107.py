import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
a = [48, 24, 12, 6, 3]
b = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]
assert len(a) == 5 and len(b) == 10
w, pitch, x0, h = 14, 16.5, 2, 9
# chaîne de 48 : 5 idéaux (bleu), le dernier en vert
for i, v in enumerate(a):
    box(ax, x0 + pitch * i, 46, w, h, 'resultat' if i == 4 else 'sujet', label=f'({v})', size='s')
    if i: arrow(ax, (x0 + pitch * i - 2.4, 50.5), (x0 + pitch * i - 0.1, 50.5), 'fixe', lw=0.6)
line(ax, [(2, 38), (86, 38)], 'fixe', lw=0.4)
# chaîne de 1024 : 10 idéaux (violet), sur deux rangées de 5, le dernier en vert
for j, v in enumerate(b):
    r, i = divmod(j, 5)
    y = 24 - 17 * r
    box(ax, x0 + pitch * i, y, w, h, 'resultat' if j == 9 else 'autre', label=f'({v})', size='s')
    if i: arrow(ax, (x0 + pitch * i - 2.4, y + 4.5), (x0 + pitch * i - 0.1, y + 4.5), 'fixe', lw=0.6)
xe = x0 + pitch * 4 + w / 2
line(ax, [(xe, 24), (xe, 19.5), (x0 + w / 2, 19.5)], 'fixe', lw=0.6)
arrow(ax, (x0 + w / 2, 19.5), (x0 + w / 2, 15.5), 'fixe', lw=0.6)
save(fig, '56-107')
