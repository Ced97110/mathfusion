import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 22, 66, 'à la main', 'limite', 'm'); text(ax, 66, 66, 'avec le théorème', 'resultat', 'm')
L = ['normal : 3 matrices', 'paquets = un groupe', 'construire ≅']
R = ['det est un homomorph.', 'det est surjectif', 'noyau = det 1']
for i, t in enumerate(L):
    box(ax, 3, 46 - i * 16, 38, 13, 'limite', label=t, size='s')
    if i < 2: arrow(ax, (22, 46 - i * 16), (22, 46 - i * 16 - 3), 'limite')
for i, t in enumerate(R):
    box(ax, 47, 53 - i * 8, 38, 6.5, 'resultat', label=t, size='s', r=0.5)
brace(ax, 3, 41, 12, 'limite', label='long', down=True)
brace(ax, 47, 85, 12, 'resultat', label='court', down=True)
save(fig, '48-138')
