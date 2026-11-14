import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cols = [['1', '0', '0'], ['0', '1', '0'], ['0', '1', '1']]
roles = ['autre', 'sujet', 'sujet']
heads = [r'$Tu=u$', r'$Tw=w$', r'$Tv=v+w$']
xs = [22, 44, 66]; cy = 28
r = fig.canvas.get_renderer(); h = 0
for x, c, ro, hd in zip(xs, cols, roles, heads):
    t = text(ax, x, cy, '\n'.join(c), ro, 'l')
    h = max(h, t.get_window_extent(r).height * 25.4 / fig.dpi)
    text(ax, x, 56, hd, ro, 'm')
hh = h / 2 + 1
for s in (-1, 1):
    x = 44 + s * 34
    line(ax, [(x - s * 1.5, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.5, cy - hh)], 'fixe')
for k, (nm, ro) in enumerate((('u', 'autre'), ('w', 'sujet'), ('v', 'sujet'))):
    text(ax, 5, cy + h / 2 - (k + 0.5) * h / 3, nm, ro, 'm')
text(ax, 44, 8, 'une colonne par image', 'fixe', 's')
save(fig, '60-217')
