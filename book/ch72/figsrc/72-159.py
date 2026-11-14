import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
cy = 44
text(ax, 44, 63, r'$L_1$ au choix, $L_2$ à 45°', 'encre', 's')
for c, a1 in [(15, 0), (44, 45), (73, 20)]:
    for a, role, nm in [(a1, 'sujet', r'$L_1$'), (a1 + 45, 'autre', r'$L_2$')]:
        t = math.radians(a); h = 11
        line(ax, [(c - h * math.cos(t), cy - h * math.sin(t)), (c + h * math.cos(t), cy + h * math.sin(t))], role, lw=1.4)
        text(ax, c + (h + 2.5) * math.cos(t), cy + (h + 2.5) * math.sin(t), nm, role, 's')
    line(ax, [(c + 6 * math.cos(math.radians(a1 + d)), cy + 6 * math.sin(math.radians(a1 + d))) for d in range(0, 46, 5)], 'varie', lw=0.9)
    m = math.radians(a1 + 22.5)
    text(ax, c + 14 * math.cos(m), cy + 14 * math.sin(m) - (1.5 if a1 == 0 else 0), '45°', 'varie', 's')
    # same result under each pair: the quarter turn
    arrow(ax, (c, 31), (c, 27), 'fixe', lw=0.8)
    oq = (c - 3, 17)
    line(ax, [oq, (oq[0] + 9, oq[1])], 'fixe', lw=0.7); line(ax, [oq, (oq[0], oq[1] + 9)], 'fixe', lw=0.7)
    arrow(ax, (oq[0] + 7, oq[1]), (oq[0], oq[1] + 7), 'varie', lw=1.3, curve=0.5)
text(ax, 44, 8, 'même quart de tour : 90°', 'resultat', 's')
text(ax, 44, 2.5, 'une infinité de paires', 'resultat', 's', weight='bold')
save(fig, '72-159')
