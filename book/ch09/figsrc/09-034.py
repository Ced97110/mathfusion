import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
bw = 7
text(ax, 44, 76, r'$36 / 4 = 9$', 'sujet', 'l')
for i in range(9):
    box(ax, 6 + i * bw, 52, bw, 8, 'sujet', r=0.5)
brace(ax, 6, 6 + 9 * bw, 62, 'fixe', label='36', down=False)
brace(ax, 6, 6 + 9 * bw, 51, 'resultat', label='9 paquets de 4')
text(ax, 44, 30, r'8 miles $/$ 2 miles $= 4$', 'autre', 'l')
for i in range(4):
    box(ax, 6 + i * bw, 8, bw, 8, 'autre', r=0.5)
brace(ax, 6, 6 + 4 * bw, 18, 'fixe', label='8 miles', down=False)
brace(ax, 6, 6 + 4 * bw, 7, 'resultat', label='4 paquets de 2 miles')
save(fig, '09-034')
