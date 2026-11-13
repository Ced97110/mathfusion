import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 4, 52, 62, 22, 'sujet'); text(ax, 35, 68, '30 − 15 − 10 − 6', 'sujet', 'm'); text(ax, 35, 58, '+ 5 + 3 + 2 − 1', 'sujet', 'm')
box(ax, 70, 52, 14, 22, 'resultat', label='8', size='xl')
text(ax, 44, 41, r'$=$', 'resultat', 'xl')
text(ax, 44, 30, 'sans facteur commun avec 30', 'fixe', 's')
bw, gap, x0 = 8.6, 1.3, 5
for i, n in enumerate([1, 7, 11, 13, 17, 19, 23, 29]):
    box(ax, x0 + i * (bw + gap), 14, bw, 9, 'autre', label=str(n), size='s')
brace(ax, x0, x0 + 8 * bw + 7 * gap, 14, 'resultat', label='8 entiers', down=True)
save(fig, '80-369')
