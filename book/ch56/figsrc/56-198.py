import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
u = 20
S3 = math.sqrt(3)
text(ax, 22, 79, r'$\mathbb{Z}[i]$', 'sujet', 'l')
text(ax, 66, 79, r'$\mathbb{Z}[\sqrt{3}\,i]$', 'sujet', 'l')
for (cx0, cy0, w, h, role) in [(12, 24, 1, 1, 'resultat'), (54, 24, 1, S3, 'limite')]:
    corners = [(cx0, cy0), (cx0 + w * u, cy0), (cx0 + w * u, cy0 + h * u), (cx0, cy0 + h * u)]
    poly(ax, corners, 'sujet', fill=False, lw=1.0)
    for p in corners:
        disc(ax, p[0], p[1], 1.2, 'sujet')
    zx, zy = cx0 + w * u / 2, cy0 + h * u / 2
    disc(ax, zx, zy, 1.0, 'varie')
    arrow(ax, (zx, zy), (cx0, cy0), role, lw=1.0)
text(ax, 22, 19.5, r'distance $\approx0{,}71$', 'resultat', 's')
text(ax, 64, 19.5, r'distance $1$', 'limite', 's')
box(ax, 4, 4, 38, 11, 'resultat', label='moins de 1 : marche', size='s')
box(ax, 46, 4, 38, 11, 'limite', label='égal à 1 : échec', size='s')
save(fig, '56-198')
