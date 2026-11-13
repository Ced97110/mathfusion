import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(46)
labs = [r'$\sqrt{3}\,\sqrt{6}$', r'$\sqrt{18}$', r'$\sqrt{9\times2}$', r'$3\sqrt{2}$']
roles = ['sujet', 'fixe', 'fixe', 'resultat']
for i, (l, r) in enumerate(zip(labs, roles)):
    box(ax, 2 + i * 21.7, 24, 18, 11, r, label=l, size='s')
for i in range(3):
    arrow(ax, (20.5 + i * 21.7, 29.5), (23.7 + i * 21.7, 29.5), 'varie')
for i, t in enumerate(['règle ×', r'$18=9\times2$', r'$\sqrt{9}=3$']):
    text(ax, 22 + i * 21.7, 18, t, 'varie', 's')
text(ax, 44, 9, r'des deux côtés : environ 4,24', 'fixe', 's')
save(fig, '22-093')
