import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'polynôme minimal de $u$', 'encre', 'm')
text(ax, 44, 59, r'racines : $\pm\sqrt{2}\pm\sqrt{3}$', 'fixe', 's')
coefs = ['1', '0', '−10', '0', '1']
heads = [r'$x^{4}$', r'$x^{3}$', r'$x^{2}$', r'$x$', r'$1$']
for i, (c, hd) in enumerate(zip(coefs, heads)):
    x = 6 + 16 * i
    box(ax, x, 36, 14, 12, 'sujet' if i == 4 else 'fixe', label=c, size='m')
    text(ax, x + 7, 52, hd, 'sujet' if i == 4 else 'fixe', 's')
arrow(ax, (77, 36), (77, 24), 'resultat')
text(ax, 74, 30, r'terme constant $c_{4}=1$', 'sujet', 's', ha='right')
box(ax, 24, 8, 62, 14, 'resultat', label=r'$N_{E/\mathbb{Q}}(u)=(-1)^{4}\,c_{4}=1$', size='m')
save(fig, '67-201')
