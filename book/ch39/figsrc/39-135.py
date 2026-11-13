import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 8, 12, 14
P = lambda a, b: (ox + a * u, oy + b * u)
q = P(1, math.sqrt(3))
arrow(ax, (ox, oy), (ox + 2.1 * u, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy), (ox, oy + 2.1 * u), 'fixe', lw=0.6)
line(ax, [q, (q[0], oy)], 'fixe', dash=True, lw=0.7)
line(ax, [q, (ox, q[1])], 'fixe', dash=True, lw=0.7)
arrow(ax, (ox, oy), q, 'sujet', lw=1.3)
disc(ax, q[0], q[1], 1.2, 'sujet')
t = [math.radians(60 * k / 20) for k in range(21)]
line(ax, [(ox + 8 * math.cos(v), oy + 8 * math.sin(v)) for v in t], 'varie', lw=0.9)
text(ax, ox + 11, oy + 3.5, '60°', 'varie', 's')
text(ax, ox + 3.2, oy + 15, '2', 'sujet', 's')
text(ax, q[0], oy - 3, '1', 'fixe', 's')
text(ax, ox - 4.5, q[1], r'$\sqrt{3}$', 'fixe', 's')
X = 40
text(ax, X, 56, r'$(x,\,y)=(1,\sqrt{3})$', 'sujet', ha='left')
text(ax, X, 47, r'$a+bi=1+\sqrt{3}\,i$', 'sujet', ha='left')
text(ax, X, 38, r'$a\,\mathbf{i}+b\,\mathbf{j}=1\,\mathbf{i}+\sqrt{3}\,\mathbf{j}$', 'sujet', ha='left')
text(ax, X, 29, r'$(r,\,\theta)=(2,\,60^\circ)$', 'varie', ha='left')
text(ax, X, 20, 'même flèche, même point', 'resultat', 's', ha='left')
save(fig, '39-135')
