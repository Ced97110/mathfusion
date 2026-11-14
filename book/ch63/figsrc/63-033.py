import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$\mathrm{Gal}(E/F)=\{1,\tau\}$ : table de $\circ$', 'sujet', 'm', weight='bold')
x0, cw, ch = 20, 16, 10
cols = [x0 + cw * i for i in range(3)]
rows = [50, 40, 30]
box(ax, cols[0], rows[0], cw, ch, 'fixe', label=r'$\circ$')
heads = ['1', r'$\tau$']
for i, h in enumerate(heads):
    box(ax, cols[i + 1], rows[0], cw, ch, 'sujet', label=h)
    box(ax, cols[0], rows[i + 1], cw, ch, 'sujet', label=h)
table = [['1', r'$\tau$'], [r'$\tau$', '1']]
for r in range(2):
    for c in range(2):
        if r == 1 and c == 1: role = 'varie'
        elif r == 0 or c == 0: role = 'fixe'
        else: role = 'resultat'
        box(ax, cols[c + 1], rows[r + 1], cw, ch, role, label=table[r][c])
text(ax, 8, 22, r'gris : $1$ ne change rien (identité)', 'fixe', 's', ha='left')
text(ax, 8, 14, r'toute case est $1$ ou $\tau$ (composée)', 'resultat', 's', ha='left')
text(ax, 8, 6, r'orange : $\tau\circ\tau=1$ (inverse de $\tau$)', 'varie', 's', ha='left')
save(fig, '63-033')
