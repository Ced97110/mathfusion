import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78); ax.set_ylim(14, 92)
f = lambda t: 6 + t * 10; y0, u = 72, 10
T1 = 13 * math.pi / 6
line(ax, [(4, y0), (f(T1) + 5, y0)], 'fixe', lw=0.6)
line(ax, [(f(i * T1 / 160), y0 + u * math.sin(i * T1 / 160)) for i in range(161)], 'sujet')
for k in range(2, 13):
    if k not in (5, 11): disc(ax, f(k * math.pi / 6), y0 + u * math.sin(k * math.pi / 6), 1.0, 'fixe')
disc(ax, f(math.pi / 6), y0 + u / 2, 1.6, 'resultat')
for k, up in ((5, True), (11, False), (13, True)):
    px = f(k * math.pi / 6); py = y0 + u * math.sin(k * math.pi / 6)
    line(ax, [(px, py), (px, y0 + (-1.5 if up else 1.5))], 'fixe', lw=0.5, dash=True)
    disc(ax, px, py, 1.6, 'varie')
    text(ax, px, y0 + (-4.2 if up else 4.2), rf'${k}\pi/6$', 'varie', 's')
text(ax, 2, 89, r'seul point essayé : $\pi/6$', 'resultat', 's', ha='left')
text(ax, 86, 56, 'autres points : non essayés', 'fixe', 's', ha='right')
text(ax, 44, 51, 'Un point ne prouve rien', 'encre', 'm', weight='bold')
text(ax, 44, 44, r'À vérifier pour chaque $x$', 'encre', 'm', weight='bold')
rows = [(r'translation de $2\pi$ → $13\pi/6$', r'$\sin(x+2\pi)=\sin x$'), (r'retournement → $5\pi/6$', r'$\sin(\pi-x)=\sin x$'), (r'demi-tour → $11\pi/6$', r'$\sin(2\pi-x)=-\sin x$')]
for i, (n, e) in enumerate(rows):
    y = 33 - 8 * i
    text(ax, 2, y, n, 'varie', 's', ha='left'); text(ax, 86, y, e, 'resultat', 's', ha='right')
save(fig, '30-186')
