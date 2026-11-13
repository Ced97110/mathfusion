import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 54, 64, r'$f(1+1)$', 'sujet', 's'); text(ax, 76, 64, r'$f(1)+f(1)$', 'autre', 's')
rows = [('reste mod 4', '2', '2', True), ('tout sur 0', '0', '0', True), ('pair 0, impair 1', '0', '2', False)]
for i, (nom, a, b, ok) in enumerate(rows):
    y = 50 - i * 20
    role = 'resultat' if ok else 'limite'
    box(ax, 2, y - 6, 34, 12, role, label=nom, size='s')
    box(ax, 44, y - 5, 20, 10, 'sujet', label=a)
    box(ax, 68, y - 5, 18, 10, 'autre', label=b)
    text(ax, 40, y, '=' if ok else '≠', role, 'l', weight='bold')
save(fig, '48-018')
