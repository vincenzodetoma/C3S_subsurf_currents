import xarray as xr
import sys
variable=sys.argv[1]
year=sys.argv[2]
month=sys.argv[3]
data_path='/DataArchive/C3S/ORAS5/REGULAR/opa0/'
weight_path = '/DataArchive/cyang/GLORYS_Atlantic/GRID/ORAS5'
dest_path = '/DataArchive/C3S/subsurf_currents/'
dm = xr.open_dataset(weight_path+'/'+'mesh_mask.nc').rename({'t': 'time', 'z': 'depth'})
ds = xr.open_dataset(data_path+variable+'/'+variable+'_ORCA-0.25x0.25_regular_'+year+month+'.nc')
var = ds[variable]
dz = dm['e3w_1d']

vert_mean_15m = ((var*dz).sel(depth=slice(0,15)).mean(dim='depth')).rename(variable)
vert_mean_15m.to_netcdf(dest_path+'tmp/'+year+'/'+variable+'_top15m_ORCA-0.25x0.25_regular_'+year+month+'.nc')

ds.close()
dm.close()
