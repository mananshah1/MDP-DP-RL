import numpy as np
T = 10
M = 200
el = [(10.0, 10.0), (9.0, 16.0), (8.0, 20.0), (7.0, 23.0), (6.0, 25.0), (5.0, 26.0)]

v = np.zeros((T + 1, M + 1))
pi = np.zeros((T, M + 1))
for t in range(T - 1, -1, -1):
    for s in range(M + 1):
        vals = np.zeros(len(el))
        for i in range(len(el)):
            p = el[i][0]
            ld = el[i][1]
            prob_sum = 0.
            mult = 1.
            for d in range(s):
                if d > 1:
                    mult *= d
                prob = (np.exp(-ld) * ld ** d) / mult
                vals[i] += prob * (d * p + v[t + 1, s - d])
                prob_sum += prob
            vals[i] += (1. - prob_sum) * (s * p + v[t + 1, 0])
        v[t, s] = np.max(vals)
        pi[t, s] = el[int(np.argmax(vals))][0]
print(pi)
print(v)
