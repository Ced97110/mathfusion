import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
def bk(cx, cy, w, h, role):
    for sgn in (-1, 1):
        xx = cx + sgn * w
        line(ax, [(xx - sgn * 1.5, cy + h), (xx, cy + h), (xx, cy - h), (xx - sgn * 1.5, cy - h)], role, lw=0.9)
text(ax, 44, 77, 'test avec deux matrices', 'encre', 's')
rows = [(66, 'a  b\nc  d', 'sujet', 'U quelconque'),
        (42, 'a  0\n0  d', 'varie', 'alors b = 0 et c = 0'),
        (18, 'a  0\n0  a', 'resultat', 'alors a = d : U = a × 1')]
for y, s, role, note in rows:
    text(ax, 16, y, s, role, 'l'); bk(16, y, 8, 5.5, role)
    text(ax, 30, y, note, role, 's', ha='left')
for y0, lab in ((58, 'commute avec (1 0 ; 0 0)'), (34, 'commute avec (0 1 ; 0 0)')):
    arrow(ax, (16, y0), (16, y0 - 10), 'varie')
    text(ax, 24, y0 - 5, lab, 'varie', 's', ha='left')
save(fig, '60-199')
