import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [5.25, 11.75, 20.25, 26.75, 33.25, 41.75, 48.25, 54.75, 63.25, 69.75, 76.25]
for i, x in enumerate(xs):
    box(ax, x, 34, 6.5, 8, 'sujet', label='2' if i == 0 else '0', size='m', lw=1.3 if i == 0 else 0.8, r=0.6)
brace(ax, 5.25, 82.75, 43, 'sujet', label='11 signes', down=False, size='m')
text(ax, 44, 29, 'on lit : 20 milliards', 'resultat', 's')
for i in range(40):
    x = 5 + 1.4 * i
    line(ax, [(x, 12), (x, 20)], 'limite', lw=0.6)
line(ax, [(62, 16), (83, 16)], 'limite', lw=0.9, dash=True)
text(ax, 44, 6, 'pas 20 milliards de traits', 'limite', 's')
save(fig, '01-100')
