import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 9.0; ox, oy = 8, 36
P = (ox + 7 * u, oy + 2 * u)
poly(ax, [(ox, oy), (P[0], oy), P], 'fixe')
line(ax, [(ox, oy), P], 'sujet', lw=1.3)
line(ax, [(ox, oy), (P[0], oy)], 'varie', lw=1.3)
line(ax, [(P[0], oy), P], 'varie', lw=1.3)
disc(ax, P[0], P[1], 1.5, 'sujet')
text(ax, P[0], P[1] + 4, r'$7+2i$', 'sujet', 'm')
text(ax, (ox + P[0]) / 2, oy - 3.5, r'$m=7$', 'varie', 's')
text(ax, P[0] - 2, oy + u, r'$n=2$', 'varie', 's', ha='right')
text(ax, ox + 3 * u, oy + 2.2 * u * 0.55 + 5, 'distance', 'sujet', 's', rot=0)
y = 12
for x, w, role, lab in [(4, 24, 'varie', r'$7^2=49$'), (32, 20, 'varie', r'$2^2=4$'), (56, 28, 'resultat', r'$49+4=53$')]:
    box(ax, x, y, w, 9, role, label=lab)
text(ax, 30, y + 4.5, '+', 'encre', 'l') if False else None
arrow(ax, (28, y + 4.5), (32, y + 4.5), 'fixe', lw=0.6)
arrow(ax, (52, y + 4.5), (56, y + 4.5), 'fixe', lw=0.6)
text(ax, 70, 3, r'$\delta=53$ = distance$^2$', 'resultat', 's')
save(fig, '56-127')
