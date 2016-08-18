def make_light_curve(fname):
    times = []
    with open(file) as f:
        for line in f.readlines()[1:]:
            data_in_line = line.split()
            time_as_string = data_in_line[0]
            time_as_float = float(time_as_string)
            times.append(time_as_float)

    lc = OrderedDict()
    i = 0
    j = 1
    while j < len(times):
        if times[j] - times[i] >= MIN_BIN_WIDTH:
            c_time = 0.5 * (times[j] + times[i])
            lc[c_time] = ((j - i + 1) / (times[j] - times[i]) / 1e4,
                          np.sqrt(j - i + 1) / (times[j] - times[i]) / 1e4)
            i = j
            j += 1
        else:
            j += 1
    return lc
