import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# p = 2 ; x^3+2x+2 : a = (2, 2, 0, 1) ; x^2-4 : a = (-4, 0, 1)
def tests(a, p=2):
    return [all(c % p == 0 for c in a[:-1]), a[-1] % p != 0, a[0] % (p * p) != 0]
t1, t2 = tests([2, 2, 0, 1]), tests([-4, 0, 1])
assert t1 == [True, True, True] and t2 == [True, True, False]
text(ax, 2, 72, r'$p=2$', 'encre', 'm', ha='left', weight='bold')
text(ax, 50, 72, r'$x^3+2x+2$', 'sujet', 'm')
text(ax, 75, 72, r'$x^2-4$', 'autre', 'm')
labels = [r'$p$ divise $a_0,\ldots,a_{n-1}$', r'$p$ ne divise pas $a_n$', r'$p^2$ ne divise pas $a_0$']
for i, lab in enumerate(labels):
    y = 52 - i * 14
    text(ax, 2, y + 5, lab, 'encre', 's', ha='left')
    for tx, t in [(39, t1), (64, t2)]:
        box(ax, tx, y, 22, 10, 'resultat' if t[i] else 'limite', label='✓' if t[i] else '✗', size='m')
box(ax, 39, 4, 22, 11, 'resultat', label='irréductible', size='s')
box(ax, 64, 4, 22, 11, 'limite', label=r'$(x-2)(x+2)$', size='s')
text(ax, 2, 9.5, 'conclusion', 'encre', 's', ha='left')
save(fig, '56-159')
