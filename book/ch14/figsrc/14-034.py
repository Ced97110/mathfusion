import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
X0, S = 18, 10.5
for i in range(5): box(ax, X0 + i*S, 34, 9, 9, 'varie' if i < 2 else 'fixe', label=r'$a$')
for i in range(2): box(ax, X0 + i*S, 17, 9, 9, 'varie', label=r'$a$')
line(ax, [(14, 30), (74, 30)], 'encre', lw=1.2)
for i in range(2): line(ax, [(X0 + i*S + 4.5, 33), (X0 + i*S + 4.5, 27)], 'varie', dash=True)
brace(ax, X0, X0 + S + 9, 16, 'varie', label=r'$m$ = 2 facteurs annulés')
text(ax, X0 + 2*S, 48, 'non annulés', 'fixe', 's', ha='left')
save(fig, '14-034')
