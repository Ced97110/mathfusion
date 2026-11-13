import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 4
def panel(ox, h, role, lab, eq, dim):
    oy = 14
    R = lambda a, b: (ox + a * u, oy + b * u)
    poly(ax, [R(0,0), R(8,0), R(8,h), R(0,h)], 'autre')
    poly(ax, [R(0,0), R(4,0), R(4,3), R(0,3)], 'sujet')
    line(ax, [R(0,0), R(8,6)], 'sujet', dash=True)
    line(ax, [R(0,0), R(8,h)], role, lw=1.4)
    text(ax, ox + 16, 9, dim, 'autre', 's')
    text(ax, ox + 16, 48, lab, role, 'm', weight='bold')
    text(ax, ox + 16, 41, eq, role, 's')
panel(6, 6, 'resultat', 'même direction', r'$0{,}75 = 0{,}75$', 'grand : 8 sur 6')
panel(50, 5, 'limite', 'directions différentes', r'$0{,}75 \neq 0{,}625$', 'grand : 8 sur 5')
text(ax, 44, 55, 'petit rectangle : 4 sur 3', 'sujet', 's')
save(fig, '09-018')
