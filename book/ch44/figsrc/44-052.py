import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx = [18, 45.5, 73]; roles = ['sujet', 'varie', 'fixe']
heads = [r'ensemble $M$', r'opération $p$', r'neutre $1$']
rows = [['ℕ', '+', '0'], [r'$M(S)$', '∘', r'$1_S$'], ['mots', 'bout à bout', 'mot vide']]
for j in range(3):
    text(ax, cx[j], 60, heads[j], roles[j], 'm', weight='bold')
for i, r in enumerate(rows):
    y = 44 - 16*i
    for j in range(3):
        box(ax, cx[j] - 12.5, y - 6, 25, 12, roles[j], label=r[j], size='m')
save(fig, '44-052')
