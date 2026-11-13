import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
y = 54
items = [(4, 14, 'fixe', r'$17$'), (26, 10, 'sujet', r'$5$'), (46, 10, 'varie', r'$0$'), (66, 14, 'varie', r'$17$')]
for x, w, role, lab in items:
    box(ax, x, y, w, 9, role, label=lab, weight='bold')
text(ax, 20.5, y + 4.5, '=', 'encre', 'l')
text(ax, 38, y + 4.5, r'$\times$', 'encre', 'l')
text(ax, 58, y + 4.5, '+', 'encre', 'l')
text(ax, 44, y + 13, r'$q=0$, $r=a$ : toujours possible', 'varie', 's')
text(ax, 44, y - 5, 'égalité vraie, mais elle', 'resultat', 's')
text(ax, 44, y - 9, 'est vraie pour tout $a$, $b$', 'resultat', 's')
# tailles : delta(r)=17 contre delta(b)=5 (2,6 mm par unité)
u = 2.6
text(ax, 4, 28, r'$\delta(r)=17$', 'varie', 's', ha='left')
box(ax, 26, 25, 17 * u, 6, 'varie')
text(ax, 4, 17, r'$\delta(b)=5$', 'sujet', 's', ha='left')
box(ax, 26, 14, 5 * u, 6, 'sujet')
text(ax, 44, 5, r'$17<5$ : faux, couple écarté', 'limite', 's')
save(fig, '56-122')
