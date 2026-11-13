import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
h = 8
def sq(cx, cy, lab, role):
    poly(ax, [(cx-h,cy-h),(cx+h,cy-h),(cx+h,cy+h),(cx-h,cy+h)], role)
    for (dx, dy), l in zip([(-h,h),(h,h),(h,-h),(-h,-h)], lab):
        disc(ax, cx+dx, cy+dy, 2.6, role, label=l, size='s')
sq(44, 70, 'abcd', 'sujet')
sq(20, 20, 'adcb', 'autre')
sq(68, 20, 'cbad', 'varie')
arrow(ax, (36, 60), (24, 31), 'autre')
arrow(ax, (52, 60), (64, 31), 'varie')
text(ax, 17, 47, 's puis r', 'autre', 's')
text(ax, 71, 47, 'r puis s', 'varie', 's')
line(ax, [(40, 21.5), (48, 21.5)], 'limite', lw=1.6)
line(ax, [(40, 18.5), (48, 18.5)], 'limite', lw=1.6)
line(ax, [(42, 15), (46, 25)], 'limite', lw=1.6)
text(ax, 44, 4, 'deux résultats différents', 'limite', 'm')
text(ax, 72, 70, 'départ', 'sujet', 'm')
save(fig, '49-286')
