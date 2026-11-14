import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
bw = 15.5
text(ax, 3 + bw / 2, 61, 'image de 1', 'sujet', 's')
text(ax, 3 + bw * 1.5 + 1, 61, r'image de $i$', 'varie', 's')
gen = [[r'$a$', r'$-b$'], [r'$b$', r'$a$']]
con = [[r'$1$', r'$2$'], [r'$1$', r'$1$']]
for grid, x0 in [(gen, 3), (con, 54)]:
    for r in range(2):
        for c in range(2):
            box(ax, x0 + c * (bw + 1), 47 - r * 11, bw, 10, 'sujet' if c == 0 else 'varie', label=grid[r][c])
    line(ax, [(x0 + bw - 4.5, 50.5), (x0 + bw + 5.5, 42.5)], 'resultat', lw=1.0, dash=True)
arrow(ax, (37, 47), (53, 47), 'fixe')
text(ax, 45, 51, r'$a=b=1$', 'fixe', 's')
text(ax, 45, 43, r'$-1=2$', 'fixe', 's')
text(ax, 44, 26, r'trace (diagonale) $=a+a=2a=2$', 'resultat')
text(ax, 44, 14, r'déterminant $=a^2+b^2=2$', 'resultat')
save(fig, '67-167')
