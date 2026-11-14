import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
for i, (e, k) in enumerate([(r'$x+5=12$', 1), (r'$x^2+4x=30$', 2), (r'$x^3=8$', 3)]):
    y = 70 - i * 12; role = 'sujet' if k == 2 else 'fixe'
    text(ax, 2, y + 4.5, f'exposant {k}', role, 's', ha='left')
    box(ax, 24, y, 40, 9, role, True, label=e)
text(ax, 67, 70 - 12 + 4.5, 'second degré', 'sujet', 's', ha='left')
for x, w, s, sub in [(6, 26, r'$ax^2$', r'terme en $x^2$'), (32, 24, r'$+\,bx$', r'terme en $x$'), (56, 26, r'$+\,c=0$', 'nombre seul')]:
    box(ax, x, 20, w, 10, 'sujet', True, label=s)
    text(ax, x + w / 2, 13, sub, 'sujet', 's')
text(ax, 19, 6, r'$a\neq0$', 'encre', 's')
save(fig, '23-014')
