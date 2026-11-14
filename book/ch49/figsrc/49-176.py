import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def square(cx, cy, s, diag, fixed):
    pts = {'A': (cx - s, cy - s), 'B': (cx + s, cy - s), 'C': (cx + s, cy + s), 'D': (cx - s, cy + s)}
    poly(ax, list(pts.values()), 'fixe')
    a, b = diag
    line(ax, [pts[a], pts[b]], 'varie', lw=1.3, dash=True)
    for k, (x, y) in pts.items():
        dx = -3.2 if x < cx else 3.2; dy = -3.2 if y < cy else 3.2
        if k == fixed: disc(ax, x, y, 1.6, 'sujet')
        text(ax, x + dx, y + dy, k, 'sujet' if k == fixed else 'fixe', 'm', weight='bold' if k == fixed else 'normal')
for cx, diag, fx, lab in [(23, 'AC', 'A', r'Stab $A$ = {1, axe $AC$}'), (65, 'BD', 'B', r'Stab $B$ = {1, axe $BD$}')]:
    square(cx, 36, 11, diag, fx)
    text(ax, cx, 12, lab, 'sujet', 's')
    text(ax, cx, 6, '2 éléments', 'resultat', 's')
save(fig, '49-176')
