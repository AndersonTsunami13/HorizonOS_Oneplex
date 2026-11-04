# dynamicbar.py

from Engine.MDL_dynamic_bar import mdl_dynamic_bar_start, mdl_dynamic_bar, mdl_dynamic_bar_finish

def f_dynamic_bar_start(argumento1="HorizonUI", argumento2=True, argumento3=True):
    mdl_dynamic_bar_start(
        titulo=argumento1,
        hora=argumento2,
        tempo=argumento3
    )

def f_dynamic_bar(argumento):
    mdl_dynamic_bar(argumento)

def f_dynamic_bar_finish(argumento):
    mdl_dynamic_bar_finish()