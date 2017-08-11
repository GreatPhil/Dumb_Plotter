#!/usr/bin/python
'''This script is used for plotting car prices per miles.
   The input file for this script must contain data similar to car_info.txt'''

import matplotlib.mlab as mlab

# Set some params:
input_filemame = "car_info.txt"
num_cols = 10
num_rows = 10

# Helper function:
def count_string(x):
    if (x == 0):
        return ""
    else:
        return str(x)

# Start main script here...
print "\nCAR PLOTTER, v1.0\nSource Data = '{0}'\n".format(input_filemame)

# Read in Car Info:
index = 0
car_info = {}
with open(input_filemame) as fh:
    for line in fh.readlines():
        car_info[index] = [x.strip() for x in line.split(":")]
        index += 1

# Get min and max miles and price in data set:
min_miles = min(float(tp[1][3].replace(",","")) for tp in car_info.iteritems())
max_miles = max(float(tp[1][3].replace(",","")) for tp in car_info.iteritems())
min_price = min(float(tp[1][4].replace(",","")) for tp in car_info.iteritems())
max_price = max(float(tp[1][4].replace(",","")) for tp in car_info.iteritems())

# Get X Plot Ranges:
x_span = max_miles - min_miles
x_min  = min_miles - 0.1 * x_span
x_max  = max_miles + 0.1 * x_span
x_span = x_max - x_min

# Get Y Plot Ranges:
y_span = max_price - min_price
y_min  = min_price - 0.1 * y_span
y_max  = max_price + 0.1 * y_span
y_span = y_max - y_min

x_points = mlab.frange(x_min, x_max, x_span/num_cols)
y_points = mlab.frange(y_min, y_max, y_span/num_rows)

# Fill in Scatter-Plot Table:
scatter_plot = []

for y in range(num_rows):

    scatter_plot.append([])

    for x in range(num_cols):

        count = 0

        for tp in car_info.iteritems():

            if(float(tp[1][4].replace(",","")) >= y_points[y] and float(tp[1][4].replace(",","")) < y_points[y+1] and
               float(tp[1][3].replace(",","")) >= x_points[x] and float(tp[1][3].replace(",","")) <  x_points[x+1]):
                 count += 1

        scatter_plot[y].append(count)

# Plot the Data:
y_counter = 1

for y in reversed(y_points):

    # Print Y-Axis:
    print "{0:7s}|".format("${0:4.1f}K".format(y/1000)),
    print ". . . . " * num_cols

    print "       |  ",

    # Print Data:
    if (y_counter <= num_rows):
        print "".join(["{0:4s}.   ".format(count_string(x)) for x in scatter_plot[num_rows-y_counter]])
    else:
        print "    |   " * num_cols

    y_counter += 1

# Print X-Axis
print "MI: ",
for x in x_points:
    print "{0:7s}".format("{0:0.1f}K".format(x/1000)),

print "\n\nTOTAL = {0} data points.\n".format(index)


# GOOD DEAL???
# https://sfbay.craigslist.org/sfc/cto/d/porsche-911/6230679423.html
