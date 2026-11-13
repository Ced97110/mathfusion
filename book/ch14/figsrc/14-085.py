import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cols = [('fixe', r'$\div$ nombres', '24', r'$2^3 = 8$', '3'),
        ('sujet', '$-$ exposants de $a$', r'$a^7$', r'$a^4$', r'$a^3$'),
        ('autre', '$-$ exposants de $b$', r'$b^9$', r'$b^{-6}$', r'$b^{15}$')]
w, gap, x0 = 26, 2, 3
for c, (role, head, top, bot, res) in enumerate(cols):
    x = x0 + c * (w + gap); xm = x + w / 2
    text(ax, xm, 74, head, role, 's')
    box(ax, x, 56, w, 12, role, label=top, size='l')
    line(ax, [(x, 52), (x + w, 52)], 'encre', lw=1.2)
    box(ax, x, 36, w, 12, role, label=bot, size='l')
    arrow(ax, (xm, 33), (xm, 25), 'varie')
    box(ax, x, 8, w, 14, 'resultat', label=res, size='l')
text(ax, 44, 2.5, r'$3\,a^3\,b^{15}$', 'resultat', 's')
save(fig, '14-085')
