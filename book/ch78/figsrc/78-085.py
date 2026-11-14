import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 3, 64, 36, 11, 'resultat', label=r'$(e_1e_1)e_2=-e_2$', size='s')
text(ax, 44, 69.5, '=', 'encre', 'l')
box(ax, 49, 64, 36, 11, 'resultat', label=r'$e_1(e_1e_2)=-e_2$', size='s')
cols = [r'$[x,x,y]$', r'$[y,x,x]$', r'$[x,y,z]$']
cx = [30, 49, 68]; cw = 17
for c, lab in zip(cx, cols): text(ax, c + cw / 2, 54, lab, 'encre', 's')
rows = [('associative', 'fixe', [1, 1, 1], 40), ('alternative', 'sujet', [1, 1, 0], 27), ('quelconque', 'fixe', [0, 0, 0], 14)]
for name, role, on, y in rows:
    text(ax, 3, y + 4.5, name, role, 's', ha='left')
    for c, v in zip(cx, on):
        if v: box(ax, c, y, cw, 9, 'resultat', label='0')
        else: box(ax, c, y, cw, 9, 'fixe', fill=False, dash=True)
save(fig, '78-085')
