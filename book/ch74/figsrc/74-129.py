import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 24, 48, 40, 9, 'sujet', label=r'$\cos 72^\circ \approx 0{,}309$')
cx, cy, R = 20, 24, 12
pts = [(cx + R*math.sin(2*math.pi*k/5), cy + R*math.cos(2*math.pi*k/5)) for k in range(5)]
poly(ax, pts, 'resultat')
text(ax, cx, 7, 'tracer : possible', 'resultat', 's')
arrow(ax, (32, 48), (cx, 38.5), 'sujet')
f = numberline(ax, 52, 74, 26, 0, 1, arrow_right=False)
disc(ax, f(0.618), 26, 1.6, 'limite')
text(ax, f(0.618), 35, r'$2\cos 72^\circ \approx 0{,}618$', 'limite', 's')
arrow(ax, (58, 48), (f(0.618), 38.5), 'sujet')
text(ax, 63, 11, 'répéter : impossible', 'limite', 's')
save(fig, '74-129')
