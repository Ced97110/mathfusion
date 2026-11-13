import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [('quelconque', (6, 1), (1.5, 4.5)), ('rectangle', (6, 0), (0, 4.5)), ('losange', (5.5, 0), (1.4, 5.3)),
        ('carré', (5.5, 0), (0, 5.5)), ('hexagonal', (5.5, 0), (2.75, 4.76))]
text(ax, 62, 76, 'ordre 4', 'sujet', 's'); text(ax, 80, 76, 'ordres 3, 6', 'sujet', 's')
def mark(x, y, ok):
    if ok:
        line(ax, [(x-2, y), (x-0.6, y-1.8), (x+2.2, y+2)], 'resultat', lw=1.6)
    else:
        line(ax, [(x-1.8, y-1.8), (x+1.8, y+1.8)], 'limite', lw=1.6); line(ax, [(x-1.8, y+1.8), (x+1.8, y-1.8)], 'limite', lw=1.6)
for k, (name, a, b) in enumerate(rows):
    y = 62 - k*13.5
    ox = 4
    P = lambda i, j: (ox + i*a[0]*0.8 + j*b[0]*0.8, y - 4 + i*a[1]*0.8 + j*b[1]*0.8)
    poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'varie')
    for i in range(3):
        for j in range(2):
            disc(ax, P(i, j)[0], P(i, j)[1], 0.7, 'sujet')
    text(ax, 30, y, name, 'sujet', 's', ha='left')
    mark(62, y, name == 'carré'); mark(80, y, name == 'hexagonal')
save(fig, '74-142')
