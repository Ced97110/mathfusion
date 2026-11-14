import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
ox, oy, S = 44, 48, 17.0; h = math.pi / 2
ts = [-h + i * math.pi / 80 for i in range(81)]
line(ax, [(ox - 33, oy), (ox + 33, oy)], 'fixe', lw=0.5); line(ax, [(ox, oy - 33), (ox, oy + 33)], 'fixe', lw=0.5)
line(ax, [(ox - 31, oy - 31), (ox + 31, oy + 31)], 'fixe', lw=1.0, dash=True)
line(ax, [(ox + t * S, oy + math.sin(t) * S) for t in ts], 'sujet', lw=1.8)
line(ax, [(ox + math.sin(t) * S, oy + t * S) for t in ts], 'varie', lw=1.8)
A = (ox + h * S, oy + S); B = (ox + S, oy + h * S)
line(ax, [A, B], 'resultat', lw=0.8, dash=True)
disc(ax, *A, 1.3, 'sujet'); disc(ax, *B, 1.3, 'varie')
text(ax, A[0] + 2.5, A[1] - 3, 'A', 'sujet', 'l', ha='left'); text(ax, B[0] - 2.5, B[1] + 3, 'A′', 'varie', 'l', ha='right')
text(ax, ox + 14, oy - 7, 'sinus', 'sujet', 'm'); text(ax, ox - 14, oy + 18, 'arcsinus', 'varie', 'm')
text(ax, ox + 33, oy + 36, r'$y=x$', 'fixe', 'm')
save(fig, '33-069')
