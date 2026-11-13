import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
w, step, x0 = 10.0, 13.5, 4.0
def chain(y, labs, brace_label):
    for i, l in enumerate(labs):
        x = x0 + i * step
        box(ax, x, y, w, 9, 'fixe' if l == '…' else 'sujet', label=l, size='s', dash=(l == '…'))
        if i < len(labs) - 1:
            arrow(ax, (x + w + 0.3, y + 4.5), (x + step - 0.3, y + 4.5), 'varie')
    xe = x0 + (len(labs) - 1) * step + w
    line(ax, [(xe + 2.5, y + 0.5), (xe + 2.5, y + 8.5)], 'resultat', lw=1.8)
    brace(ax, x0, xe, y - 1.5, 'resultat', label=brace_label)
chain(50, ['48', '24', '12', '6', '3'], '5 nombres, puis fin')
chain(22, ['1024', '512', '256', '…', '4', '2'], '10 nombres, puis fin')
save(fig, '56-072')
