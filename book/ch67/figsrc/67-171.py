import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# table des puissances de alpha : alpha^4 = alpha + 1, v = [a0, a1, a2, a3]
def mulx(v):
    a0, a1, a2, a3 = v
    return [a3, a0 ^ a3, a1, a2]
p = [[1, 0, 0, 0]]
for _ in range(15):
    p.append(mulx(p[-1]))
assert p[15] == [1, 0, 0, 0] and len(set(map(tuple, p[:15]))) == 15 and all(any(v) for v in p[:15])
assert p[4] == [1, 1, 0, 0] and p[5] == [0, 1, 1, 0] and p[10] == [1, 1, 1, 0]
assert [k for k in range(15) if (3 * k) % 15 == 0] == [0, 5, 10]
verts = {0, 5, 10}
heads = [r'$1$', r'$\alpha$', r'$\alpha^2$', r'$\alpha^3$']
for c in range(4):
    text(ax, 32 + c * 9.5 + 4.25, 84, heads[c], 'fixe')
for k in range(15):
    y = 77 - k * 4.7
    for c in range(4):
        x = 32 + c * 9.5
        if p[k][c]:
            r = 'resultat' if k in verts else 'sujet'
            ax.add_patch(Rectangle((x, y), 8.5, 4.2, ec=COL[r], fc=COL[r], lw=0.4, zorder=2))
        else:
            ax.add_patch(Rectangle((x, y), 8.5, 4.2, ec=COL['fixe'], fc=FILL['fixe'], lw=0.4, zorder=2))
for k, s in [(0, r'$\alpha^0$'), (4, r'$\alpha^4$'), (5, r'$\alpha^5$'), (10, r'$\alpha^{10}$'), (14, r'$\alpha^{14}$')]:
    text(ax, 30, 77 - k * 4.7 + 2.1, s, 'resultat' if k in verts else 'fixe', 's', ha='right')
text(ax, 73, 70, 'bleu = 1', 'sujet', 's', ha='left')
text(ax, 73, 64, r'vert : $\mathbb{F}_4$', 'resultat', 's', ha='left')
save(fig, '67-171')
