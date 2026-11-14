import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, r'$G=\mathbb{Z}/4\oplus\mathbb{Z}/2$ , $g=(1,0)$', 'encre', 's')
text(ax, 44, 82, r'$H=\{(0,0),(0,1)\}$', 'encre', 's')
box(ax, 48, 64, 36, 10, 'varie', label=r'$K=\{(0,0),(0,1)\}\supseteq H$', size='s')
cx, cy, R, r = 24, 42, 11, 5.2
names = ['0', r'$g$', r'$2g$', r'$3g$']
for k in range(4):
    a = math.radians(90 - 90 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), r, 'sujet', label=names[k], size='s')
box(ax, 56, 38, 26, 10, 'varie', label=r'$K/H=\{0\}$', size='s')
text(ax, 69, 33, 'complément', 'varie', 's')
text(ax, 42, 42, '⊕', 'encre', 'l')
arrow(ax, (69, 49), (69, 63), 'varie')
text(ax, 71, 56, 'remonter', 'varie', 's', ha='left')
text(ax, cx, 21, r'$\langle g+H\rangle$ : horloge de 4', 'sujet', 's')
text(ax, 44, 8, r'$G/H = \langle g+H\rangle \oplus K/H$', 'resultat', 'l', weight='bold')
save(fig, '60-137')
