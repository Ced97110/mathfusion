import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(100)
# haut : courbe du sinus (x en radians) contre la droite y = x, de 0 à 60°
o = (8, 50)
s = 36.0                      # mm par radian, mêmes unités sur les deux axes
xmax = math.pi / 3
pts = [(o[0] + s * t, o[1] + s * math.sin(t)) for t in [xmax * i / 60 for i in range(61)]]
line(ax, pts, 'sujet', lw=1.4)
line(ax, [o, (o[0] + s * xmax, o[1] + s * xmax)], 'fixe', lw=0.9, dash=True)
arrow(ax, o, (o[0] + 52, o[1]), 'fixe', lw=0.8)
arrow(ax, o, (o[0], o[1] + 40), 'fixe', lw=0.8)
text(ax, o[0] + 52, o[1] - 3, 'angle', 'fixe', 's')
text(ax, 49, 68, 'courbe du sinus', 'sujet', 's', ha='left')
text(ax, 22, 85, r'droite $y=x$', 'fixe', 's')
text(ax, 44, 93, 'près de 0°, le sinus monte au plus vite', 'encre', 'm')
# bas : deux barres de même longueur (1 mm = 0,0001), agrandies
k = 1 / 0.0001 / 1000 * 1.0   # 0,00175 -> 17,5 mm
ax.add_patch(Rectangle((8, 28), 0.00175 * 1e4, 4.5, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
ax.add_patch(Rectangle((8, 14), 0.1 * math.pi / 180 * 1e4, 4.5, ec=COL['autre'], fc=FILL['autre'], lw=0.8, zorder=2))
text(ax, 8 + 17.5 + 3, 30.3, r'$\sin3{,}35°-\sin3{,}25°=0{,}00175$', 'sujet', 's', ha='left')
text(ax, 8 + 17.5 + 3, 16.3, r'$0{,}1\times\pi/180\approx0{,}00175$', 'autre', 's', ha='left')
text(ax, 8, 38, 'même longueur (échelle agrandie)', 'fixe', 's', ha='left')
save(fig, '38-080')
