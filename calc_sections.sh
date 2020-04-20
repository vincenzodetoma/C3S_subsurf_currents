#!/bin/bash

subsurf_dir=/home/Vincenzo.DeToma/April_deliverables/subsurf_currents

for (( y=1979;y<=2018;y++ ));do
  mkdir -p ${subsurd_dir}/tmp/${y}
  for (( m=1;m<=12;m++ ));do
    python section_A3.py uo ${y} `printf "%02d" ${m}`
    python section_A3.py vo ${y} `printf "%02d" ${m}`
    python section_P16.py uo ${y} `printf "%02d" ${m}`
    python section_P16.py vo ${y} `printf "%02d" ${m}`
    python section_IR06.py uo ${y} `printf "%02d" ${m}`
    python section_IR06.py vo ${y} `printf "%02d" ${m}`
    python section_I06.py uo ${y} `printf "%02d" ${m}`
    python section_I06.py vo ${y} `printf "%02d" ${m}`
    python section_A21.py uo ${y} `printf "%02d" ${m}`
    python section_A21.py vo ${y} `printf "%02d" ${m}`
    python section_S3.py uo ${y} `printf "%02d" ${m}`
    python section_S3.py vo ${y} `printf "%02d" ${m}`
  done
done
cdo mergetime ${subsurf_dir}/tmp/*/uo_A3_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/uo_A3_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/uo_P16_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/uo_P16_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/uo_IR06_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/uo_IR06_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/uo_I06_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/uo_I06_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/uo_A21_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/uo_A21_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/uo_S3_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/uo_S3_ORCA-0.25x0.25_regular_1979_2018.nc

cdo mergetime ${subsurf_dir}/tmp/*/vo_A3_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/vo_A3_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/vo_P16_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/vo_P16_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/vo_IR06_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/vo_IR06_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/vo_I06_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/vo_I06_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/vo_A21_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/vo_A21_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/vo_S3_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/vo_S3_ORCA-0.25x0.25_regular_1979_2018.nc






