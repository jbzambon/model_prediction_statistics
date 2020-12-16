# model_prediction_statistics
Model Prediction Statistics from Stow et al. "Skill assessment for coupled biological/physical models of marine systems" JMS 2009

Requires math

```
import model_prediction_statistics19 as mps
r = mps.corrcoef(verif[:,4], wrf_only[0:t_end:2,2])
rmse = mps.rmse(verif[:,4], wrf_only[0:t_end:2,2])
ri = mps.ri(verif[:,4], wrf_only[0:t_end:2,2])
ae = mps.ae(verif[:,4], wrf_only[0:t_end:2,2])
aae = mps.aae(verif[:,4], wrf_only[0:t_end:2,2])
mef = mps.mef(verif[:,4], wrf_only[0:t_end:2,2])

print(r)
0.8720372545794709
print(rmse)
14.505171491574997
print(ri)
print(ae)
print(aae)
print(mef)

Last Updated: 16 December 2020  
Joseph B. Zambon  
jbzambon@ncsu.edu
