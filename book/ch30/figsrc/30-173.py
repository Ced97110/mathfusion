import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
X = lambda t: 10 + t * 8.75
y0, sy = 34, 20
line(ax, [(10, y0), (78, y0)], 'fixe')
line(ax, [(X(i * 7.5 / 150), y0 + sy * math.sin(i * 7.5 / 150)) for i in range(151)], 'sujet', lw=1.6)
line(ax, [(10, y0 + sy * 0.5), (78, y0 + sy * 0.5)], 'varie', dash=True)
for t in (0.524, 2.618, 6.807):
    line(ax, [(X(t), y0), (X(t), y0 + sy * 0.5)], 'fixe', dash=True)
    disc(ax, X(t), y0 + sy * 0.5, 1.3, 'resultat')
    text(ax, X(t), y0 - 3.5, f'{t:.3f}'.replace('.', ','), 'resultat', 's')
arrow(ax, (X(0.524), 63), (X(6.807), 63), 'varie')
text(ax, X(3.66), 68, r'$+\,2\pi \approx 6{,}283$', 'varie', 's')
text(ax, 62, y0 + sy * 0.5 + 4.5, r'$\sin x = 0{,}5$', 'varie', 's')
save(fig, '30-173')
