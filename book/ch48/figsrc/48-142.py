import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
c = 3.9; x0 = 30
def block(y, n, tot, half):
    text(ax, 44, y + 17, f'n = {n} : {tot} permutations', 'sujet', 'm')
    for r, (role, nm) in enumerate([('resultat', 'paires'), ('fixe', 'impaires')]):
        yy = y + 8 - r * 8
        text(ax, 4, yy + 3, f'{nm} : {half}', role, 's', ha='left')
        cs = c if half > 6 else 8
        for k in range(half):
            box(ax, x0 + k * (cs + 0.5) if half > 6 else x0 + k * 9, yy, (cs if half > 6 else 8), 6, role, r=0.5)
block(48, 3, 6, 3); block(8, 4, 24, 12)
text(ax, 44, 3, 'A_n = n!/2', 'resultat', 'l') if False else None
save(fig, '48-142')
