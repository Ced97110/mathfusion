import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'alphabet $\{a,\ b\}$', 'fixe', 'm')
R = {'a': 'sujet', 'b': 'autre'}
def word(x, y, w, s=7):
    for i, ch in enumerate(w):
        box(ax, x + i * s, y, s, s, R[ch], label=ch, size='m', r=0.5)
for i, w_ in enumerate(['ab', 'bba', 'a', 'bbbb', 'ba']):
    y = 52 - i * 10.5
    word(24, y, w_)
    text(ax, 2, y + 3.5, f'{len(w_)} lettre' + ('s' if len(w_) > 1 else ''), 'fixe', 's', ha='left')
text(ax, 84, 13.5, 'ab ≠ ba', 'limite', 's', ha='right')
save(fig, '44-075')
