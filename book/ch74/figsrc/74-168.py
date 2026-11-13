import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
t = 6.6
def dia(x, y): poly(ax, [(x-1.9, y), (x, y+2.6), (x+1.9, y), (x, y-2.6)], 'sujet')
for k, ox in enumerate([3, 33, 63]):
    for i in range(4):
        line(ax, [(ox, 12 + i*t), (ox + 3*t, 12 + i*t)], 'fixe', lw=0.5)
        line(ax, [(ox + i*t, 12), (ox + i*t, 12 + 3*t)], 'fixe', lw=0.5)
    if k != 1:
        for i in range(4):
            for j in range(4): dia(ox + i*t, 12 + j*t)
    if k != 0:
        for i in range(3):
            for j in range(3): disc(ax, ox + (i+.5)*t, 12 + (j+.5)*t, 2.0, 'resultat')
text(ax, 29, 28, '+', 'encre', 'xl')
text(ax, 58.5, 28, '=', 'encre', 'xl')
text(ax, 12.9, 6, 'losanges bleus', 'sujet', 's')
text(ax, 42.9, 6, 'disques verts', 'resultat', 's')
text(ax, 72.9, 6, 'le dessin', 'encre', 's')
text(ax, 44, 41, 'deux sortes de marques', 'encre', 'm')
save(fig, '74-168')
