import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 50, 63, 'diviseurs de l’ordre', 'encre', 's')
rows = [(38, r'$\mathbb{F}_4$', [1, 2, 4], 2), (10, r'$\mathbb{F}_9$', [1, 3, 9], 3)]
for y, name, divs, p in rows:
    text(ax, 11, y + 5, name, 'sujet', 'l')
    for x, d in zip((22, 42, 62), divs):
        box(ax, x, y, 16, 10, 'resultat' if d == p else 'fixe', label=str(d))
        if d == p: text(ax, x + 8, y - 4, 'caractéristique', 'resultat', 's')
    brace(ax, 22, 78, y + 11, 'fixe', label='3 choix possibles', down=False)
save(fig, '67-038')
