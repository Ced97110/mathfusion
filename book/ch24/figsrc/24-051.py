import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [(12, 'sujet', r'$A$', r'$x+y$'), (30, 'autre', r'$C$', r'$2x+y$'), (58, 'sujet', r'$B$', '5'), (76, 'autre', r'$D$', '8')]
for xc, r, t, v in cols:
    box(ax, xc - 7, 48, 14, 9, r, fill=True, label=t, size='l')
    box(ax, xc - 7, 32, 14, 9, r, fill=True, label=v)
    arrow(ax, (xc, 48), (xc, 42), r, lw=0.9)
for xc, s in ((21, '+'), (44, '='), (67, '+')):
    text(ax, xc, 52.5, s, 'fixe', 'l')
brace(ax, 4, 38, 31, 'resultat', down=True)
brace(ax, 50, 84, 31, 'resultat', down=True)
box(ax, 4, 8, 34, 10, 'resultat', fill=True, label=r'$3x+2y$')
text(ax, 44, 13, '=', 'fixe', 'l')
box(ax, 50, 8, 34, 10, 'resultat', fill=True, label='13')
save(fig, '24-051')
