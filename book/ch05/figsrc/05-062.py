import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
t = 4.2
text(ax, 44, 62, r'essais : impair $\Rightarrow$ premier ?', 'encre', 'm')
x0 = 14
def tiles(x, y, w, h, role):
    for i in range(w):
        for j in range(h):
            box(ax, x + i * t, y + j * t, t, t, role, r=0.3, lw=0.6)
for k, n in enumerate([3, 5, 7]):
    y = 50 - k * 8
    text(ax, 6, y + t / 2, str(n), 'resultat', 'l')
    tiles(x0, y, n, 1, 'resultat')
    text(ax, 50, y + t / 2, 'premier', 'resultat', 's', ha='left')
y9 = 12
text(ax, 6, y9 + 1.5 * t, '9', 'limite', 'l')
tiles(x0, y9, 3, 3, 'limite')
text(ax, 32, y9 + 2.2 * t, r'$9 = 3 \times 3$ : composé', 'limite', 's', ha='left')
text(ax, 32, y9 + 0.8 * t, 'la règle casse', 'limite', 's', ha='left')
save(fig, '05-062')
