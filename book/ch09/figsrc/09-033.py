import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
x0, bw = 8, 8
for i in range(9):
    box(ax, x0 + i * bw, 14, bw, 10, 'sujet', label='4', r=0.5)
brace(ax, x0, x0 + 9 * bw, 26, 'fixe', label='36', down=False)
brace(ax, x0, x0 + 9 * bw, 13, 'resultat', label='9 paquets de 4', down=True)
text(ax, 44, 42, r'$36 \div 4$ : combien de fois 4 ?', 'encre', 'm')
save(fig, '09-033')
