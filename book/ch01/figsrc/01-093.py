import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
x = lambda v: 8 + (v - 4300) * 0.72
line(ax, [(8, 38), (80, 38)], 'fixe')
for xx in (8, 80):
    line(ax, [(xx, 36.8), (xx, 39.2)], 'fixe', lw=0.8)
box(ax, 8, 41, 43.28 - 8, 6, 'resultat')
box(ax, 44, 41, 79.28 - 44, 6, 'autre')
text(ax, 25.6, 52, 'arrondi : 4 300', 'resultat', 's')
text(ax, 61.6, 52, 'arrondi : 4 400', 'autre', 's')
for v in (4301, 4349, 4350, 4399):
    disc(ax, x(v), 38, 0.9, 'fixe')
text(ax, x(4301), 33, '4 301', 'fixe', 's')
text(ax, 42.5, 33, '4 349', 'fixe', 's', ha='right')
text(ax, 45, 33, '4 350', 'fixe', 's', ha='left')
text(ax, x(4399), 33, '4 399', 'fixe', 's')
disc(ax, x(4329), 38, 1.3, 'sujet')
text(ax, x(4329), 33, '4 329', 'sujet', 's')
text(ax, 25.6, 25, 'dizaines : 0 à 4', 'resultat', 's')
text(ax, 61.6, 25, 'dizaines : 5 à 9', 'autre', 's')
brace(ax, 8, 43.28, 20, 'fixe', label='50 nombres, même arrondi')
save(fig, '01-093')
