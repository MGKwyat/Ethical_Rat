for f in file_path:
    jfile = open(f, "r")
    reader2 = csv.reader(jfile, delimiter= ';')
    header2 = reader2.next()
    header2 = [x.strip(' ') for x in header2]
    if header[1][10] == 'K':            	# Band flux conversion input
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
	y1 = np.divide(u,z)     	* yscale_factor
	a1.append(x1)
	b1.append(y1)

INPUT FILE
column1;2;3;4
xmin;xmax;ymin;ymax;xscale;yscale
azin/home/filename;2;3;
legend;symbol;color;2;3;repete
special_file1;special_file2;

SPECIAL FILE
Star;scale
CI Hyi;1
--;1
----;2
----;1.5


