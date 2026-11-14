import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cx, cy, R = 44, 48, 26
def pos(k, rad=R):
    t = math.radians(90 - 24 * k)
    return cx + rad * math.cos(t), cy + rad * math.sin(t)
tri = [0, 5, 10]
assert [k for k in range(15) if (3 * k) % 15 == 0] == tri
line(ax, [pos(k) for k in tri + [0]], 'resultat', lw=1.0)
for k in range(15):
    x, y = pos(k)
    if k in tri:
        disc(ax, x, y, 4.0, 'resultat')
    else:
        disc(ax, x, y, 2.6, 'fixe')
for k, s in [(0, r'$\alpha^0=1$'), (5, r'$\alpha^5=\beta$'), (10, r'$\alpha^{10}=\beta^2$')]:
    x, y = pos(k, R + 9)
    text(ax, x, y, s, 'resultat', 's')
text(ax, 44, 52, r'$u^3=1$', 'resultat')
text(ax, 44, 45, r'15 divise $3k$', 'fixe', 's')
text(ax, 44, 11, r'$\mathbb{F}_4=\{0,1,\alpha^5,\alpha^{10}\}$', 'resultat')
text(ax, 44, 4, r'$\beta^2=\beta+1$', 'resultat')
save(fig, '67-180')
