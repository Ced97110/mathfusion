import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
w, h, y = 4.5, 8, 28
def bar(x, n, role, lab):
    for k in range(n):
        box(ax, x + k * w + 0.3, y, w - 0.6, h, role, r=0.5)
    text(ax, x + n * w / 2, y - 4, lab, role, 's')
    return x + n * w
text(ax, 21, 54, 'ℤ/12', 'encre', 'l'); text(ax, 66, 54, 'ℤ/2 ⊕ ℤ/6', 'encre', 'l')
e = bar(3, 4, 'sujet', '2²'); bar(e + 3, 3, 'autre', '3')
a = bar(47, 2, 'sujet', '2')
b = bar(a + 3, 2, 'sujet', '2'); c = bar(b + 3, 3, 'autre', '3')
brace(ax, a + 3, c, y + h + 1, 'fixe', label='ℤ/6', down=False)
text(ax, 44, 8, '≠ : listes différentes', 'limite', 'm')
save(fig, '60-030')
