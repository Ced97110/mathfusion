import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
u = 2.8; x0 = (W - 23 * u) / 2; h = 7 * u
text(ax, 44, 84, "comptée d'un bloc", 'sujet', 's')
box(ax, x0, 62, 23 * u, h, 'sujet', label=r'$7 \times 23 = 161$', size='m')
text(ax, 44, 52, 'même surface, même nombre', 'resultat', 's')
text(ax, 44, 43, 'comptée en deux morceaux', 'varie', 's')
box(ax, x0, 22, 20 * u, h, 'sujet', label='140', size='m')
box(ax, x0 + 20 * u, 22, 3 * u, h, 'varie', label='21', size='s')
text(ax, 44, 12, r'$140 + 21 = 161$', 'resultat', 'm')
save(fig, '10-059')
