import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s = 28
poly(ax, [(6, 14), (6+s, 14), (6+s, 14+s), (6, 14+s)], 'sujet')
text(ax, 6 + s/2, 14 + s/2, 'aire\n2 m²', 'sujet', 'm')
line(ax, [(6, 11), (6+s, 11)], 'varie', lw=1.4)
text(ax, 6 + s/2, 6.5, 'règle : environ 1,41 m', 'varie', 's')
box(ax, 44, 30, 40, 12, 'resultat', label='le côté existe', size='m')
box(ax, 44, 12, 40, 14, 'limite', label='pas d\'écriture\ndécimale exacte', size='s')
text(ax, 64, 47, 'la pièce a un côté', 'encre', 'm')
save(fig, '22-006')
