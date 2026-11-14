import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'$(\mathbb{Z},\,\times,\,1)$', 'sujet', 'xl')
text(ax, 80, 54, 'se défait ?', 'fixe', 's', ha='right')
rows = [('sujet', '−1', r'$(-1)\times(-1)=1$', True), ('sujet', '1', r'$1\times 1=1$', True), ('limite', '2', r'$2\times ?=1$', False)]
for i, (role, n, eq, ok) in enumerate(rows):
    y = 38 - i * 15
    disc(ax, 9, y + 5, 5, role, label=n, size='l')
    box(ax, 18, y, 46, 10, 'resultat' if ok else 'limite', label=eq, size='m')
    text(ax, 76, y + 5, '✓' if ok else '✗', 'resultat' if ok else 'limite', 'xl')
save(fig, '44-072')
