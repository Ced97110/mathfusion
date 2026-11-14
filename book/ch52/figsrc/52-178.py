import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$a \equiv a_1 \ (\mathrm{mod}\ I_1)$', 'sujet', 'l')
f = numberline(ax, 8, 76, 24, 0, 12, arrow_right=False)
for v in (3, 7, 11): disc(ax, f(v), 24, 1.5, 'sujet')
disc(ax, f(10), 24, 1.5, 'limite')
for a, b in ((3, 7), (7, 11)):
    arrow(ax, (f(a), 26.5), (f(b), 26.5), 'varie', curve=-0.5)
    text(ax, f((a + b) / 2), 34, '+ 4', 'varie', 's')
text(ax, 44, 12, '11 − 3 = 8 : multiple de 4', 'resultat', 's')
text(ax, 44, 5, '10 − 3 = 7 : pas multiple de 4', 'limite', 's')
save(fig, '52-178')
