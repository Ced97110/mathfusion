import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
rows = [(80, r'$u=\sqrt{2+\sqrt{3}}$', 'sujet', '2 racines carrées'),
        (55, r'$u^2=2+\sqrt{3}$', 'sujet', '1 racine carrée'),
        (30, r'$u^2-2=\sqrt{3}$', 'varie', 'racine isolée'),
        (5, r'$(u^2-2)^2=3$', 'resultat', '0 racine carrée')]
for y, s, role, n in rows:
    box(ax, 3, y, 46, 14, role, label=s, size='l')
    text(ax, 54, y + 7, n, role, 's', ha='left')
for y, lab in ((80, 'au carré'), (55, 'isoler $\\sqrt{3}$'), (30, 'au carré')):
    arrow(ax, (26, y), (26, y - 11), 'varie')
    text(ax, 30, y - 5.5, lab, 'varie', 's', ha='left')
save(fig, '61-095')
