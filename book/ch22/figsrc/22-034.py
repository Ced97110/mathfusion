import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(68)
h = 10; sw = .45 * h
text(ax, 4, 62, 'le trait couvre 9 + 16', 'sujet', 'm', ha='left')
y = 44; xr = rad(ax, 6, y, 22, h, 'sujet')
box(ax, xr + .5, y - 1, 21, h - 2, 'sujet', fill=False, dash=True)
text(ax, xr + 11, y + 4.2, r'$9+16$', 'encre', 'l')
text(ax, 62, y + 4.5, r'$=\sqrt{25}=5$', 'resultat', 'l')
text(ax, 4, 36, 'le trait couvre 9 seulement', 'autre', 'm', ha='left')
y = 18; xr = rad(ax, 6, y, 7, h, 'autre')
text(ax, xr + 3.5, y + 4.2, '9', 'encre', 'l')
text(ax, xr + 7 + 7, y + 4.2, r'$+16$', 'encre', 'l')
text(ax, 62, y + 4.5, r'$=3+16=19$', 'autre', 'l')
save(fig, '22-034')
