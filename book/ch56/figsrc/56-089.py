import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = [(70, 'sujet', r'$5\mid30=3\times10$, $5\nmid3$'),
         (51, 'varie', r'$2\times5+(-3)\times3=1$'),
         (32, 'sujet', r'$\times10$ : $100+(-90)=10$'),
         (13, 'resultat', r'$100=5\times20$ ; $-90=5\times(-18)$')]
for y, role, lab in steps:
    box(ax, 3, y, 82, 12, role, label=lab)
for y in (70, 51, 32):
    arrow(ax, (30, y - 0.5), (30, y - 6.5), 'fixe')
text(ax, 36, 66.5, 'étape décisive : 1', 'varie', 's', ha='left')
text(ax, 44, 5, '$5$ divise $10$', 'resultat', 'l')
save(fig, '56-089')
