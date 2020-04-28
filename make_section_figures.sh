#!/bin/bash

python mean_section_plot.py vo A3 #vel_comp #section
python mean_section_plot.py uo P16
python mean_section_plot.py uo IR06
python mean_section_plot.py uo I06
python mean_section_plot.py uo A21
python mean_section_plot.py uo S3

#trend plot

python plot_section_trend.py vo A3 #vel_comp #section
python plot_section_trend.py uo P16
python plot_section_trend.py uo IR06
python plot_section_trend.py uo I06
python plot_section_trend.py uo A21
python plot_section_trend.py uo S3

#pvalue plot

python plot_section_pval.py vo A3 #vel_comp #section
python plot_section_pval.py uo P16
python plot_section_pval.py uo IR06
python plot_section_pval.py uo I06
python plot_section_pval.py uo A21
python plot_section_pval.py uo S3


