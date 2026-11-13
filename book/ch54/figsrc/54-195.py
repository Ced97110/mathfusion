import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 56, 22, 11, 'sujet', label=r'$(p)$')
text(ax, 30, 61.5, r'= tous les multiples de $p$', 'encre', 'm', ha='left')
text(ax, 44, 46, r'$p=5$', 'fixe', 'm')
f = numberline(ax, 8, 80, 36, -10, 10, 1, arrow_right=False, every=5)
for v in range(-10, 11, 5):
    disc(ax, f(v), 36, 1.5, 'sujet')
box(ax, 2, 8, 84, 13, 'varie', label=r'$p=x^2+1$ : $(x^2+1)\,q$')
save(fig, '54-195')
