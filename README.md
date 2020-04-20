# C3S_subsurf_currents
This repository contains the scripts used to assess ORAS5 subsurface currents in the framework of the Copernicus C3S_511.
All scripts are produced with Python3 and bash scripts (single files have been merged using the cdo command mergetime), using the following libraries, loaded together in a conda environment:

xarray
matplotlib
numpy
cartopy
statsmodels

In the order, the Evaluation has proceeded as follows:
 - the script make_all_figures.sh make all the figures after the calculations;
 - vertmean15m.py and vertmean1000m.py calculate the different contributions,
 - calc_vert_mean15m.sh and calc_vert_mean1000m.sh iterate the procedure;
 - plot_map15m.py and plot_map_1000m.py produce the mean map, make_meanmaps.sh iterates the procedure;
 - std_plot_map_15m.py and std_plot_map_1000m.py produce the interannual variability maps;
 - horizontal trends done with subsurf_trend.py, make_trends.sh iterates the procedure;
 - plot_trend.py makes the correspondent figure, iterated by make_trend_figures.sh
 - make_figures.sh iterates the procedure and produce the figures for mean, variability, plot with arrows and trends;
 - section are extracted by the scripts section*, procedure iterated by calc_sections.sh;
 - section trends done with section_trends.py, iterated by make_section_trends.sh
 - section figures done with the script make_section_figures.sh, mean_section_plot.py for the mean,
 plot_section_trend.py for the trend;
 
 Files are not commented too much but code is easy to read. Ancillary routines are in the other files, such as slice_trend.py, trend_2d_parallel.py, running_mean.py, mk_test.py and bootstr_confidence.py. 
 
 for all further information please refer to:
 
 Vincenzo.DeToma@artov.ismar.cnr.it


