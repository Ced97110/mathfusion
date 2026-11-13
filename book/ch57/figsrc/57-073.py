import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$a,\ b\in R$', 'sujet', 'l', weight='bold')
text(ax, 44, 41, 'ici a = 3 et b = 2', 'varie', 's')
f = numberline(ax, 8, 68, 20, 0, 6, arrow_right=True)
for v, s in [(2, '$b$'), (3, '$a$')]:
    disc(ax, f(v), 30, 3, 'varie', label=s)
    line(ax, [(f(v), 27), (f(v), 21.5)], 'varie', dash=True)
brace(ax, 8, 73, 12, 'fixe', label='R = ℤ : les coefficients', down=True)
save(fig, '57-073')
