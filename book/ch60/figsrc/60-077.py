import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, 'ann z = (4)', 'resultat', 'l')
text(ax, 44, 40, 'z = 3 dans ℤ/12', 'sujet', 'm')
f = numberline(ax, 8, 80, 14, 0, 12, step=1, labels=False, arrow_right=False)
for v in (0, 4, 8, 12):
    disc(ax, f(v), 24, 2, 'resultat')
    text(ax, f(v), 30, str(v), 'resultat', 'm')
    line(ax, [(f(v), 22), (f(v), 15.5)], 'resultat', dash=True)
text(ax, 44, 4, '4 × 3 = 12, qui revient à 0', 'encre', 's')
save(fig, '60-077')
