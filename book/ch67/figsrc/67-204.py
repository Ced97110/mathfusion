import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 3, 56, 24, 15, 'sujet', label=r'$v=2+i$', size='m')
box(ax, 33, 56, 24, 15, 'varie', label=r'$\frac{2+i}{2-i}$', size='m')
box(ax, 63, 56, 24, 15, 'resultat', label=r'$\frac{3+4i}{5}$', size='m')
arrow(ax, (27, 63.5), (33, 63.5), 'fixe')
arrow(ax, (57, 63.5), (63, 63.5), 'fixe')
# triangle 3-4-5 a l'echelle 9 mm par unite
ox, oy = 8, 6
A, B, C = (ox, oy), (ox + 36, oy), (ox, oy + 27)
poly(ax, [A, B, C], 'sujet')
line(ax, [(ox, oy + 3), (ox + 3, oy + 3), (ox + 3, oy)], 'sujet', lw=0.7)
text(ax, ox + 18, oy - 3.5, '4', 'sujet', 'm')
text(ax, ox - 4, oy + 13.5, '3', 'sujet', 'm')
text(ax, ox + 18 + 3.6, oy + 13.5 + 4.8, '5', 'sujet', 'm')
arrow(ax, (75, 56), (75, 36), 'resultat')
text(ax, 66, 28, r'$3^{2}+4^{2}=5^{2}$', 'sujet', 'm')
text(ax, 66, 17, r'$(\frac{3}{5})^{2}+(\frac{4}{5})^{2}=1$', 'resultat', 'm')
save(fig, '67-204')
