import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# vérifications numériques écrites dans la figure
for y in (2, -4):
    assert y * y + 2 * y - 8 == 0
assert 4 + 32 == 36 and (-2 + 6) / 2 == 2 and (-2 - 6) / 2 == -4
# x^4 + 2x^2 - 8 -> y = x^2 -> (y - 2)(y + 4) -> racines
box(ax, 4, 86, 80, 11, 'sujet', label=r'$x^4+2x^2-8$')
arrow(ax, (44, 86), (44, 77), 'varie', lw=1.2)
text(ax, 49, 81.5, r'poser $y=x^2$', 'varie', 's', ha='left')
box(ax, 4, 63, 80, 14, 'fixe', label=r'$y^2+2y-8$' + '\n' + r'discriminant $4+32=36$,  $y=(-2\pm6)/2$', size='s')
arrow(ax, (23, 63), (23, 54), 'sujet', lw=1.0)
arrow(ax, (65, 63), (65, 54), 'autre', lw=1.0)
text(ax, 27, 58.5, r'$y=2$', 'sujet', 's', ha='left')
text(ax, 69, 58.5, r'$y=-4$', 'autre', 's', ha='left')
box(ax, 4, 41, 38, 12, 'sujet', label=r'$x^2=2$', size='m')
box(ax, 46, 41, 38, 12, 'autre', label=r'$x^2=-4$', size='m')
arrow(ax, (23, 41), (23, 30), 'sujet', lw=1.0)
arrow(ax, (65, 41), (65, 30), 'autre', lw=1.0)
box(ax, 4, 18, 38, 12, 'resultat', label=r'$x=\pm\sqrt{2}$', size='m')
box(ax, 46, 18, 38, 12, 'resultat', label=r'$x=\pm2i$', size='m')
text(ax, 23, 12.5, r'facteur $x^2-2$', 'sujet', 's')
text(ax, 65, 12.5, r'facteur $x^2+4$', 'autre', 's')
save(fig, '62-146')
