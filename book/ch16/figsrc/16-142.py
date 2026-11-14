import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'3 ÷ ($x$ − 2) = 5', 'sujet', 'l')
f = numberline(ax, 10, 70, 14, 0, 5, 1, arrow_right=False, size='m')
disc(ax, f(2), 14, 1.8, 'limite'); text(ax, f(2) - 1, 25, r'$x$ ≠ 2 : diviseur 0', 'limite', 's', ha='right')
line(ax, [(f(2), 16), (f(2), 22)], 'limite', dash=True)
disc(ax, f(2.6), 14, 1.8, 'resultat'); text(ax, f(2.6) + 1, 25, r'$x$ = 2,6', 'resultat', 's', ha='left')
line(ax, [(f(2.6), 16), (f(2.6), 22)], 'resultat', dash=True)
save(fig, '16-142')
