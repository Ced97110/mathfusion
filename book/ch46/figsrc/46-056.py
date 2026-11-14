import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
def mat(xc, c1, c2, role):
    y = 26; h = 14
    line(ax, [(xc - 8, y - h/2), (xc - 9.5, y - h/2), (xc - 9.5, y + h/2), (xc - 8, y + h/2)], role, lw=1)
    line(ax, [(xc + 8, y - h/2), (xc + 9.5, y - h/2), (xc + 9.5, y + h/2), (xc + 8, y + h/2)], role, lw=1)
    t1 = text(ax, xc - 1.5, y, c1, role, 'm', ha='right'); t2 = text(ax, xc + 6, y, c2, role, 'm', ha='right')
    t1.set_linespacing(2.2); t2.set_linespacing(2.2)
mat(14, '1\n0', '0\n1', 'sujet'); mat(48, '−1\n0', '0\n−1', 'sujet'); mat(78, '0\n0', '0\n0', 'limite')
text(ax, 31, 26, '+', 'encre', 'xl'); text(ax, 63, 26, '=', 'encre', 'xl')
text(ax, 14, 11, 'déterminant 1', 'sujet', 's'); text(ax, 48, 11, 'déterminant 1', 'sujet', 's'); text(ax, 78, 11, 'sans inverse', 'limite', 's')
text(ax, 44, 43, 'deux matrices inversibles', 'sujet', 's')
save(fig, '46-056')
