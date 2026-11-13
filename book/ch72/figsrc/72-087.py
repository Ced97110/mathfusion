import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 2, 4, 84, 44, 'sujet', fill=False, dash=True)
text(ax, 44, 43, r'$O(V,B)$', 'sujet', 'l')
tri = [(-6, -3), (6, -3), (-6, 4)]
def panel(cx, f, name):
    cy = 24
    line(ax, [(cx-11, cy), (cx+11, cy)], 'fixe', lw=0.5); line(ax, [(cx, cy-11), (cx, cy+11)], 'fixe', lw=0.5)
    poly(ax, [(cx+a, cy+b) for a, b in tri], 'fixe', fill=False, lw=0.8)
    poly(ax, [(cx+f(a, b)[0], cy+f(a, b)[1]) for a, b in tri], 'sujet', lw=0.8)
    text(ax, cx, 10, name, 'sujet', 's')
panel(18, lambda a, b: (a, b), 'ne rien faire')
panel(44, lambda a, b: (-b, a), 'quart de tour')
panel(70, lambda a, b: (a, -b), 'pli')
save(fig, '72-087')
