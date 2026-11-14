import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 8, 70, 20, 0, 2, 1)
disc(ax, f(1), 20, 2.2, 'resultat')
text(ax, f(1), 29, r'$5^0 = 1$', 'resultat', weight='bold')
box(ax, 46, 42, 38, 12, 'limite', dash=True, label=r'$0^0 = 0\ /\ 0$')
text(ax, 65, 37, 'pas un nombre', 'limite', 's')
save(fig, '14-040')
