import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
line(ax, [(44, 8), (44, 60)], 'fixe', lw=0.6, dash=True)
for ox, role, hdr, rel, cap in [(0, 'sujet', 'anneau commutatif', '≠', 'le rang est fixé'),
                                (46, 'autre', 'certains non commutatifs', '≅', "le rang n'est plus fixé")]:
    text(ax, ox + 21, 60, hdr, role, 's')
    text(ax, ox + 3, 44, '$R^{(1)}$', role, 'm', ha='left')
    text(ax, ox + 3, 16, '$R^{(2)}$', role, 'm', ha='left')
    box(ax, ox + 18, 40, 8, 8, role)
    box(ax, ox + 18, 12, 8, 8, role); box(ax, ox + 28, 12, 8, 8, role)
    text(ax, ox + 22, 30, rel, role, 'xl')
    text(ax, ox + 21, 4, cap, role, 's')
save(fig, '58-073')
