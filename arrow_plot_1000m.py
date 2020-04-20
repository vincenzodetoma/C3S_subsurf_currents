import xarray as xr
import xarray.ufuncs as xu
import numpy as np
import matplotlib.pyplot as plt
import sys
import cartopy.crs as ccrs
import cmocean
plt.rcParams.update({'font.size': 14})

surf_path='/DataArchive/C3S/subsurf_currents'

dv = xr.open_dataset(surf_path+'/Results/'+'vo_1000m_ORCA-0.25x0.25_regular_1979_2018.nc')
du = xr.open_dataset(surf_path+'/Results/'+'uo_1000m_ORCA-0.25x0.25_regular_1979_2018.nc')
dv.coords['lon'] = (dv.coords['lon'] + 180) % 360 - 180
dv = dv.sortby(dv.lon)
du.coords['lon'] = (du.coords['lon'] + 180) % 360 - 180
du = du.sortby(du.lon)
v = dv['vo'].squeeze()
u = du['uo'].squeeze()
speed = xu.sqrt(u**2 + v**2)
v_av = v.mean(dim='time')
u_av = u.mean(dim='time')
speed_av = speed.mean(dim='time').rename('speed'+r' $[m/s]$')
N=1
palette='YlOrRd'
f = plt.figure(1, figsize=(15,8))
ax = plt.axes(projection=ccrs.PlateCarree())
p = speed_av.plot.contourf(ax=ax, transform=ccrs.PlateCarree(),
                  extend='max', 
                  cmap=palette,
                  vmin=0.,
                  vmax=0.3,
                  levels=31, 
                  cbar_kwargs={'drawedges': True, 'shrink' : 0.65})
x=v_av.coords['lon'].values
y=v_av.coords['lat'].values
ax.streamplot(x[::N], y[::N],
              u_av[::N,::N].values, 
              v_av[::N,::N].values, 
              transform=ccrs.PlateCarree(),
              linewidth=1., 
              color='k', 
              density=5, 
              minlength=0.05, 
              maxlength=7., 
              arrowstyle='->', 
              integration_direction='forward')
ax.coastlines('50m')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
plt.savefig(surf_path+'/Figures/'+'speed_1000m_arrowplot.png', dpi=300, transparent=True)
plt.show()

