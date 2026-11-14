import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, U = 26, 52, 14.0
r = 2 ** 0.25
arrow(ax, (cx - 20, cy), (cx + 22, cy), 'fixe', lw=0.8)
arrow(ax, (cx, cy - 19), (cx, cy + 22), 'fixe', lw=0.8)
for sx, sy, role in ((1, 0, 'sujet'), (-1, 0, 'sujet'), (0, 1, 'varie'), (0, -1, 'varie')):
    disc(ax, cx + sx * r * U, cy + sy * r * U, 1.8, role)
text(ax, cx + 12, cy - 5, 'réelles', 'sujet', 's')
text(ax, cx + 12, cy + 18, 'non réelles', 'varie', 's')
text(ax, 66, 66, r'$x^4-2$', 'sujet', 'm')
text(ax, 66, 58, 'irréductible', 'sujet', 's')
text(ax, 66, 50, '2 non réelles', 'varie', 's')
text(ax, 66, 42, 'degré 4 : pas premier', 'limite', 's')
box(ax, 8, 4, 33, 12, 'limite', label=r'$S_4$ : 24', size='s')
box(ax, 47, 4, 37, 12, 'resultat', label='groupe réel : 8', size='s')
text(ax, 44, 22, 'groupe de Galois', 'encre', 's')
save(fig, '65-134')
