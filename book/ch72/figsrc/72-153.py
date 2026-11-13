import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cy = 34
for c in (20, 68):
    line(ax, [(c - 15, cy), (c + 15, cy)], 'fixe', lw=0.6); line(ax, [(c, cy - 15), (c, cy + 15)], 'fixe', lw=0.6)
arrow(ax, (20, cy), (34, cy), 'sujet', lw=1.5); line(ax, [(20, cy - 14), (20, cy + 14)], 'sujet', dash=True)
text(ax, 31, cy - 3.5, r'$u$', 'sujet', 'm'); text(ax, 20, cy + 18, r'$S_u$', 'sujet', 'm')
arrow(ax, (68, cy), (68, cy + 14), 'autre', lw=1.5); line(ax, [(54, cy), (82, cy)], 'autre', dash=True)
text(ax, 72, cy + 11, r'$\eta u$', 'autre', 'm'); text(ax, 58, cy + 3.5, r'$S_{\eta u}$', 'autre', 's')
arrow(ax, (30, 56), (58, 56), 'varie', curve=-0.4)
text(ax, 44, 63, r'$\eta$ : quart de tour', 'varie', 's')
text(ax, 44, 8, r'$\eta\,S_u\,\eta^{-1}=S_{\eta u}$', 'resultat', 'l')
save(fig, '72-153')
