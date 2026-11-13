import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
G = 6.7; x0 = (88 - 12 * G) / 2; y = 30
for i in range(12):
    cx = x0 + (i + 0.5) * G
    box(ax, cx - 2.9, y - 4.5, 5.8, 9, 'resultat', r=0.8)
    for d in (-1.4, 1.4): disc(ax, cx + d, y, 1.0, 'sujet')
brace(ax, x0, x0 + 12 * G, y + 6, 'sujet', label=r'24 couples $(h, k)$', down=False)
brace(ax, x0, x0 + 12 * G, y - 6, 'resultat', label='12 sommes différentes', down=True)
text(ax, 44, 9, r'chaque somme : $|H \cap K| = 2$ couples', 'resultat', 's')
text(ax, 44, 2.5, r'$24 / 2 = 12$', 'resultat', 'm')
save(fig, '50-191')
