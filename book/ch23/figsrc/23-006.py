import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
u = 2.2
for (x, n, role, cap) in [(6, 10, 'limite', r'$10\times11=110$'), (46, 12, 'resultat', r'$12\times13=156$')]:
    w, h = (n + 1) * u, n * u
    box(ax, x, 36, w, h, role, True)
    text(ax, x + w / 2, 36 + h + 2.6, str(n + 1), role, 's')
    text(ax, x - 2.8, 36 + h / 2, str(n), role, 's')
    text(ax, x + w / 2, 29, cap, role, 's')
text(ax, 44, 17, r'$x\times(x+1)=156$', 'encre', 'm')
text(ax, 44, 8, r'donc $x^2+x=156$', 'sujet', 'm')
save(fig, '23-006')
