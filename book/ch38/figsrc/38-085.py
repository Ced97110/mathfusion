import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
# courbe du sinus de 0° à 180° : 1° = 0,42 mm ; sin = 1 -> 34 mm
o = (6, 18)
kx, ky = 76 / 180, 34.0
pts = [(o[0] + kx * t, o[1] + ky * math.sin(math.radians(t))) for t in [180 * i / 180 for i in range(181)]]
line(ax, [(o[0], o[1]), (o[0] + 76, o[1])], 'fixe', lw=0.9)
line(ax, pts, 'fixe', lw=1.3)
for t in (0, 90, 180):
    ax.plot([o[0] + kx * t] * 2, [o[1] - 1.2, o[1] + 1.2], color=COL['fixe'], lw=0.8)
    text(ax, o[0] + kx * t, o[1] - 4, f'{t}°', 'fixe', 's')
marks = [(3.25, 'varie', 3.25), (60, 'resultat', 60), (176.75, 'varie', 176.75)]
for t, role, _ in marks:
    x, y = o[0] + kx * t, o[1] + ky * math.sin(math.radians(t))
    disc(ax, x, y, 1.4, role)
    ax.plot([x, x], [o[1], y], color=COL[role], lw=1.0, ls='--', zorder=2)
text(ax, o[0] + kx * 60, o[1] + ky * math.sin(math.radians(60)) + 5, r'$60°$ : $0{,}86603$', 'resultat', 's')
text(ax, 16, o[1] + 10, r'$3{,}25°$', 'varie', 's')
text(ax, 16, o[1] + 6.5, r'$0{,}05669$', 'varie', 's')
text(ax, 72, o[1] + 10, r'$176{,}75°$', 'varie', 's')
text(ax, 72, o[1] + 6.5, r'$0{,}05669$', 'varie', 's')
text(ax, 44, 76, r'$\sin(180°-x)=\sin x$', 'encre', 'm')
text(ax, 44, 68, 'petit sinus aux deux bouts : à éviter', 'varie', 's')
text(ax, 44, 8, 'angles voisins de 60° : à préférer', 'resultat', 's')
save(fig, '38-085')
