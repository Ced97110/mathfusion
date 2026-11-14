import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
cols = [('fixe', r'$\times$ nombres', ['9', '8', '2'], '144'),
        ('sujet', '+ exposants de $a$', [r'$a^2$', r'$a^1$', ''], r'$a^3$'),
        ('autre', '+ exposants de $b$', [r'$b^6$', r'$b^4$', r'$b^3$'], r'$b^{13}$')]
w, gap, x0 = 26, 2, 3
for c, (role, head, cells, res) in enumerate(cols):
    x = x0 + c * (w + gap)
    text(ax, x + w / 2, 84, head, role, 's')
    for r, s in enumerate(cells):
        y = 66 - r * 14
        if s: box(ax, x, y, w, 11, role, label=s, size='l')
        else: box(ax, x, y, w, 11, role, fill=False, dash=True, label='pas de $a$', size='s')
    arrow(ax, (x + w / 2, 37), (x + w / 2, 32), 'varie')
    box(ax, x, 16, w, 14, 'resultat', label=res, size='l')
text(ax, 44, 6, r'$144\,a^3\,b^{13}$', 'resultat', 'xl', weight='bold')
save(fig, '14-084')
