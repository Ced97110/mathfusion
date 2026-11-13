import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# plan complexe : point 3+4i
ox, oy, u = 10, 10, 5.2
arrow(ax, (ox-4, oy), (ox+22, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy-4), (ox, oy+44), 'fixe', lw=0.8)
px, py = ox+3*u, oy+4*u*0.9
line(ax, [(px, oy), (px, py)], 'fixe', dash=True); line(ax, [(ox, py), (px, py)], 'fixe', dash=True)
disc(ax, px, py, 1.6, 'sujet')
text(ax, px+1, py+5, r'$z = 3+4i$', 'sujet', 's')
text(ax, 13, 56, r'$\mathbb{C}$', 'sujet', 'l')
# droite réelle
f = numberline(ax, 50, 80, 20, 0, 25, step=5, arrow_right=False, role='fixe', every=1)
disc(ax, f(25), 20, 1.6, 'resultat')
text(ax, 65, 56, r'$\mathbb{R}$', 'resultat', 'l')
text(ax, f(25)-1, 26, r'$z\bar{z} = 25$', 'resultat', 's')
arrow(ax, (px+3, py-2), (f(25)-1, 23.5), 'varie', curve=-0.25)
text(ax, 58, 42, 'norme', 'varie', 'm')
save(fig, '75-177')
