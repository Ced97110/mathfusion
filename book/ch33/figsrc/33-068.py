import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
S = 13.0; h = math.pi / 2
def graph(ox, oy, curve, role, xs, ys):
    line(ax, [(ox - 15, oy), (ox + 15, oy)], 'fixe', lw=0.6); line(ax, [(ox, oy - 25), (ox, oy + 25)], 'fixe', lw=0.6)
    line(ax, [(ox + X * S * xs, oy + curve(X) * S * ys) for X in [i / 40 for i in range(-40, 41)]] if False else curve, role, lw=1.6)
# sinus restreint : x = angle (pi/2 -> 14), y = sin
ox1, oy, k = 20, 38, 14 / h
cs = [(ox1 + t * k, oy + math.sin(t) * 14) for t in [(-h + i * math.pi / 60) for i in range(61)]]
cs2 = [(ox2, oy + a * k) for ox2, a in []]
line(ax, [(ox1 - 17, oy), (ox1 + 17, oy)], 'fixe', lw=0.6); line(ax, [(ox1, oy - 17), (ox1, oy + 17)], 'fixe', lw=0.6)
line(ax, cs, 'sujet', lw=1.6)
ox2 = 68
ca = [(ox2 + math.sin(t) * 14, oy + t * k) for t in [(-h + i * math.pi / 60) for i in range(61)]]
line(ax, [(ox2 - 17, oy), (ox2 + 17, oy)], 'fixe', lw=0.6); line(ax, [(ox2, oy - 17), (ox2, oy + 17)], 'fixe', lw=0.6)
line(ax, ca, 'varie', lw=1.6)
a, b = math.pi / 6, 0.5
A = (ox1 + a * k, oy + b * 14); B = (ox2 + b * 14, oy + a * k)
line(ax, [(ox1 + a * k, oy), A, (ox1, oy + b * 14)], 'sujet', dash=True, lw=0.7)
line(ax, [(ox2 + b * 14, oy), B, (ox2, oy + a * k)], 'varie', dash=True, lw=0.7)
disc(ax, *A, 1.2, 'sujet'); disc(ax, *B, 1.2, 'varie')
text(ax, A[0] + 2, A[1] + 3.5, '(a, b)', 'sujet', 's', ha='left')
text(ax, B[0] + 2, B[1] - 4, '(b, a)', 'varie', 's', ha='left')
text(ax, ox1, oy + 24, 'sinus', 'sujet', 'm'); text(ax, ox2, oy + 24, 'arcsinus', 'varie', 'm')
text(ax, ox1, 11, r'$\sin a=b$', 'sujet', 'm'); text(ax, ox2, 11, r'$\arcsin b=a$', 'varie', 'm')
arrow(ax, (38, 36), (50, 36), 'resultat', lw=1.2, curve=0)
text(ax, 44, 40.5, 'échange', 'resultat', 's')
save(fig, '33-068')
