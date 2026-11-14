import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mulx(v):
    a0, a1, a2, a3 = v
    return [a3, a0 ^ a3, a1, a2]
p = [[1, 0, 0, 0]]
for _ in range(15):
    p.append(mulx(p[-1]))
b4, b9 = p[4], p[9]
s = [x ^ y for x, y in zip(b4, b9)]
assert b4 == [1, 1, 0, 0] and b9 == [0, 1, 0, 1] and s == [1, 0, 0, 1] and p[14] == s
heads = [r'$1$', r'$\alpha$', r'$\alpha^2$', r'$\alpha^3$']
for c in range(4):
    text(ax, 30 + c * 10 + 4.5, 57, heads[c], 'fixe')
def row(y, bits, role):
    for c in range(4):
        x = 30 + c * 10
        if bits[c]:
            ax.add_patch(Rectangle((x, y), 9, 7, ec=COL[role], fc=COL[role], lw=0.5, zorder=2))
        else:
            ax.add_patch(Rectangle((x, y), 9, 7, ec=COL['fixe'], fc=FILL['fixe'], lw=0.5, zorder=2))
row(44, b4, 'sujet'); text(ax, 27, 47.5, r'$\alpha^4$', 'sujet', ha='right')
row(35, b9, 'autre'); text(ax, 27, 38.5, r'$\alpha^9$', 'autre', ha='right')
line(ax, [(30, 32), (69, 32)], 'fixe')
row(23, s, 'resultat'); text(ax, 27, 26.5, 'somme', 'resultat', 's', ha='right')
text(ax, 44.5, 18, r'$1+1=0$', 'fixe', 's')
text(ax, 71, 26.5, r'$=\alpha^{14}$', 'resultat', ha='left')
text(ax, 44, 8, r'faux : $4+9=13\neq14$', 'limite')
save(fig, '67-175')
