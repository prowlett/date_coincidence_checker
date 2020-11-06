"""
digit sums for dates in a year

Looks at all days over a year starting at start_date_str and sums the digits of the day, month and two-digit year. Reports:

- the digit sum for each day in the year;
- the number of days in the year matching each digit sum;
- a bar chart of digit sums against number of days in the year matching this digit sum

Example: 2020-10-31 sums as 20-10-31 giving 2+0+1+0+3+1=7.

Ref. https://twitter.com/aa42john/status/1324405199419674624
"""

import datetime
from matplotlib import pyplot as plt,ticker

# Edit this to change the start date
start_date_str = "2020-01-01"

# format start as date and end a year later
start_date = datetime.date.fromisoformat(start_date_str)
end_date = datetime.date(start_date.year+1,start_date.month,start_date.day)

# to store the digit sums
digit_sum = []
for i in range(0,39):
    digit_sum.append(0)

# calculate and print digit sum per day
print("Dates this year")
while start_date<end_date:
    this_sum=0
    for y in str(start_date.year)[2:]: # last two digits of the year
        this_sum+=int(y)
    for m in str(start_date.month): # month digits
        this_sum+=int(m)
    for d in str(start_date.day): # day digits
        this_sum+=int(d)
    # store and print
    digit_sum[this_sum]+=1
    print("{}: {}".format(start_date,this_sum))
    # increment date by one day
    start_date += datetime.timedelta(days=1)

# print digit sum frequencies
print("Number of dates matching each digit sum")
firstds = 0
lastds = 40
for i in range(1,39):
    if digit_sum[i]!=0:
        lastds = i # find the last non-zero digit sum (for the plot)
        if firstds==0:
            firstds = i # find the first non-zero digit sum (for the plot)
    print("{}: {} matches".format(i,digit_sum[i]))

# Plot a bar chart of digit sum frequencies
plt.bar(range(firstds,lastds+1),digit_sum[firstds:lastds+1])
plt.xlabel("Digit sum")
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1)) # force integer x-axis with interval 1
plt.ylabel("Number of days with this digit sum")
plt.title("Counts of digit sums for {} to {}.".format(start_date_str,(end_date-datetime.timedelta(days=1)).isoformat())) # e.g. "Counts of digit sums for 2020-01-01 to 2020-12-31." (N.B end is one day less than end_date.)
plt.show()
