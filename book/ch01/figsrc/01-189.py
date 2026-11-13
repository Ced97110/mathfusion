import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
cx = lambda i: 14 + 9 * i
role = {0: 'limite', 7: 'limite', 2: 'resultat', 4: 'resultat', 6: 'resultat'}
line(ax, [(9, 14), (cx(0) - 3.2, 14)], 'fixe')
for i in range(7):
    line(ax, [(cx(i) + 3.2, 14), (cx(i + 1) - 3.2, 14)], 'fixe')
arrow(ax, (cx(7) + 3.2, 14), (86, 14), 'fixe', lw=0.9)
for i in range(8):
    r = role.get(i, 'fixe')
    disc(ax, cx(i), 14, 3.2, r, label=str(i), size='m', lw=1.2 if r == 'limite' else 0.8)
text(ax, 5, 14, 'ℕ', 'fixe', 'l')
box(ax, 22, 34, 50, 14, 'sujet')
for x, s in [(32, '2'), (50, '4'), (68, '6')]:
    disc(ax, x, 41, 3.5, 'sujet', label=s, size='m')
    arrow(ax, (x, 37.5), (x, 17.5), 'resultat')
text(ax, 47, 51, 'collection', 'sujet', 'm')
text(ax, 44, 5, '0 et 7 manquent', 'limite', 's')
save(fig, '01-189')
