import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
for x, e, k, name in [(15, r'$x+3=8$', 1, 'premier degré'), (44, r'$x^2=49$', 2, 'second degré'), (73, r'$x^3=27$', 3, 'troisième degré')]:
    role = 'sujet' if k == 2 else 'fixe'
    text(ax, x, 62, e, role, 'l')
    arrow(ax, (x, 57), (x, 49), role)
    disc(ax, x, 42, 5, role, True, label=str(k), size='l')
    text(ax, x, 31, name, role, 's')
text(ax, 44, 14, 'un seul terme, degré 2', 'sujet', 'm')
save(fig, '23-016')
