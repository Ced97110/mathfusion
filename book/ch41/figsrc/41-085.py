import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
a = 20                       # côté d'un carré de 3 unités
xs = [5, 34, 63]
y0 = 20
labs = [r'$(1-4)^2$', r'$(2-5)^2$', r'$(3-6)^2$']
for i, x in enumerate(xs):
    role = 'sujet' if i < 2 else 'varie'
    box(ax, x, y0, a, a, role, label='9', size='l')
    text(ax, x + a / 2, y0 - 4, labs[i], role, 's')
brace(ax, xs[0], xs[1] + a, y0 + a + 1, 'sujet', label='plan : 2 carrés', down=False, depth=1.6)
brace(ax, xs[2], xs[2] + a, y0 + a + 1, 'varie', label='espace : + 1', down=False, depth=1.6)
text(ax, 29.5, y0 + a / 2, '+', 'encre', 'l')
text(ax, 58.5, y0 + a / 2, '+', 'encre', 'l')
box(ax, 8, 2, 72, 9, 'resultat', label=r'$9+9+9=27=14+77-2\times32$', size='s')
save(fig, '41-085')
