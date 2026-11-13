import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, S = 14, 12, 30.0; h = math.pi / 2
line(ax, [(ox, oy), (ox + 56, oy)], 'fixe', lw=0.6); line(ax, [(ox, oy), (ox, oy + 58)], 'fixe', lw=0.6)
line(ax, [(ox, oy), (ox + 54, oy + 54)], 'fixe', lw=1.0, dash=True)
ts = [i * h / 60 for i in range(61)]
line(ax, [(ox + t * S, oy + math.sin(t) * S) for t in ts], 'sujet', lw=1.8)
line(ax, [(ox + math.sin(t) * S, oy + t * S) for t in ts], 'varie', lw=1.8)
A = (ox + h * S, oy + S); B = (ox + S, oy + h * S)
line(ax, [(A[0], oy), A, (ox, A[1])], 'sujet', dash=True, lw=0.7)
line(ax, [(B[0], oy), B, (ox, B[1])], 'varie', dash=True, lw=0.7)
arrow(ax, (A[0] - 2, A[1] + 1.5), (B[0] + 2, B[1] - 1.5), 'resultat', lw=1.2, curve=0.0)
disc(ax, *A, 1.4, 'sujet'); disc(ax, *B, 1.4, 'varie')
text(ax, A[0] + 2.5, A[1] - 3, r'$A=(\pi/2,\ 1)$', 'sujet', 's', ha='right') if False else None
text(ax, A[0] - 3, A[1] - 5, r'$A=(\pi/2,\ 1)$', 'sujet', 's', ha='right')
text(ax, B[0] - 2, B[1] + 3.5, r'$A^{\prime}=(1,\ \pi/2)$', 'varie', 's', ha='left')
for v, s in ((1, '1'), (h, r'$\pi/2$')):
    text(ax, ox + v * S, oy - 3, s, 'sujet' if v == h else 'varie', 's')
    text(ax, ox - 2, oy + v * S, s, 'varie' if v == h else 'sujet', 's', ha='right')
text(ax, ox + 40, oy + 8, 'sinus', 'sujet', 'm'); text(ax, ox + 6, oy + 40, 'arcsinus', 'varie', 'm', ha='left')
save(fig, '33-073')
