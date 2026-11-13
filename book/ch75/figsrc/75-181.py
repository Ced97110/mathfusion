import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 0.95
w, h = 16*u, 45*u
x0, y0 = 22, 14
box(ax, x0, y0, w, h, 'fixe', r=0.3)
box(ax, x0, y0, w, w*0+16*u, 'resultat', r=0.3)
text(ax, x0+w/2, y0+h*0.62, '45', 'fixe', 'l'); text(ax, x0+w/2, y0+h*0.62-5, 'impair', 'fixe', 's')
text(ax, x0+w/2, y0+8, '16', 'resultat', 'l')
text(ax, x0+w/2, y0-5, r'$720 = 16 \times 45$', 'encre', 's')
arrow(ax, (x0+w+3, y0+8), (50, y0+8), 'varie')
text(ax, 67, y0+8+9, r'$q^{n^2}$', 'resultat', 'l')
text(ax, 67, y0+8+1, r'$q=2,\ n=2$', 'sujet', 's')
text(ax, 67, y0+8-6, r'$2^{4} = 16$', 'resultat', 'm')
text(ax, 67, y0+8-13, 'taille du sous-groupe', 'varie', 's')
text(ax, 67, y0+8-17, 'de Sylow', 'varie', 's')
save(fig, '75-181')
