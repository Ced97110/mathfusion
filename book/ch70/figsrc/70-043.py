import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 24, 60, r'$f=2y+2$', 'sujet', 'm')
text(ax, 64, 60, r'$g=3y+6$', 'autre', 'm')
box(ax, 6, 44, 10, 9, 'fixe', label='2', size='m')
box(ax, 17, 44, 20, 9, 'sujet', label=r'$y+1$', size='m')
box(ax, 48, 44, 10, 9, 'fixe', label='3', size='m')
box(ax, 59, 44, 20, 9, 'autre', label=r'$y+2$', size='m')
text(ax, 44, 38, 'constantes : degré 0', 'fixe', 's')
cw, ch, x0, y0 = 10, 8, 8, 12
for i, row in enumerate([['2', '2'], ['3', '6']]):
    for j, s in enumerate(row):
        box(ax, x0 + j * cw + 0.4, y0 + (1 - i) * ch + 0.4, cw - 0.8, ch - 0.8, 'sujet' if i == 0 else 'autre', label=s, size='m', r=0.4)
text(ax, 56, y0 + 12, r'$2\times6-2\times3=6$', 'fixe', 's')
box(ax, 36, y0 + 1, 44, 8, 'resultat', label=r'$Res=6$ : pas nul', size='s')
save(fig, '70-043')
