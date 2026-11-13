import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, y0, s = 16, 18, 14
vals = [['3', '1'], ['5', '2']]
for i, r in enumerate(vals):
    for j, v in enumerate(r): box(ax, x0 + j * (s + 1), y0 + (1 - i) * (s + 1), s, s, 'sujet', label=v, size='l')
for j in range(2): text(ax, x0 + j * (s + 1) + s / 2, y0 + 2 * s + 5, f'colonne {j + 1}', 'varie', 's')
for i in range(2): text(ax, x0 + 2 * s + 4, y0 + (1 - i) * (s + 1) + s / 2, f'ligne {i + 1}', 'varie', 's', ha='left')
text(ax, 44, 8, r'2 lignes $\times$ 2 colonnes = 4 nombres', 'sujet', 'm')
save(fig, '42-252')
