import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for i, (role, s) in enumerate([('sujet', 'a = 2'), ('autre', 'b = 6'), ('varie', r"$b^{\prime}$ = 5"), ('fixe', r"$a^{\prime}$ = 15")]):
    box(ax, 2 + i * 21.5, 52, 19.5, 11, role, label=s, size='s')
rows = [(r'$a\leq b$', '2 divise 6'), (r"$a\wedge b^{\prime}=O$", 'PGCD(2, 5) = 1'), (r"$a^{\prime}\vee b=I$", 'PPCM(15, 6) = 30')]
for i, (ph, calc) in enumerate(rows):
    y = 36 - i * 16
    box(ax, 2, y, 84, 12, 'resultat')
    text(ax, 6, y + 6, ph, 'encre', 's', ha='left')
    text(ax, 46, y + 6, calc, 'encre', 's')
    text(ax, 82, y + 6, 'vrai', 'resultat', 's', ha='right', weight='bold')
save(fig, '80-236')
