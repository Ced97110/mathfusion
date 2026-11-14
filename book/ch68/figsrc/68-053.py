import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

def d(a, b):
    return sum(p != q for p, q in zip(a, b))

cw = 7.0
text(ax, 44, 85, r'$d \geq 0$ ; $d = 0$ seulement si $x = y$', 'resultat', 's', weight='bold')
text(ax, 18, 73, r'$x$', 'sujet', 'm', weight='bold')
text(ax, 42, 73, r'$y$', 'autre', 'm', weight='bold')
rows = [(58, '10', '10', 'd = 0 : mots égaux', 'resultat'),
        (36, '10', '01', 'd = 2, donc d ≥ 1\nmots différents', 'varie')]
for y, a, b, lab, role in rows:
    dd = d(a, b)
    assert lab.startswith('d = %d' % dd)
    bits(ax, 11, y, a, ['varie' if p != q else 'sujet' for p, q in zip(a, b)], cw)
    bits(ax, 35, y, b, ['varie' if p != q else 'autre' for p, q in zip(a, b)], cw)
    text(ax, 55, y + 3.25, lab, role, 's', ha='left', weight='bold')
# mauvaise mesure : écart des nombres de 1
y = 12
a, b = '10', '01'
assert a.count('1') - b.count('1') == 0 and a != b
bits(ax, 11, y, a, 'fixe', cw)
bits(ax, 35, y, b, 'fixe', cw)
text(ax, 55, y + 3.25, 'écart des 1 : 0\nmots différents : faux', 'limite', 's', ha='left', weight='bold')
line(ax, [(3, 28), (85, 28)], 'fixe', lw=0.5, dash=True)
save(fig, '68-053')
