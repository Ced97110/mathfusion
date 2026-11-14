import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1 = 32, 82
f = numberline(ax, x0, x1, 20, 0, 20, 1, every=5, arrow_right=False)
rows = [(48, 'multiples de 6', 'sujet', range(0, 21, 6)), (38, 'multiples de 10', 'autre', range(0, 21, 10)),
        (28, '$6a+10b$', 'resultat', range(0, 21, 2))]
for y, name, role, vals in rows:
    text(ax, 2, y, name, role, 's', ha='left')
    for v in vals:
        disc(ax, f(v), y, 1.2, role)
text(ax, 44, 8, '$2=2\\times6-10$ : générateur 2', 'resultat', 's')
save(fig, '56-083')
