import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cw, ch, x0 = 12, 8, 19
text(ax, 8, 66, 'classe', 'autre', 's'); text(ax, 8, 36, 'entiers', 'sujet', 's')
for j in range(5):
    box(ax, x0 + j * (cw + 1), 62, cw, ch, 'autre', label=str(j))
for r in range(4):
    for j in range(5):
        v = 5 * r + j
        role = 'resultat' if j == 0 else 'sujet'
        if v == 17: role = 'varie'
        box(ax, x0 + j * (cw + 1), 50 - r * (ch + 2), cw, ch, role, label=str(v))
brace(ax, x0, x0 + cw, 18, 'resultat', label='noyau 5ℤ', down=True)
brace(ax, x0 + 2 * (cw + 1), x0 + 3 * cw + 2, 18, 'varie', label='17 → 2', down=True)
text(ax, 8, 66 - 0, 'classe', 'autre', 's') if False else None
save(fig, '48-130')
