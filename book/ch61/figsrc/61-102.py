import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, r'les briques de $K$ sur $F$', 'sujet', 'm')
xs = [4, 25, 46, 67]
labs = [r'$v_1=1$', r'$v_2=\sqrt{2}$', '…', r'$v_r$']
nums = ['numéro 1', 'numéro 2', '', r'numéro $r$']
for i, (x, s, n) in enumerate(zip(xs, labs, nums)):
    box(ax, x, 28, 18, 14, 'sujet', label=s, size='m', dash=(i >= 2))
    if n: text(ax, x + 9, 24, n, 'varie', 's')
brace(ax, 4, 85, 19, 'sujet', label=r'$r$ briques', depth=1.6)
save(fig, '61-102')
