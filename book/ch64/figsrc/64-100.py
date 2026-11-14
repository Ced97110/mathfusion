import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
RO = {2: 'sujet', 3: 'varie', 5: 'resultat'}
rows = [(40, 'suite 1', [3, 5, 2, 2]), (14, 'suite 2', [2, 2, 5, 3])]
for y, cap, fs in rows:
    text(ax, 5, y + 13, cap, 'encre', 's', ha='left')
    for k, f in enumerate(fs):
        box(ax, 8 + k * 19.5, y, 16, 9, RO[f], label=str(f), size='l')
    brace(ax, 8, 8 + 3 * 19.5 + 16, y, 'fixe', label=r'$%s=60$' % r'\times'.join(map(str, fs)))
text(ax, 44, 2.5, 'deux suites seulement : un exemple', 'fixe', 's')
save(fig, '64-100')
