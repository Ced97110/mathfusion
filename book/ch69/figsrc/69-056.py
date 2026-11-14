import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'$[1,\,2]$', 'sujet', 18)
f = numberline(ax, 10, 64, 22, 0, 3, arrow_right=True)
line(ax, [(f(1), 22), (f(2), 22)], 'sujet', lw=3.0)
for v in (1, 2):
    line(ax, [(f(v), 18.5), (f(v), 25.5)], 'sujet', lw=1.4)
    disc(ax, f(v), 22, 2.0, 'sujet')
text(ax, f(1), 30, r'$a=1$', 'sujet', 's')
text(ax, f(2), 30, r'$b=2$', 'sujet', 's')
text(ax, f(1.5), 34, '1 et 2 inclus', 'resultat', 's')
save(fig, '69-056')
