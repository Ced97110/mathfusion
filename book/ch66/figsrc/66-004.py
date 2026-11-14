import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
y = 26
for i, n in enumerate([3, 4, 5, 6, 7]):
    ok = n != 7
    box(ax, 4 + 11 * i, y, 9, 9, 'resultat' if ok else 'fixe', label=str(n), dash=not ok)
text(ax, 62, y + 4.5, '…', 'fixe', 'l')
box(ax, 70, y, 12, 9, 'resultat', label='17')
brace(ax, 4, 82, y + 11, 'fixe', label=r'la liste des $n$ qui marchent', down=False)
brace(ax, 4, 46, y - 2, 'resultat', label='se construisent')
text(ax, 52.5, y - 7, 'résiste', 'fixe', 's')
text(ax, 76, y - 7, 'Gauss, 1796', 'varie', 's')
text(ax, 44, 52, r'pour quels $n$ ?', 'sujet', 'l', weight='bold')
save(fig, '66-004')
