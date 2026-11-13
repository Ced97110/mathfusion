import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
o = (44, 42); s = 8
P = lambda a, b: (o[0] + a * s, o[1] + b * s)
arrow(ax, P(-5.2, 0), P(5.2, 0), 'fixe', lw=0.5); arrow(ax, P(0, -5), P(0, 5), 'fixe', lw=0.5)
line(ax, [P(-1.7, -3.4), P(1.7, 3.4)], 'fixe', lw=1.2)
line(ax, [P(-3.6, 1.8), P(3.6, -1.8)], 'sujet', lw=1.6)
arrow(ax, P(0, 0), P(1, 2), 'fixe', lw=1.2); arrow(ax, P(0, 0), P(2, -1), 'sujet', lw=1.2)
d = 2.2
line(ax, [(o[0] + d * 0.447, o[1] + d * 0.894), (o[0] + d * 0.447 + d * 0.894, o[1] + d * 0.894 - d * 0.447), (o[0] + d * 0.894, o[1] - d * 0.447)], 'encre', lw=0.5)
text(ax, P(2, 3.9)[0] + 4, P(2, 3.9)[1] + 2, r'$U$', 'fixe', 'l')
text(ax, P(3.6, -1.8)[0] - 6, P(3.6, -1.8)[1] - 4, r'$U^{\perp}$', 'sujet', 'l')
text(ax, P(1, 2)[0] + 7, P(1, 2)[1] - 1, r'$(1,\,2)$', 'fixe', 's')
text(ax, P(2, -1)[0] + 1, P(2, -1)[1] - 4, r'$(2,\,-1)$', 'sujet', 's')
text(ax, 44, 8, r'$B(x,z)=0$ pour tout $x$ de $U$', 'sujet', 's')
save(fig, '71-072')
