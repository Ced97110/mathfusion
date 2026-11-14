import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, ytop, cw, ch = 12, 56, 15, 9
def order(i, j):
    o4 = {0: 1, 1: 4, 2: 2, 3: 4}[i]
    o2 = 1 if j == 0 else 2
    return max(o4, o2)  # lcm of orders that are powers of 2
for i in range(4):
    text(ax, 6, ytop - (i + 0.5) * ch, f'ligne {i}'.replace('ligne ', ''), 'fixe', 's')
    for j in range(2):
        o = order(i, j)
        role = 'sujet' if j == 0 else 'fixe'
        lw = 1.8 if (i, j) == (1, 0) else 0.8
        box(ax, x0 + j * cw, ytop - (i + 1) * ch, cw, ch, role, label=str(o), size='m', lw=lw, r=0.5)
text(ax, x0 + cw / 2, ytop + 3.5, r'$\langle g\rangle$', 'sujet', 's')
text(ax, x0 + 1.5 * cw, ytop + 3.5, r'hors de $\langle g\rangle$', 'fixe', 's')
text(ax, 62, 46, 'g = (1, 0)', 'sujet', 's', weight='bold')
text(ax, 62, 41, 'ordre 4 : maximal', 'sujet', 's')
text(ax, 62, 30, 'ordres hors de', 'fixe', 's')
text(ax, 62, 26, r'$\langle g\rangle$ : 2, 4, 2, 4', 'fixe', 's')
text(ax, 44, 8, 'chiffre = ordre de la case', 'fixe', 's')
save(fig, '60-129')
