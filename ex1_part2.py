os.chdir("/Users/gogrean/code/python_tutorial/data")
files = ["glg_tte_n6_bn090510016_v00.txt", 
         "glg_tte_n7_bn090510016_v00.txt", 
         "glg_tte_n9_bn090510016_v00.txt"]
light_curve = []

for file in files:
    lc = make_light_curve(file)
    light_curve.append(lc)

n_light_curves = len(light_curve)

# Estimates for the peak times.
peak_loc = [0.54, 0.58, 0.665, 0.73, 0.825]

# Get detector from file name.
detector = [s[8:10] for s in files]

min_rate = lambda y: [x[0] - x[1] for x in y.values()]
max_rate = lambda y: [x[0] + x[1] for x in y.values()]

fig, ax = plt.subplots(n_light_curves, figsize=(12,10), sharex=True, sharey=True)
for det, lc, axis, color in zip(detector, light_curve, ax, colors):
    times = list(lc.keys())
    ct_rate = [x[0] for x in lc.values()]
    ct_rate_err = [x[1] for x in lc.values()]
    min_ct_rate = min_rate(lc)
    max_ct_rate = max_rate(lc)
    axis.step(times, ct_rate, c=color, linewidth=2)
    for peak in peak_loc:
        axis.plot([peak]*2, [0,10], c=color, linestyle='dashed', linewidth=2, alpha=0.5)
    axis.set_xlim([0,1.3])
    axis.set_ylim([np.min(ct_rate)*0.5, np.max(ct_rate)*1.3])
    
    axis.fill_between(times, min_ct_rate, max_ct_rate, color=color, 
                      step='pre', alpha=0.3)
    axis.text(1.2, 0.9, det.upper(), fontsize=16)

plt.xlabel('Time (s)', fontsize=16)

big_ax = fig.add_subplot(111, frameon=False)
big_ax.set_axis_bgcolor('none')
big_ax.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
big_ax.set_ylabel(r'Count rate ($10^4$ photons s$^{-1}$)', fontsize=16)

fig.subplots_adjust(hspace=0)
