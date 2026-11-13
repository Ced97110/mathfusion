import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y0 = 14; k = 40 / 5.6713
def bar(x, v, role, lab, dash=False):
    box(ax, x, y0, 9, max(v * k, 1.6), role, fill=not dash, r=0.3, dash=dash)
    text(ax, x + 4.5, y0 + max(v * k, 1.6) + 3, lab, role, 's')
bar(11, 0.1763, 'sujet', '0,1763')
text(ax, 15.5, y0 - 4, '10°', 'encre', 'm')
bar(33, 0.3526, 'fixe', '0,3526', dash=True)
bar(44, 0.3640, 'sujet', '0,3640')
text(ax, 43.5, y0 - 4, '20°', 'encre', 'm')
bar(62, 1.4104, 'fixe', '1,4104', dash=True)
bar(73, 5.6713, 'sujet', '5,6713')
text(ax, 72.5, y0 - 4, '80°', 'encre', 'm')
box(ax, 4, 60, 6, 4, 'fixe', dash=True, r=0.3)
text(ax, 12, 62, 'attendu si proportionnel', 'fixe', 's', ha='left')
box(ax, 4, 53, 6, 4, 'sujet', r=0.3)
text(ax, 12, 55, 'donné par la table', 'sujet', 's', ha='left')
save(fig, '25-094')
