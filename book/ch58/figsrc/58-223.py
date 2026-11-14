import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'η est faite d’abord, ρ ensuite', 'varie', 's')
def panel(px, bottom_left, bottom_right, cap):
    box(ax, px, 3, 41, 59, 'fixe', fill=False, dash=True, lw=0.7)
    cxe, cxr = px + 12, px + 29
    box(ax, cxe - 6, 48, 12, 10, 'sujet', label=r'$\eta$')
    box(ax, cxr - 6, 48, 12, 10, 'autre', label=r'$\rho$')
    for (cx, nm) in ((cxe, bottom_left), (cxr, bottom_right)):
        role = 'sujet' if nm == '$A$' else 'autre'
        box(ax, cx - 6, 16, 12, 10, role, label=nm)
    # liens : chaque application vers son tableau
    for (top, nm) in ((cxe, '$A$'), (cxr, '$C$')):
        bx = cxe if bottom_left == nm else cxr
        line(ax, [(top, 47.5), (bx, 26.5)], 'varie', lw=1.0)
    text(ax, px + 20.5, 8, cap, 'fixe', 's')
panel(2, '$C$', '$A$', 'livre : $CA$')
panel(45, '$A$', '$C$', 'Jacobson : $AC$')
save(fig, '58-223')
