''' Made by Vincenzo de Toma on 21/04/2020'''
import xarray as xr
import xarray.ufuncs as xu
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cartopy.crs as ccrs
import sys
plt.rcParams.update({'font.size':18})
variable='uo'
surf_path='/DataArchive/C3S/subsurf_currents'
ds = xr.open_dataset(surf_path+'/Results/'+variable+'_EUC_ORCA-0.25x0.25_regular_1979_2018.nc')
var = (ds['EUC'] - ds['EUC'].mean(dim='time')).rename(r'EUC Velocity Anomalies $[m~s^{-1}]$')

fig=plt.figure(1, figsize=(15,8))
ax=fig.add_subplot(111)
p = var.plot.line('o-', ax=ax, label='EUC Monthly Anomalies', color='blue')
ax.legend(loc='best')
fig.tight_layout()
fig.savefig(surf_path+'/Figures/'+variable+'_EUC_anom_ORCA-0.25x0.25_regular_1979_2018.png', dpi=300, transparent=True)
plt.show()

