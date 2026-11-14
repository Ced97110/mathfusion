import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 84, r'$v=m+ni$ avec $m,n$ entiers', 'encre', 'm')
box(ax, 4, 58, 30, 14, 'sujet', label=r'$v=3+2i$', size='m')
box(ax, 50, 58, 34, 14, 'varie', label=r'$v^{2}=5+12i$', size='m')
arrow(ax, (34, 65), (50, 65), 'varie')
text(ax, 42, 70, 'carré', 'varie', 's')
# triangle 5-12-13 a l'echelle 3 mm par unite : 5 horizontal (partie reelle), 12 vertical
ox, oy = 10, 10
A, B, C = (ox, oy), (ox + 15, oy), (ox, oy + 36)
poly(ax, [A, B, C], 'sujet')
line(ax, [(ox, oy + 3), (ox + 3, oy + 3), (ox + 3, oy)], 'sujet', lw=0.7)
text(ax, ox + 7.5, oy - 4.5, '5', 'sujet', 'm')
text(ax, ox - 4, oy + 18, '12', 'sujet', 'm')
text(ax, ox + 7.5 + 3.7, oy + 18 + 1.5, '13', 'sujet', 'm')
text(ax, 62, 34, r'$5^{2}+12^{2}=13^{2}$', 'resultat', 'm')
text(ax, 62, 24, r'$N(v)=3^{2}+2^{2}=13$', 'sujet', 'm')
save(fig, '67-205')
