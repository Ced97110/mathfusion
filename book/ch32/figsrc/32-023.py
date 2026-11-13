import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = lambda v: 7 + (v + 360) / 1080 * 74
y0, A = 28, 16
poly(ax, [(f(0), 11), (f(360), 11), (f(360), 50), (f(0), 50)], 'fixe')
for v in (-360, 0, 360, 720):
    line(ax, [(f(v), 11), (f(v), 48)], 'fixe', lw=0.5, dash=True)
    text(ax, f(v), 6.5, f'{v}°'.replace('-', '−'), 'fixe', 's')
line(ax, [(4, y0), (84, y0)], 'fixe', lw=0.6)
pts = [(f(v), y0 + A * math.sin(math.radians(v))) for v in range(-360, 721, 5)]
line(ax, pts, 'sujet', lw=1.3)
ky = y0 + A * 0.5
line(ax, [(4, ky), (84, ky)], 'varie', lw=1.1)
for v in (-330, -210, 30, 150, 390, 510): disc(ax, f(v), ky, 1.3, 'resultat')
text(ax, 14, 55, r'$y=\sin\,x$', 'sujet', 'm'); text(ax, 70, ky + 4.5, r'$y=0{,}5$', 'varie', 's')
text(ax, f(180), 55, 'un tour : 2 croisements', 'resultat', 's')
save(fig, '32-023')
