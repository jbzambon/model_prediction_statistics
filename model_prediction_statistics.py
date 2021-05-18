# model_prediciton_statistics.py
# Program to compute 6 metrics between observed and predicted values:
#     Correlation Coefficient (r)
#     Root Mean Squared Error (RMSE)
#     Reliability Index (RI)
#     Average Error (Bias)
#     Absolute Average Error
#     Modelling Efficiency
# x = observations
# y = predicitons
#
# Source:
#   Craig A. Stow, Jason Jolliff, Dennis J. McGillicuddy, Scott C. Doney, Icarus Allen
#     Marjorie A.M. Friedrichs, Kenneth A. Rose, and Philip Wallhead
#   Skill assessment for coupled biological/physical models of marine systems
#   Journal of Marine Systems, 76, 1-2, p. 4-15
#   https://doi.org/10.1016/j.jmarsys.2008.03.011
#
# Joseph B. Zambon
#  16-December 2020
#  jbzambon@ncsu.edu

import math

def corrcoef(x,y):
    if len(x) != len(y):
        raise ValueError("Arrays must have the same size")
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)
    r_t    = 0
    o_t    = 0
    p_t    = 0
    r      = 0
    for t in range(0,len(x)):
        r_t = r_t + (x[t]-mean_x)*(y[t]-mean_y)
        o_t = o_t + (x[t]-mean_x)**2
        p_t = p_t + (y[t]-mean_y)**2
    r = r_t/(o_t*p_t)**0.5
    return r

def rmse(x,y):
    if len(x) != len(y):
        raise ValueError("Arrays must have the same size")
    n = len(x)
    rmse_t = 0
    for t in range(0,len(x)):
        rmse_t = rmse_t + ( ( y[t] - x[t] ) **2 )
    rmse_c = ( rmse_t / n ) **0.5
    return rmse_c

def ri(x,y):
    if len(x) != len(y):
        raise ValueError("Arrays must have the same size")
    n = len(x)
    ri_t = 0
    for t in range(0,len(x)):
        ri_t = ri_t + ( math.log( x[t] / y[t] ) **2 )
    ri_c = math.exp( ( ri_t / n ) **0.5 )
    return ri_c
    
def ae(x,y):
    if len(x) != len(y):
        raise ValueError("Arrays must have the same size")
    n = len(x)
    ae_t = 0
    for t in range(0,len(x)):
        ae_t = ae_t + ( y[t] - x[t] )
    ae_c = ae_t / n
    return ae_c

def aae(x,y):
    if len(x) != len(y):
        raise ValueError("Arrays must have the same size")
    n = len(x)
    aae_t = 0
    for t in range(0,len(x)):
        aae_t = aae_t + abs( y[t] - x[t] )
    aae_c = aae_t / n
    return aae_c

def mef(x,y):
    if len(x) != len(y):
        raise ValueError("Arrays must have the same size")
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)
    o_t    = 0
    p_t    = 0
    for t in range(0,len(x)):
        o_t = o_t + (x[t]-mean_x)**2
        #p_t = p_t + (y[t]-mean_y)**2    #Error caught by S. Mao
        p_t = p_t + (y[t]-x[t])**2
    mef_c = (o_t - p_t) / o_t
    return mef_c
