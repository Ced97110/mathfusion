import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy, u = 44, 38, 14
s5 = 5 ** 0.5
for a in range(-2, 3):
    for b in (-1, 0, 1):
        disc(ax, ox + a * u, oy + b * s5 * u, 1.0, 'fixe')
disc(ax, ox, oy, 2 ** 0.5 * u, 'limite', fill=False, lw=1.0)
disc(ax, ox, oy, 3 ** 0.5 * u, 'limite', fill=False, lw=1.0)
disc(ax, ox, oy, 1.3, 'encre')
text(ax, ox, oy - 3.6, '0', 'encre', 's')
text(ax, ox + u, oy - 3.6, '1', 'fixe', 's')
text(ax, ox + 2 * u, oy - 3.6, '2', 'fixe', 's')
text(ax, ox, oy + s5 * u + 4, '2,24', 'fixe', 's')
text(ax, ox + u, oy + s5 * u + 4, '2,45', 'fixe', 's')
c = math.cos(math.radians(45))
p2 = (ox + 2 ** 0.5 * u * c, oy + 2 ** 0.5 * u * c)
p3 = (ox - 3 ** 0.5 * u * c, oy + 3 ** 0.5 * u * c)
text(ax, ox, oy + 9, 'rayon √2 ≈ 1,41', 'limite', 's')
line(ax, [(18, 62), p3], 'limite')
text(ax, 17, 64, 'rayon √3 ≈ 1,73', 'limite', 's')
save(fig, '56-015')
