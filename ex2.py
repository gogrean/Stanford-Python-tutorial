for det, lc in zip(detector, light_curve):
    times = list(lc.keys())
    ct_rate = np.array([x[0] for x in lc.values()])
    ct_rate_err = np.array([x[1] for x in lc.values()])
    min_ct_rate = np.array([x[0] - x[1] for x in lc.values()])
    max_ct_rate = np.array([x[0] + x[1] for x in lc.values()])
    
    max_jump = times[np.argmax(max_ct_rate[1:] - min_ct_rate[:-1]) + 1]
    print("Jump in light curve from detector %s happens at %.2f seconds." % (det.upper(), max_jump))
