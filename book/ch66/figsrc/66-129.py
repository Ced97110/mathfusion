import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 4.4
x0, y0 = 6, 10
n = 0
for r in range(7):
    for c in range(5):
        if n >= 32:
            break
        role = 'sujet' if n < 30 else 'varie'
        box(ax, x0 + c * s, y0 + (6 - r) * s, 4.0, 4.0, role, r=0.3, lw=0.6)
        n += 1
text(ax, 65, 46, r'$2^{5}=32$', 'encre', 'l')
text(ax, 65, 37, r'$32=6\times5+2$', 'encre', 'm')
text(ax, 65, 28, '6 groupes de 5', 'sujet', 'm')
text(ax, 65, 20, 'reste 2 : pas divisible', 'varie', 's')
text(ax, 65, 13, r'$N_p$ a aussi le reste 2', 'varie', 's')
save(fig, '66-129')
