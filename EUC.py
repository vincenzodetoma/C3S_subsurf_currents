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
months=['01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

EUC_list = []
for year in range(1979,2019):
  print(year)
  for month in months:
    data_path='/DataArchive/C3S/ORAS5/REGULAR/opa0/'+variable+'/'
    namefile = variable+'_ORCA-0.25x0.25_regular_'+str(year)+month+'.nc'
    ds = xr.open_dataset(data_path+'/'+namefile)
    varname=variable
    EUC = ds[varname].sel(lat=slice(-2,2), lon=slice(270,330), depth=slice(10,300)).max(dim=['lat', 'lon', 'depth'])
    EUC_list.append(EUC)
    ds.close()

xr_EUC = xr.concat([e for e in EUC_list], dim='time').rename('EUC')
xr_EUC.attrs['long_name'] = r'EUC Velocity'
xr_EUC.attrs['units'] = r'$m~s^{-1}$'

surf_path='/DataArchive/C3S/subsurf_currents'
xr_EUC.to_netcdf(surf_path+'/Results/'+variable+'_EUC_ORCA-0.25x0.25_regular_1979_2018.nc')
surf_path='/DataArchive/C3S/subsurf_currents'
ds = xr.open_dataset(surf_path+'/Results/'+variable+'_EUC_ORCA-0.25x0.25_regular_1979_2018.nc')
var = ds['EUC']

fig=plt.figure(1, figsize=(15,8))
ax=fig.add_subplot(111)
p = var.plot.line('o-', ax=ax, label='EUC Monthly', color='blue')
ax.legend(loc='best')
fig.tight_layout()
#fig.savefig(surf_path+'/Figures/'+variable+'_EUC_ORCA-0.25x0.25_regular_1979_2018.png', dpi=300, transparent=True)
plt.show()

