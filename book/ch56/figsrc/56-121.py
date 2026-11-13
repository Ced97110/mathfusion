import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# 17 = 5 x 3 + 2
items = [(4, 14, 'fixe', r'$17$', r'$a$'), (26, 10, 'sujet', r'$5$', r'$b$ non nul'),
         (46, 10, 'varie', r'$3$', r'$q$'), (66, 10, 'resultat', r'$2$', r'$r$')]
y = 46
for x, w, role, lab, name in items:
    box(ax, x, y, w, 9, role, label=lab, weight='bold')
    text(ax, x + w / 2, y - 4, name, role, 's')
text(ax, 20.5, y + 4.5, '=', 'encre', 'l')
text(ax, 38, y + 4.5, r'$\times$', 'encre', 'l')
text(ax, 58, y + 4.5, '+', 'encre', 'l')
# size bars: delta(r)=2, delta(b)=5 (3.5 mm par unité)
u = 4.0
text(ax, 4, 26, r'$\delta(r)=2$', 'resultat', 's', ha='left')
box(ax, 30, 23, 2 * u, 6, 'resultat')
text(ax, 4, 14, r'$\delta(b)=5$', 'sujet', 's', ha='left')
box(ax, 30, 11, 5 * u, 6, 'sujet')
text(ax, 30 + 5 * u + 6, 20, r'$2<5$', 'resultat', 'm', ha='left')
save(fig, '56-121')
