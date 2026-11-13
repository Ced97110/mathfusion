import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for i in range(6):
    box(ax, 14 + i * 12 - 4.5, 37.5, 9, 9, 'varie' if i < 3 else 'sujet', label=str(i + 1))
brace(ax, 9, 79, 49, 'fixe', r'$U$', down=False)
brace(ax, 9, 39, 35, 'varie', r'$A$ (retiré)')
brace(ax, 45, 79, 35, 'sujet', 'ce qui reste')
text(ax, 44, 20, r"$A' = U \setminus A$", 'sujet', 'l')
text(ax, 44, 10, 'les deux : 4, 5 et 6', 'resultat', 'm')
save(fig, '42-135')
