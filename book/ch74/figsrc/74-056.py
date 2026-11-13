import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def F(ox, oy, s, role, f=lambda p: p):
    segs = [[(0, 0), (0, 6)], [(0, 6), (3.2, 6)], [(0, 3.3), (2.4, 3.3)]]
    for sg in segs:
        pts = [f(p) for p in sg]
        line(ax, [(ox + s * x, oy + s * y) for x, y in pts], role, lw=1.5)
rot = lambda p: (-p[1], p[0])
mir = lambda p: (-p[0], p[1])
mirup = lambda p: (-p[0], p[1] + 6)
box(ax, 2, 3, 41, 83, 'sujet', fill=False); box(ax, 45, 3, 41, 83, 'autre', fill=False)
text(ax, 22.5, 80, r'$\det A=1$', 'sujet', 'l'); text(ax, 65.5, 80, r'$\det A=-1$', 'autre', 'l')
s = 1.0
rows = [(60, 'translation', 'réflexion'), (38, 'rotation', 'symétrie glissée')]
# left column
F(8, 56, s, 'sujet'); arrow(ax, (18, 59), (27, 59), 'varie', lw=0.8); F(30, 62, s, 'varie')
text(ax, 22.5, 50, 'translation', 'encre', 's')
F(8, 29, s, 'sujet'); arrow(ax, (18, 32), (24, 32), 'varie', lw=0.8); F(40, 28, s, 'varie', rot)
text(ax, 22.5, 25.5, 'rotation', 'encre', 's')
text(ax, 22.5, 9, 'se lit encore', 'sujet', 'm')
# right column (mirror: F reversed)
F(52, 56, s, 'sujet'); arrow(ax, (62, 59), (71, 59), 'varie', lw=0.8); F(80, 56, s, 'varie', mir)
text(ax, 65.5, 50, 'réflexion', 'encre', 's')
F(52, 29, s, 'sujet'); arrow(ax, (62, 32), (70, 35), 'varie', lw=0.8); F(80, 33, s, 'varie', mir)
text(ax, 65.5, 25.5, 'symétrie glissée', 'encre', 's')
text(ax, 65.5, 9, 'retourne la figure', 'autre', 'm')
save(fig, '74-056')
