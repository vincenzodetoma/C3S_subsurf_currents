import xarray as xr
import sys
variable=sys.argv[1]
year=sys.argv[2]
month=sys.argv[3]
data_path='/DataArchive/C3S/ORAS5/REGULAR/opa0/'
dest_path = '/DataArchive/C3S/subsurf_currents/'
ds = xr.open_dataset(data_path+variable+'/'+variable+'_ORCA-0.25x0.25_regular_'+year+month+'.nc')
var = ds[variable]

vert_mean_15m = var.sel(depth=slice(950,1050)).squeeze(dim='depth').rename(variable)
vert_mean_15m.to_netcdf(dest_path+'tmp/'+year+'/'+variable+'_1000m_ORCA-0.25x0.25_regular_'+year+month+'.nc')

ds.close()
