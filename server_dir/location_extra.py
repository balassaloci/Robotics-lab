def get_hist(data, resolution):
    max = 255.0
    min = 0.0

    hist = [0.0] * resolution

    for x in data:
        mapped = (x - min) / max
        slot = int(mapped * resolution)
        hist[slot] += 1

    return hist

def match_hist(a, b):
    diffs = 0.0
    for x in range(len(a)):
        d = a[x] - b[x]
        diffs += d**2

    rms_err = math.sqrt(diffs)

    return rms_err
xes = [float(x) for x in range(0, 255)]
a = get_hist(xes, 10)
b = get_hist(xes, 10)

print match_hist(a, b)
print(hist)
