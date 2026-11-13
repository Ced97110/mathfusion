import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 3, 84, 50, 'fixe', fill=False)
text(ax, 62, 47, r'$O(V,B)$', 'fixe', 'l')
box(ax, 4, 6, 54, 40, 'resultat', fill=False, dash=True)
text(ax, 17, 41, r'$O^{+}(V,B)$', 'resultat', 'l')
tri = [(-5, -3), (5, -3), (-5, 3)]
def panel(cx, f, name, role, det):
    cy = 26
    line(ax, [(cx-9, cy), (cx+9, cy)], 'fixe', lw=0.5); line(ax, [(cx, cy-9), (cx, cy+9)], 'fixe', lw=0.5)
    poly(ax, [(cx+a, cy+b) for a, b in tri], 'fixe', fill=False, lw=0.8)
    poly(ax, [(cx+f(a, b)[0], cy+f(a, b)[1]) for a, b in tri], role, lw=0.8)
    text(ax, cx, 14, name, role, 's')
    text(ax, cx, 9.5, det, role, 's')
panel(17, lambda a, b: (a, b), 'rien', 'resultat', 'det 1')
panel(43, lambda a, b: (-b, a), 'quart de tour', 'resultat', 'det 1')
panel(72, lambda a, b: (a, -b), 'pli', 'limite', 'det −1')
save(fig, '72-088')
