import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 44, 49, r'$p^4 - 7p^3 - 2p - 11$', 'sujet', 'l')
ws = [14, 18, 16, 16]; labs = [r'$p^4$', r'$-7p^3$', r'$-2p$', r'$-11$']
x = 4
for wi, s in zip(ws, labs):
    box(ax, x, 26, wi, 11, 'sujet', label=s); x += wi + 5.5
    if x < 80: line(ax, [(x - 2.75, 23), (x - 2.75, 40)], 'varie', dash=True)
brace(ax, 4, 4 + sum(ws) + 16.5, 24, 'resultat', 'quatre termes', size='m')
text(ax, 11, 42, 'sans signe : $+$', 'fixe', 's', ha='left')
save(fig, '15-026')
