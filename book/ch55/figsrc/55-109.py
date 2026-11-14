import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
f = numberline(ax, 8, 68, 70, 0, 5, labels=False)
for i, v in enumerate((1, 2, 4)):
    disc(ax, f(v), 70, 2.0, 'sujet')
    text(ax, f(v), 76.5, rf'$x_{i + 1}={v}$', 'sujet', 's')
rows = [(48, r'$(1-2)^2=1$', r'$(x_1,\,x_2)$'),
        (35, r'$(1-4)^2=9$', r'$(x_1,\,x_3)$'),
        (22, r'$(2-4)^2=4$', r'$(x_2,\,x_3)$')]
for y, lab, tag in rows:
    box(ax, 3, y, 40, 10, 'sujet', label=lab)
    text(ax, 48, y + 5, tag, 'fixe', 's', ha='left')
box(ax, 3, 4, 82, 12, 'resultat', label=r'$\Delta=1\times 9\times 4=36$', size='l', weight='bold')
save(fig, '55-109')
