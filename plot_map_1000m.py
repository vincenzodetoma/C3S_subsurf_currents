import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import sys
plt.rcParams.update({'font.size':14})
variable=sys.argv[1]

surf_path='/DataArchive/C3S/subsurf_currents'

ds = xr.open_dataset(surf_path+'/Results/'+variable+'_1000m_ORCA-0.25x0.25_regular_1979_2018.nc')
ds.coords['lon'] = (ds.coords['lon'] + 180) % 360 - 180
ds = ds.sortby(ds.lon)
var = ds[variable].mean(dim='time').squeeze().rename(variable+r' $[m/s]$')

palette='RdBu_r'

fig = plt.figure(1, figsize=(15,8))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
p = var.plot.contourf(ax=ax, 
             transform=ccrs.PlateCarree(), 
             extend='both', 
             vmin=-0.10, 
             vmax=0.10,
             levels=41, 
             cmap=palette, 
             cbar_kwargs={'drawedges': True, 'shrink' : 0.65})
ax.coastlines('50m')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
fig.savefig(surf_path+'/Figures/'+variable+'_1000m_ORCA-0.25x0.25_regular_1979_2018.png', dpi=300, transparent=True)
plt.show()

