import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
panels = [('se croisent', 'un point'), ('parallèles\ndistinctes', 'aucun point'), ('confondues', 'une infinité')]
for i, (h, c) in enumerate(panels):
    px = 2 + i * 29
    box(ax, px, 18, 27, 36, 'fixe', fill=False, lw=0.6)
    text(ax, px + 13.5, 62, h, 'encre', 's')
    text(ax, px + 13.5, 11, c, 'resultat' if i != 1 else 'encre', 's')
    if i == 0:
        line(ax, [(px + 3, 22), (px + 24, 50)], 'sujet', lw=1.2); line(ax, [(px + 3, 50), (px + 24, 22)], 'autre', lw=1.2)
        disc(ax, px + 13.5, 36, 1.6, 'resultat')
    elif i == 1:
        line(ax, [(px + 3, 22), (px + 24, 44)], 'sujet', lw=1.2); line(ax, [(px + 3, 30), (px + 24, 52)], 'autre', lw=1.2)
    else:
        pts = [(px + 3, 50), (px + 24, 22)]
        line(ax, pts, 'sujet', lw=1.4); line(ax, pts, 'autre', lw=1.4, dash=True)
        disc(ax, px + 6, 46, 1.6, 'resultat'); disc(ax, px + 21, 26, 1.6, 'resultat')
        text(ax, px + 14, 46.5, r'$(0,\,5)$', 'resultat', 's'); text(ax, px + 14, 21, r'$(5,\,0)$', 'resultat', 's')
save(fig, '24-025')
