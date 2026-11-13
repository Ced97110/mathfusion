import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = numberline(ax, 6, 82, 14, 0, 24, step=3, arrow_right=False)
for v in range(0, 25, 3):
    role = 'varie' if v in (12, 21) else ('resultat' if v == 9 else 'sujet')
    disc(ax, f(v), 14, 1.6, role)
arrow(ax, (f(21), 17), (f(12), 17), 'varie', curve=0.45)
text(ax, f(16.5), 31, '21 − 12 = 9', 'resultat', 'l')
text(ax, 44, 40, '3ℤ : les multiples de 3', 'sujet', 'm')
text(ax, 44, 3, '9 est encore un multiple de 3', 'resultat', 's')
save(fig, '46-260')
