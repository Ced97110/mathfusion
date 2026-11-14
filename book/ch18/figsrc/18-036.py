import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(72)
text(ax, 44, 67, r'départ : $9x^3 + 18x^2 + 27x$', 'fixe', 's')
xs = [2.5, 30.5, 58.5]
top = [r'$9x^3$', r'$18x^2$', r'$27x$']
bot = [r'$9x \times x^2 = 9x^3$', r'$9x \times 2x = 18x^2$', r'$9x \times 2 = 18x$']
sym = ['=', '=', r'$\neq$']; cr = ['resultat', 'resultat', 'limite']
for x, t, b, s_, c in zip(xs, top, bot, sym, cr):
    box(ax, x, 50, 27, 9, 'fixe', t)
    box(ax, x, 18, 27, 9, c, b, 's')
    text(ax, x + 13.5, 38.5, s_, c, 'l', weight='bold')
    arrow(ax, (x + 13.5, 31), (x + 13.5, 27.5), c) if False else None
text(ax, 44, 11, r'on redéveloppe $9x(x^2 + 2x + 2)$', 'varie', 's')
text(ax, 44, 4, '27x ne revient pas : erreur', 'limite', 's')
save(fig, '18-036')
