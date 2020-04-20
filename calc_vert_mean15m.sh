#!/bin/bash

dir=/DataArchive/C3S/subsurf_currents
for (( y=1979;y<=2018;y++ ));do
  mkdir -p ${dir}/tmp/${y}
  for (( m=1;m<=12;m++ ));do
    python vertmean_15m.py uo ${y} `printf "%02d" ${m}`
    python vertmean_15m.py vo ${y} `printf "%02d" ${m}`
  done
done
cdo mergetime ${dir}/tmp/*/uo_top15m_ORCA-0.25x0.25_regular_*.nc ${dir}/Results/uo_top15m_ORCA-0.25x0.25_regular_1979_2018.nc

cdo mergetime ${dir}/tmp/*/vo_top15m_ORCA-0.25x0.25_regular_*.nc ${dir}/Results/vo_top15m_ORCA-0.25x0.25_regular_1979_2018.nc

