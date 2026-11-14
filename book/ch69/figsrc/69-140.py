import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
text(ax, 44, 99, 'une variable : points isolés', 'fixe', 's')
line(ax, [(8, 90), (80, 90)], 'fixe')
for x, lab in [(14, 'a'), (66, 'b')]:
    line(ax, [(x, 88.5), (x, 91.5)], 'fixe')
    text(ax, x, 85, lab, 'fixe', 's')
for x in [28, 41, 57]:
    disc(ax, x, 90, 1.5, 'sujet')
cx, cy, R = 44, 42, 26
line(ax, [(6, cy), (82, cy)], 'fixe', lw=0.5)
line(ax, [(cx, 12), (cx, 70)], 'fixe', lw=0.5)
disc(ax, cx, cy, R, 'sujet', fill=False, lw=1.8)
for x, y in [(cx + R, cy), (cx, cy + R), (cx - R, cy)]:
    disc(ax, x, y, 1.7, 'resultat')
text(ax, cx + R + 1.5, cy + 4, r'$(1,0)$', 'resultat', 's', ha='left')
text(ax, cx, cy + R + 4, r'$(0,1)$', 'resultat', 's')
text(ax, cx - R - 1.5, cy + 4, r'$(-1,0)$', 'resultat', 's', ha='right')
text(ax, 44, 6, r'$x^2+y^2-1=0$ : cercle entier', 'sujet', 's')
save(fig, '69-140')
