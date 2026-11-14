import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
u=7
for i in range(4):
    for j in range(4):
        r=max(i,j); role='sujet' if r<2 else 'varie'
        poly(ax,[(4+i*u,6+j*u),(4+(i+1)*u,6+j*u),(4+(i+1)*u,6+(j+1)*u),(4+i*u,6+(j+1)*u)],role,lw=0.6)
text(ax,4+u,6+u,'4','sujet','m'); text(ax,4+2.5*u,6+2.5*u,'+5','varie','s'); text(ax,4+3.5*u,6+3.5*u,'+7','varie','s')
labels=[('côté 2 · aire 4','sujet'),('côté 3 · aire 9','varie'),('côté 4 · aire 16','varie')]
for k,(s,r) in enumerate(labels):
    box(ax,40,6+12*k,44,7,r,label=s,size='s')
for k,s in enumerate(['côté +1 : aire +5','côté +1 : aire +7']):
    arrow(ax,(46,13+12*k),(46,18+12*k),'varie'); text(ax,50,15.5+12*k,s,'varie','s',ha='left')
save(fig,'22-120')
