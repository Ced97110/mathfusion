import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def square(cx, cy, orange):
    s = 8
    pts = [(cx - s, cy + s), (cx - s, cy - s), (cx + s, cy - s), (cx + s, cy + s)]
    poly(ax, pts, 'fixe', fill=False)
    for n, (x, y) in zip('ABCD', pts):
        disc(ax, x, y, 3.2, 'varie' if n in orange else 'sujet', label=n, size='s')
text(ax, 22, 67, 'coloration', 'encre', 's'); text(ax, 70, 67, 'partie', 'encre', 's')
for cy, orange, lab in [(50, 'A', r'$\{A\}$'), (24, '', r'$\varnothing$')]:
    square(22, cy, orange)
    arrow(ax, (38, cy), (56, cy), 'encre', both=True)
    text(ax, 70, cy, lab, 'varie' if orange else 'sujet', 'l')
text(ax, 70, 34, 'sommets orange', 'varie', 's') if False else None
text(ax, 44, 4.5, '16 colorations = 16 parties', 'resultat', 's')
save(fig, '49-124')
