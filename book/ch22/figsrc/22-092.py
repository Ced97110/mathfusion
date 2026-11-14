import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(80)
box(ax, 8, 62, 72, 13, 'sujet', label=r'$\sqrt{x}\,\sqrt{y}=\sqrt{xy}$', size='l')
text(ax, 44, 55, r'si $x\geq0$ et $y\geq0$', 'sujet', 's')
text(ax, 44, 44, r'contre-exemple : $x=-4$, $y=-9$', 'fixe', 's')
box(ax, 2, 14, 38, 22, 'limite')
text(ax, 21, 30, r'$\sqrt{-4}\,\sqrt{-9}$', 'limite', 'm')
text(ax, 21, 20, 'n’existent pas', 'limite', 's')
box(ax, 48, 14, 38, 22, 'resultat')
text(ax, 67, 30, r'$\sqrt{36}=6$', 'resultat', 'm')
text(ax, 67, 20, 'existe', 'resultat', 's')
text(ax, 44, 25, '≠', 'limite', 'xl')
save(fig, '22-092')
