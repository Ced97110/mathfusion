import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
u = 20
fig, ax = canvas(72)
for cs, y, role, name in ((0.75, 51, 'sujet', '0,75'), (0.5, 17, 'autre', '0,5')):
    w, h = (1 + cs)*u, (1 - cs)*u
    box(ax, 8, y, w, h, role, r=0.4)
    text(ax, 8, y + h + 10, f'cos A = {name}', role, 'm', ha='left', weight='bold')
    text(ax, 8 + w/2, y + h + 4, f'1 + cos A = {1 + cs:g}'.replace('.', ','), role, 'm')
    text(ax, 8 + w + 2, y + h/2, f'1 − cos A = {1 - cs:g}'.replace('.', ','), role, 'm', ha='left')
    text(ax, 8 + w + 2, y + h/2 - 6, f'sin² A = {(1 + cs)*(1 - cs):g}'.replace('.', ','), 'resultat', 'm', ha='left')
save(fig, '37-083')
