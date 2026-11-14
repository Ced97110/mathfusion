import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X0, S = 4, 11.5
for i in range(5): box(ax, X0 + i*S, 38, 10, 9, 'sujet' if i < 2 else 'varie', label=r'$a$')
for i in range(2): box(ax, X0 + i*S, 14, 10, 9, 'fixe', label=r'$a$')
line(ax, [(2, 30.5), (86, 30.5)], 'encre', lw=1.2)
for i in range(2): arrow(ax, (X0 + i*S + 5, 23.5), (X0 + i*S + 5, 28.5), 'fixe', lw=0.9)
for i in range(2): arrow(ax, (X0 + i*S + 5, 37.5), (X0 + i*S + 5, 32.5), 'fixe', lw=0.9)
brace(ax, X0, X0 + 4*S + 10, 48, 'sujet', label=r'$n$ = 5 facteurs en haut', down=False)
text(ax, X0 + 5, 9, r'$m$ = 2 en bas', 'fixe', 's', ha='left')
text(ax, X0 + 4*S - 6, 23, r'$n-m=3$ restent en haut', 'varie', 's', ha='center')
text(ax, X0 + 5.8, 27.2, 'se simplifient', 'fixe', 's', ha='left') if False else None
save(fig, '14-033')
