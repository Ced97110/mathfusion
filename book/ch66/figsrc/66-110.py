import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, 'φ(1) = 1 et φ(2) = 1 : vert', 'resultat', 's')
by = 30
disc(ax, 12, by, 1.5, 'fixe')
line(ax, [(28, by), (40, by)], 'fixe', lw=1.4)
disc(ax, 28, by, 1.2, 'fixe'); disc(ax, 40, by, 1.2, 'fixe')
h = 14 * math.sqrt(3) / 2
poly(ax, [(49, by - h / 2), (63, by - h / 2), (56, by + h / 2)], 'sujet')
poly(ax, [(72, by - 6), (84, by - 6), (84, by + 6), (72, by + 6)], 'sujet')
for x, t, r in [(12, '1 point', 'fixe'), (34, '2 points', 'fixe'), (56, '3 côtés', 'sujet'), (78, '4 côtés', 'sujet')]:
    text(ax, x, 20, t, r, 's')
brace(ax, 4, 41, 16, 'fixe', label='cas limites : pas polygones')
brace(ax, 48, 86, 16, 'sujet', label='polygones : au moins 3 côtés')
save(fig, '66-110')
