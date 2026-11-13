import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 57, 'même nature', 'sujet', 'm', weight='bold')
text(ax, 66, 57, 'natures différentes', 'autre', 'm', weight='bold')
for cx, top, bot, res, note, role in [(22, '8 miles', '2 miles', r'$= 4$', 'aucune unité', 'sujet'),
                                      (66, '8 miles', '2 gallons', r'$= 4$ miles/gallon', 'unités gardées', 'autre')]:
    text(ax, cx, 44, top, role, 'm')
    line(ax, [(cx - 12, 37), (cx + 12, 37)], role, lw=1.0)
    text(ax, cx, 30, bot, role, 'm')
    text(ax, cx, 20, res, 'resultat', 'm', weight='bold')
    text(ax, cx, 8, note, 'fixe', 's')
# units crossed out on the left
line(ax, [(22 - 2.2, 41), (22 + 7.5, 47)], 'limite', lw=1.1)
line(ax, [(22 - 2.2, 27), (22 + 7.5, 33)], 'limite', lw=1.1)
line(ax, [(44, 8), (44, 52)], 'fixe', dash=True)
save(fig, '09-035')
