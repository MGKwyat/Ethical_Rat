# Example:
# python multiple_plot_copy.py multiple_file_plot_inp.csv

k = 653.2           # zero_Jy of the band
h = 1049.5
j = 1636.6  

import numpy as np
import matplotlib.pyplot as plt
import sys, csv, math, re


arg = sys.argv
ifile = open(sys.argv[1], "r")
reader = csv.reader(ifile, delimiter = ';')
header = reader.next()                              # read first row as input for columns
axes_scale = reader.next()                          # read second row as input for range and scale_factor
file_path0 = list(reader)

file_path = file_path0[0]
plot_factors = file_path0[1]
plot_factors1 = file_path0[3]

numerator = header[0]                   # data columns (row 2 col 1-4)
denominator = header[1]
fuvnuv1 = header[2]
fuvnuv2 = header[3]

a = []
b = []
all_data = [] 
nan = 'nan'


if ((header[1] == '1') and (header[3] == '1')):
    for f in file_path:
        jfile = open(f, "r")
        reader2 = csv.reader(jfile, delimiter= ';')
        header2 = reader2.next()
        header2 = [x.strip(' ') for x in header2]
        column1 = header2.index(numerator)
        column3 = header2.index(fuvnuv1)
        x0, y0 = [], []
        for row in reader2:
            col1 = row[column1]
            col3 = row[column3]
            x0.append(col1)
            y0.append(col3)
        
        zipped = zip(x0,y0)
        removed = [i for i in zipped if nan not in i]
        x1,y1 = zip(*removed)
        x, y = np.array(list(map(float,x1))), np.array(list(map(float,y1)))
        a.append(x)
        b.append(y)
    plt.xlabel(numerator)
    plt.ylabel(fuvnuv1)
    absmin_x = min(map(min, a))
    absmin_y = min(map(min, b))
    absmax_x = max(map(max, a))
    absmax_y = max(map(max, b))
    #/home/azin/rsg-K/rsg-K_smry.csv;/home/azin/symbio-v0/symbio-belczynski00_1_smry.csv
    
elif header[1] == '1':
    for f in file_path:
        jfile = open(f, "r")
        reader2 = csv.reader(jfile, delimiter= ';')
        header2 = reader2.next()
        header2 = [x.strip(' ') for x in header2]
        column1 = header2.index(numerator)               
        column2 = header2.index(fuvnuv1)         # fuv_avg input
        column3 = header2.index(fuvnuv2)
        
        x0, v0, w0 = [], [], []
        for row in reader2:
            col1 = row[column1]
            col2 = row[column2]
            col3 = row[column3]
            x0.append(col1)                        # fuv_avg
            v0.append(col2)                        # K band
            w0.append(col3)                        # FUV/NUV
            
        zipped = zip(x0, v0, w0)                   # zip three list together
        removed = [i for i in zipped if nan not in i and '0' not in i] # remove element if includ 'nan'
        x1, v1, w1 = zip(*removed)                    # unzip in three list
    
        x, v, w = np.array(list(map(float, x1))), np.array(list(map(float, v1))), np.array(list(map(float, w1)))
        y = np.divide(v,w)
        a.append(x)
        b.append(y)
        
    plt.xlabel(numerator)
    plt.ylabel(fuvnuv1 + ' /' + fuvnuv2)
    
elif header[3] == '1':
    for f in file_path:
        jfile = open(f, "r")
        reader2 = csv.reader(jfile, delimiter= ';')
        header2 = reader2.next()
        header2 = [x.strip(' ') for x in header2]
        if header[1][10] == 'K':                # Band flux conversion input
            band = k
        elif header[1][10] == 'J':
            band = j
        elif header[1][10] == 'H':
            band = h
        column1 = header2.index(numerator)
        column2 = header2.index(denominator)
        column3 = header2.index(fuvnuv1)
        
        v0, w0, y0 = [], [], []
        for row in reader2:
            col1 = row[column1]
            col2 = row[column2]
            col3 = row[column3]
            v0.append(col1)                        # fuv_avg
            w0.append(col2)                        # K band
            y0.append(col3)                        # FUV/NUV
        zipped = zip(v0, w0, y0)                   # zip three list together
        removed = [i for i in zipped if nan not in i and '0' not in i and ' ' not in i]# remove element if includ 'nan' & ' ' & '0'
        v1, w1, y1 = zip(*removed)
        v, w, y = np.array(list(map(float, v1))), np.array(list(map(float, w1))), np.array(list(map(float, y1)))
        w_input = (band * (10 ** (-0.4 * w))) * (10**6)       # convert input band magnitude to flux and Jy to microJy
        x1 = np.divide(v,w_input)
        xscale_factor = float(axes_scale[4])
        yscale_factor = float(axes_scale[5])
        x = x1 * xscale_factor
        a.append(x)
        b.append(y)
    plt.xlabel(numerator + '/' + denominator[10] + '  ' + '  scaled by ' + axes_scale[4])
    plt.ylabel(fuvnuv1)
else:   
    for f in file_path:
        jfile = open(f, "r")
        reader2 = csv.reader(jfile, delimiter= ';')
        header2 = reader2.next() 
        header2 = [x.strip(' ') for x in header2]
        if header[1][10] == 'K':                # Band flux conversion input
            band = k
        elif header[1][10] == 'J':
            band = j
        elif header[1][10] == 'H':
            band = h
            
        column1 = header2.index(numerator)
        column2 = header2.index(denominator)        
        column3 = header2.index(fuvnuv1)
        column4 = header2.index(fuvnuv2)
        v0, w0, u0, z0, star0 = [], [], [], [], []

        for row in reader2:
            col1 = row[column1]
            col2 = row[column2]
            col3 = row[column3]
            col4 = row[column4]
            col5 = row[0]
            
            v0.append(col1)                        
            w0.append(col2)                       
            u0.append(col3)                        
            z0.append(col4)                        
            star0.append(col5)
    
        zipped = zip(v0, w0, u0, z0, star0)
        removed = [i for i in zipped if nan not in i and '0' not in i and ' ' not in i] 
        v1, w1, u1, z1, star1 = zip(*removed)
        v, w, u, z = np.array(list(map(float, v1))), np.array(list(map(float, w1))), np.array(list(map(float, u1))), np.array(list(map(float, z1)))
        
        star1 = [x.strip(' ') for x in star1]
        removed = zip(v1, w1, u1, z1, star1)
        
        
        w_input = (band * (10 ** (-0.4 * w))) * (10** 6)
        x1 = np.divide(v,w_input)
        y1 = np.divide(u,z)
        xscale_factor = float(axes_scale[4])
        yscale_factor = float(axes_scale[5])
        x = x1 * xscale_factor
        y = y1 * yscale_factor
        a.append(x)
        b.append(y)
        all_data.append(removed)
        
        
    plt.xlabel(numerator + ' / ' + denominator[10] + '  scaled by ' + axes_scale[4])
    plt.ylabel(fuvnuv1 + ' / ' + fuvnuv2 + '  yscaled by ' + axes_scale[5])
    

spe_stars, spe_scale = [], []
for f in file_path0[2]:
    kfile = open(f, "r")
    reader3 = csv.reader(kfile, delimiter= ';')
    header3 = reader3.next()
    c, d = [], []
    for row in reader3:
        col1 = row[0]
        col2 = row[1]
        c.append(col1)
        d.append(col2)
    spe_stars.append(c)
    spe_scale.append(d)
print spe_stars 
spe_stars_index = []
for i in spe_stars:
    for f in i:
        res = [i for i, e1 in enumerate(star1) if f in e1]
        spe_stars_index.append(res[0])

spe_stars_data = []    
for f in spe_stars_index:
    for i in all_data:
        spe_stars_data.append(i[f])

a1,b1 = [], []
for f in spe_stars_data:
    v1, w1, u1, z1, star1 = zip(*spe_stars_data)
    v, w, u, z = np.array(list(map(float, v1))), np.array(list(map(float, w1))), np.array(list(map(float, u1))), np.array(list(map(float, z1)))
    w_input = (band * (10 ** (-0.4 * w))) * (10** 6)
    x1 = np.divide(v,w_input)   * xscale_factor
    y1 = np.divide(u,z)         * yscale_factor
    a1.append(x1)
    b1.append(y1)


if len(a) == 1:
    plt.scatter(a[0],b[0],edgecolors=plot_factors[2], marker=plot_factors[1] , label=plot_factors[0])
    plt.scatter(a1[0],b1[0],facecolor="none",edgecolors=plot_factors1[2], marker=plot_factors1[1] , label=plot_factors1[0])
elif len(a) == 2:
    plt.scatter(a[0],b[0],edgecolors=plot_factors[2], marker=plot_factors[1] , label=plot_factors[0])
    plt.scatter(a[1],b[1],edgecolors=plot_factors[5], marker=plot_factors[4] , label=plot_factors[3])
    plt.scatter(a1[0],b1[0],facecolor="none",edgecolors=plot_factors1[2], marker=plot_factors1[1] , label=plot_factors1[0])
    plt.scatter(a1[1],b1[1],facecolor='none',edgecolors=plot_factors1[5], marker=plot_factors1[4] , label=plot_factors1[3])
elif len(a) == 3:
    plt.scatter(a[0],b[0],edgecolors=plot_factors[2], marker=plot_factors[1] , label=plot_factors[0])
    plt.scatter(a[1],b[1],edgecolors=plot_factors[5], marker=plot_factors[4] , label=plot_factors[3])
    plt.scatter(a[2],b[2],edgecolors=plot_factors[8], marker=plot_factors[7] , label=plot_factors[6])
    plt.scatter(a1[0],b1[0],facecolor='none',edgecolors=plot_factors1[2], marker=plot_factors1[1] , label=plot_factors1[0])
    plt.scatter(a[1],b1[1],facecolor='none',edgecolors=plot_factors1[5], marker=plot_factors1[4] , label=plot_factors1[3])
    plt.scatter(a[2],b1[2],facecolor='none',edgecolors=plot_factors1[8], marker=plot_factors1[7] , label=plot_factors1[6])
elif len(a) == 4:
    plt.scatter(a[0],b[0],edgecolors=plot_factors[2], marker=plot_factors[1] , label=plot_factors[0])
    plt.scatter(a[1],b[1],edgecolors=plot_factors[5], marker=plot_factors[4] , label=plot_factors[3])
    plt.scatter(a[2],b[2],edgecolors=plot_factors[8], marker=plot_factors[7] , label=plot_factors[6])
    plt.scatter(a[3],b[3],edgecolors=plot_factors[11], marker=plot_factors[10] ,label=plot_factors[9])
    plt.scatter(a1[0],b1[0],facecolor='none',edgecolors=plot_factors1[2], marker=plot_factors1[1] , label=plot_factors1[0])
    plt.scatter(a1[1],b1[1],facecolor='none',edgecolors=plot_factors1[5], marker=plot_factors1[4] , label=plot_factors1[3])
    plt.scatter(a1[2],b1[2],facecolor='none',edgecolors=plot_factors1[8], marker=plot_factors1[7] , label=plot_factors1[6])
    plt.scatter(a1[3],b1[3],facecolor='none',edgecolors=plot_factors1[11], marker=plot_factors1[10] , label=plot_factors1[9])
elif len(a) == 5:
    plt.scatter(a[0],b[0],edgecolors=plot_factors[2], marker=plot_factors[1] , label=plot_factors[0])
    plt.scatter(a[1],b[1],edgecolors=plot_factors[5], marker=plot_factors[4] , label=plot_factors[3])
    plt.scatter(a[2],b[2],edgecolors=plot_factors[8], marker=plot_factors[7] , label=plot_factors[6])
    plt.scatter(a[3],b[3],edgecolors=plot_factors[11], marker=plot_factors[10] , label=plot_factors[9])
    plt.scatter(a[4],b[4],edgecolors=plot_factors[14], marker=plot_factors[13] , label=plot_factors[12])
    plt.scatter(a1[0],b1[0],facecolor='none',edgecolors=plot_factors1[2], marker=plot_factors1[1] , label=plot_factors1[0])
    plt.scatter(a1[1],b1[1],facecolor='none',edgecolors=plot_factors1[5], marker=plot_factors1[4] , label=plot_factors1[3])
    plt.scatter(a1[2],b1[2],facecolor='none',edgecolors=plot_factors1[8], marker=plot_factors1[7] , label=plot_factors1[6])
    plt.scatter(a1[3],b1[3],facecolor='none',edgecolors=plot_factors1[11], marker=plot_factors1[10] , label=plot_factors1[9])
    plt.scatter(a1[4],b1[4],facecolor='none',edgecolors=plot_factors1[14], marker=plot_factors1[13] , label=plot_factors1[12])

    
x_min = axes_scale[0]
x_max = axes_scale[1]
y_min = axes_scale[2]
y_max = axes_scale[3]
absmin_x = min(map(min, a))
absmin_y = min(map(min, b))
absmax_x = max(map(max, a))
absmax_y = max(map(max, b))

if len(x_min) == 0:                     #let x_min be an empty input to give min to max axes range plot
    plt.axis([0.7*absmin_x,7*absmax_x, 0.7*absmin_y,7*absmax_y]) 
    
else:                                   # if any values in x_min it will set to plot with input axes range.
    plt.axis([float(x_min),float(x_max),float(y_min),float(y_max)])

plt.xscale("log")                           # Turning axies into log scale
plt.yscale("log")
if len(plot_factors[0]) != 0:
    plt.legend()
#plt.show()

#INPUT FILE: multiple_flie_plot_inp.csv
# fuv_mean;%FLUXLIST(K);(FUV/NUV)mx;(FUV/NUV)mn
# ;10;0.001;10;1E6;1
# /home/azin/agbmaster_v5/agb4_M4-9+O-AGB_smry_simb_cln_multepoch.csv
# AGB;.;b;RSG-K;3;r;Symbiotic;+;g
# fuvagb-xray-special_2.csv;fuvagb-xray-special_3.csv
# AGB;s;red;RSG-K;o;r;Symbiotic;o;g

# SPECIAL FILE: fuvagb-xray-special_2.csv
# Star;scale
# CI Hyi;1
# --;1
# ----;2
# ----;1.5


