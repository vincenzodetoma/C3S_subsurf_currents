#!/bin/bash

python plot_map_15m.py uo
python plot_map_15m.py vo
python arrow_plot_15m.py
python plot_map_1000m.py uo
python plot_map_1000m.py vo
python arrow_plot_1000m.py
python std_plot_map_15m.py uo
python std_plot_map_15m.py vo
python std_plot_map_1000m.py uo
python std_plot_map_1000m.py vo


python plot_trend.py uo _trend_matrix top15m
python plot_trend.py vo _trend_matrix top15m
python plot_trend.py uo _trend_matrix 1000m
python plot_trend.py vo _trend_matrix 1000m

 
