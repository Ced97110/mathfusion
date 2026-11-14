import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
rows = [('$4\\quad6$\n$6\\quad4$', 'sujet', 'facteurs 2, 10', 48),
        ('$2\\quad0$\n$0\\quad10$', 'sujet', 'facteurs 2, 10', 26),
        ('$1\\quad0$\n$0\\quad20$', 'autre', 'facteurs 1, 20', 4)]
for lab, role, fac, y in rows:
    box(ax, 3, y, 22, 16, role, label=lab, size='s')
    arrow(ax, (26.5, y + 8), (33.5, y + 8), role)
    box(ax, 35, y + 2, 24, 12, 'resultat' if role == 'sujet' else 'autre', label=fac, size='s')
line(ax, [(62, 34), (65, 34), (65, 56), (62, 56)], 'resultat')
text(ax, 75, 45, 'équivalentes', 'resultat', 's')
text(ax, 75, 12, 'pas équivalente', 'autre', 's')
save(fig, '59-092')
