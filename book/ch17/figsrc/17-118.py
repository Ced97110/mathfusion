import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$x^2 \leq 0$', 'sujet', 'l')
f = numberline(ax, 10, 70, 20, -2, 2, arrow_right=True)
for v, role, t in ((-1, 'limite', r'$(-1)^2=1$'), (0, 'resultat', r'$0^2=0$'), (1, 'limite', r'$1^2=1$')):
    disc(ax, f(v), 20, 1.5, role)
    text(ax, f(v), 29, t, role, 's')
    text(ax, f(v), 25, 'faux' if role == 'limite' else 'vrai', role, 's')
text(ax, 44, 4, 'une seule solution : 0', 'resultat', 'm', weight='bold')
save(fig, '17-118')
