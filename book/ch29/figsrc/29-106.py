import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(68)
text(ax, 44, 62, r'$r = 1$ : $s = \theta$, $A = \theta/2$', 'resultat')
for cx, th, s_, a_ in ((22, 2, '2', '1'), (66, 0.5, '0,5', '0,25')):
    line(ax, arc(cx, 38, 15, 0, 2 * math.pi), 'fixe', dash=True)
    poly(ax, [(cx, 38)] + arc(cx, 38, 15, 0, th), 'sujet')
    line(ax, arc(cx, 38, 15, 0, th), 'varie', lw=2.0)
    text(ax, cx + 7.5, 35, r'$1$', 'sujet', 's')
    text(ax, cx, 19, r'$\theta = $' + s_, 'encre')
    text(ax, cx, 13, r'$s = $' + s_ + ' m', 'varie')
    text(ax, cx, 7, r'$A = $' + a_ + r' m$^2$', 'sujet')
save(fig, '29-106')
