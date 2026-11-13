import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s, g = 5.0, 1.5
x0 = 4
for i in range(5): box(ax, x0 + i * (s + g), 40, s, s, 'sujet', r=0.5)
x1 = x0 + 5 * (s + g) + 4
for i in range(3): box(ax, x1 + i * (s + g), 40, s, s, 'varie', r=0.5)
brace(ax, x0, x0 + 5 * s + 4 * g, 38, 'sujet', '5 facteurs')
brace(ax, x1, x1 + 3 * s + 2 * g, 38, 'varie', '3 facteurs')
for i in range(8): box(ax, 4 + i * (s + g), 14, s, s, 'resultat', r=0.5)
brace(ax, 4, 4 + 8 * s + 7 * g, 12, 'resultat', '8 facteurs')
arrow(ax, (44, 29), (44, 22), 'varie')
text(ax, 62, 25.5, 'mis bout à bout', 'varie', 's')
text(ax, 22, 51, r'$2^{5}\times2^{3}$', 'sujet', 'l')
text(ax, 66, 51, r'$=2^{8}=256$', 'resultat', 'l')
save(fig, '14-002')
