import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cw, ch, x0, y0 = 32, 26, 22, 6
text(ax, x0 + cw * .5, 63, 'injectif', 'encre', 's'); text(ax, x0 + cw * 1.5, 63, 'pas injectif', 'encre', 's')
text(ax, 11, y0 + ch * 1.5, 'surjectif', 'encre', 's'); text(ax, 11, y0 + ch * .5, 'pas surjectif', 'encre', 's')
Z = r'$\mathbb{Z}$'; B = r'$\mathbb{Z}/4\mathbb{Z}$'
cells = [(0, 1, 'identité', Z + r'$\to$' + Z, 'fixe'), (1, 1, 'bouton', Z + r'$\to$' + B, 'sujet'),
         (0, 0, r'$\times 3$', Z + r'$\to$' + Z, 'fixe'), (1, 0, 'double', Z + r'$\to$' + B, 'fixe')]
for i, j, lab, sub, role in cells:
    box(ax, x0 + cw * i + 1, y0 + ch * j + 1, cw - 2, ch - 2, role, fill=(role == 'sujet'))
    cy = y0 + ch * j + ch / 2
    text(ax, x0 + cw * i + cw / 2, cy + 5, lab, role, 'm')
    text(ax, x0 + cw * i + cw / 2, cy - 1, sub, role, 's')
text(ax, x0 + cw * 1.5, y0 + ch * 1.5 - 7, r'$f(1) = f(5)$', 'sujet', 's')
save(fig, '48-046')
