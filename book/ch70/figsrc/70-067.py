import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 45, r'$\exists\,y,\ y^2=9$', 'sujet', 'xl')
f = numberline(ax, 12, 72, 22, 0, 5, arrow_right=False)
disc(ax, f(3), 22, 1.6, 'resultat')
arrow(ax, (f(3), 30), (f(3), 24.5), 'resultat')
text(ax, f(3), 33, r'$3^2=9$', 'resultat', 'm')
text(ax, 44, 8, 'un seul exemple suffit', 'resultat', 's')
save(fig, '70-067')
