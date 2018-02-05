import pandas as pd
import numpy as np
import math
import jason
import sys
input = sys.argv[1]
parsed_json = json.load(open(input))

#Hair colour
from wheel.signatures.djbec import l

variant_a = {'rs86insA_a' : 1.2522, 'rs11547464_a' : -0.61155, 'rs885479_a' : 0.2937, 'rs1805008_a' : -0.50143, 'rs1805005_a' : 0.21172, 'rs1805006_a' : 1.93E+00, 'rs1805007_a' : -0.32318, 'rs1805009_a' : 0.60861, 'rsC456A_a' : 0.25624, 'rs2228479_a' : -0.054143, 'rs1110400_a' : -0.56315, 'rs28777_a' : 0.52168, 'rs16891982_a' : 0.75284, 'rs12821256_a' : -0.34957, 'rs4959270_a' : -0.19171, 'rs12203592_a' : 1.6475, 'rs1042602_a' : 0.16092, 'rs1800407_a' : -0.19111, 'rs2402130_a' : 0.35821, 'rs12913832_a' : 1.214, 'rs2378249_a' : 0.12669, 'rs683_a' : 0.21172}

variant_b = {'rs86insA_b' : 25.508, 'rs11547464_b' : 2.5381, 'rs885479_b' : -0.20889, 'rs1805008_b' : 2.801, 'rs1805005_b' : 0.93493, 'rs1805006_b' : 3.65E+00, 'rs1805007_b' : 3.4408, 'rs1805009_b' : 4.5868, 'rsC456A_b' : 22.107, 'rs2228479_b' : 0.62307, 'rs1110400_b' : 1.4453, 'rs28777_b' : 0.70401, 'rs16891982_b' : -0.41869, 'rs12821256_b' : -0.57964, 'rs4959270_b' : 0.24861, 'rs12203592_b' : 0.90233, 'rs1042602_b' : 0.45003, 'rs1800407_b' : -0.27606, 'rs2402130_b' : 0.28313, 'rs12913832_b' : -0.093776, 'rs2378249_b' : 0.76634, 'rs683_b' : -0.053427}

variant_c = {'rs86insA_c' : 2.732, 'rs11547464_c' : -16.969, 'rs885479_c' : 0.39983, 'rs1805008_c' : -0.86062, 'rs1805005_c' : -0.0029013, 'rs1805006_c' : -1.61E+01, 'rs1805007_c' : -1.3757, 'rs1805009_c' : 0.060631, 'rsC456A_c' : 3.9824, 'rs2228479_c' : 0.17012, 'rs1110400_c' : 0.29143, 'rs28777_c' : 0.82228, 'rs16891982_c' : 1.1617, 'rs12821256_c' : -0.89824, 'rs4959270_c' : -0.36359, 'rs12203592_c' : 1.997, 'rs1042602_c' : 0.065432, 'rs1800407_c' : -0.49601, 'rs2402130_c' : 0.26536, 'rs12913832_c' : 1.9391, 'rs2378249_c' : -0.089509, 'rs683_c' : 0.15796}

results_a = []
for key, value in variant_a.iteritems():
    if 'input' >= 0:
        print (value *  'input')
    results_a.append(value * 'input')
np.hstack(results_a)
print(results_a)

results_b = []
for key, value in variant_b.iteritems():
    if 'input'>= 0:
        print (value *  'input')
    results_b.append(value * 'input')
np.hstack(results_b)

results_c = []
for key, value in variant_c.iteritems():
    if 'input' >= 0:
        print (value *  'input')
    results_c.append(value * 'input')
np.hstack(results_c)

x = exp(-2.0769) + results_a
y = exp(-6.3953) + results_b
z = exp(-2.4029) + results_c

probability of Brown hair = x/(1+(x+y+z))

probability of Black hair = y+(1+(x+y+z))

probability of Blonde hair = z/(1+(x+y+z))

probability of Red hair = (x+y+z)

#Eye colour
variant_d = {'rs12913832_d' : -4.87, 'rs1800407_d' : 1.15, 'rs12896399_d' : -0.53, 'rs16891982_d' : -1.53, 'rs1393350_d' : 0.44, 'rs12203592_d' : 0.60}

variant_e = { 'rs12913832_e' : -1.99, 'rs1800407_e' : 1.05, 'rs1289699_e' : -0.01, 'rs16891982_e' : -0.74, 'rs1393350_e' : 0.26, 'rs12203592_e' : 0.69}

results_d = []
for key, value in variant_d.iteritems():
    if 'input' >= 0:
        print(value * 'input')
    results_d.append(value * 'input')
np.hstack(results_d)

results_e = []
for key, value in variant_d.iteritems():
    if 'input' >= 0:
        print(value * 'input')
    results_e.append(value * 'input')
np.hstack(results_e)

a = exp(3.84) + results_d
b = exp(0.37) + results_e

probability of blue eyes = a/(1+(a+b)) = l

probability of green eyes = b/(1+(a+b)) = g

probability of brown eyes = 1 - l - g

#Hair shade
variant_f = {'rs11547464_f' : -16.575, 'rs885479_f' : 0.18709, 'rs1805008_f' : -0.9331, 'rs1805005_f' : -0.030452, 'rs1805006_f' : -15.305, 'rs1805007_f' : -1.7901, 'rs1805009_f' : -0.078426, 'rs2228479_f' : 0.0049399, 'rs1110400_f' : -0.15892, 'rs28777_f' : 1.4594, 'rs16891982_f' : 0.78071, 'rs12821256_f' : -0.7757, 'rs4959270_f' : -0.44286, 'rs12203592_f' : 1.8636, 'rs1042602_f' : 0.18179, 'rs1800407_f' : -0.59583, 'rs2402130_f' : 0.33304, 'rs12913832_f' : 1.9622, 'rs2378249_f' : 0.090083, 'rs683_f' : 0.18114}

results_f = []
for key, value in variant_d.iteritems():
    if 'input' >= 0:
        print(value * 'input')
    results_f.append(value * 'input')
np.hstack(results_f)

c = exp(-2.528) + results_f

probability of dark shade = c

probability of light shade = 1 - c

