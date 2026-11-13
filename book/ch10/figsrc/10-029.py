import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 44, 51, 'à payer : 1 976 euros', 'sujet', 'm')
f = numberline(ax, 8, 80, 24, 1940, 2010, 10, labels=False, arrow_right=False)
disc(ax, f(1976), 24, 1.5, 'sujet'); disc(ax, f(1952), 24, 1.5, 'limite'); disc(ax, f(2000), 24, 1.5, 'resultat')
arrow(ax, (f(1976) + 1, 26), (f(2000) - 1, 26), 'resultat', curve=-0.4); text(ax, 59, 38, r'$+24$ : reste', 'resultat', 's')
arrow(ax, (f(1976) - 1, 26), (f(1952) + 1, 26), 'limite', curve=0.4); text(ax, 31, 38, r'$-24$ : manque', 'limite', 's')
text(ax, f(1952), 14, 'prévu 1 952', 'limite', 's'); text(ax, f(2000) + 1, 14, 'prévu 2 000', 'resultat', 's')
save(fig, '10-029')
