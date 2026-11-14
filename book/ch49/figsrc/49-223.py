import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def sq(x0, y0, pos):
    for i in range(2):
        for j in range(2): box(ax, x0 + i * 9, y0 + j * 9, 9, 9, 'fixe', r=0.3, lw=0.6)
    px, py = {'hd': (1, 1), 'hg': (0, 1)}[pos]
    disc(ax, x0 + px * 9 + 4.5, y0 + py * 9 + 4.5, 3.2, 'varie')
box(ax, 4, 16, 80, 30, 'sujet', fill=False, dash=True, r=1.5)
text(ax, 44, 41, 'même orbite', 'sujet', 'm')
sq(14, 18, 'hd'); sq(56, 18, 'hg')
text(ax, 23, 11, 'départ', 'fixe', 's')
text(ax, 65, 11, 'après', 'fixe', 's')
arrow(ax, (34, 29), (53, 29), 'varie')
text(ax, 44, 33.5, 'quart de tour', 'varie', 's')
text(ax, 44, 4, 'compte pour une seule', 'resultat', 'm')
save(fig, '49-223')
