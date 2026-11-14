import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx, cy, R = 32, 36, 27
def arc(a0, a1, r=R, n=60): return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
c = R * math.sqrt(2) / 2
line(ax, arc(90, 270), 'fixe', lw=0.6); line(ax, arc(-90, 90), 'resultat', lw=2.2)
line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.6); line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.6)
A, B, Xp, Yp = (cx - c, cy - c), (cx + c, cy - c), (cx - c, cy), (cx, cy - c)
line(ax, [A, Xp], 'fixe', lw=0.8, dash=True)
line(ax, [A, B], 'fixe', lw=0.8, dash=True)
arrow(ax, (Xp[0] + 1.5, Xp[1] - 1.5), (Yp[0] - 1.5, Yp[1] + 1.5), 'varie', curve=0.35)
disc(ax, A[0], A[1], 1.8, 'sujet'); disc(ax, B[0], B[1], 1.8, 'resultat')
text(ax, A[0] - 4, A[1] - 5, '225°', 'sujet', 's'); text(ax, B[0] + 3, B[1] - 5, '−45°', 'resultat', 's')
text(ax, Xp[0], Xp[1] + 5, r'$-\sqrt{2}/2$', 'varie', 's')
text(ax, Yp[0] + 9, Yp[1] + 4.5, r'$-\sqrt{2}/2$', 'varie', 's')
text(ax, 76, 62, 'cos puis arcsin', 'encre', 's')
save(fig, '33-110')
