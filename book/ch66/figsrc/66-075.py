import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'coefficient de la plus haute puissance', 'encre', 's')
rows = [(r'$u=\sqrt{2}$', '1', 'resultat', r'$x^2-2$', 'dominant 1 : unitaire', 'entier algébrique'),
        (r'$u=\frac{1}{2}$', '2', 'limite', r'$x-1$', 'dominant 2 : pas 1', 'algébrique seulement')]
for k, (u, c, role, rest, cap, tag) in enumerate(rows):
    y = 40 - k * 26
    text(ax, 2, y + 5, u, 'sujet', 'm', ha='left')
    box(ax, 30, y, 9, 10, role, label=c, size='l')
    text(ax, 41, y + 5, rest, 'encre', 'l', ha='left')
    text(ax, 30, y - 5, cap, role, 's', ha='left')
    text(ax, 30, y - 11, tag, role, 's', ha='left')
save(fig, '66-075')
