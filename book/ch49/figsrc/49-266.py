import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
bars = [('256', 256, 'fixe'), ('64', 64, 'varie'), ('64', 64, 'varie'), ('64', 64, 'varie'), ('16', 16, 'autre'), ('16', 16, 'autre')]
x0, dx, base, sc = 12, 12.5, 30, 36 / 256
for i, (lab, v, role) in enumerate(bars):
    x = x0 + dx * i
    h = v * sc
    box(ax, x - 4, base, 8, h, role, r=0.3)
    text(ax, x, base + h + 3, lab, role, 's')
line(ax, [(5, base), (83, base)], 'fixe', lw=0.8)
text(ax, x0, base - 4, 'neutre', 'fixe', 's')
text(ax, x0 + 2 * dx, base - 4, '3 échanges', 'varie', 's')
text(ax, x0 + 4.5 * dx, base - 4, '2 tours', 'autre', 's')
text(ax, 60, 78, 'fonctions fixes', 'encre', 's')
text(ax, 44, 16, r'$256+3\times64+2\times16=480$', 'encre', 'm')
text(ax, 44, 6, r'$480\div6=80$ circuits', 'resultat', 'l')
save(fig, '49-266')
