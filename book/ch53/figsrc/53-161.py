import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
U, X = 1.4, 4.0    # 1 unité = 1,4 mm
H = 8
def bar(x, y, n, role, label=None, size='s'):
    box(ax, x, y, n * U, H, role, label=label, size=size, r=0.4)
# 1. n = 55
bar(X, 64, 55, 'sujet', r'$n = 55$')
# 2. on retire phi(n) = 40 : il reste 15
bar(X, 48, 40, 'fixe', r'$\varphi(n) = 40$')
bar(X + 40 * U, 48, 15, 'varie', '15')
# 3. on ajoute 1 : 16
bar(X, 32, 15, 'varie', '15')
bar(X + 15 * U, 32, 1, 'varie')
text(ax, X + 16 * U + 3, 36, r'$+\,1 = 16$', 'varie', 's', ha='left')
# 4. 16 = p + q
bar(X, 16, 5, 'sujet', r'$p=5$')
bar(X + 5 * U, 16, 11, 'autre', r'$q = 11$')
text(ax, X + 16 * U + 3, 20, r'$p + q = 16$', 'encre', 's', ha='left')
text(ax, 44, 5, r'et pour 667 : $667 - 616 + 1 = 52 = 23 + 29$', 'fixe', 's')
save(fig, '53-161')
