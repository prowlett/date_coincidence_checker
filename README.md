# date_coincidence_checker

## Description

Looks at all days over a year starting at `start_date_str` and sums the digits of the day, month and two-digit year. Reports:

- the digit sum for each day in the year;
- the number of days in the year matching each digit sum;
- a bar chart of non-zero digit sums against number of days in the year matching this digit sum

Example: 2020-10-31 sums as 20-10-31 giving 2+0+1+0+3+1=7.

Note: the maximum value for the digit sum of a two-digit year is 99. The maximum value for the digit sum of a day is 29. The maximum value for the digit sum of a month is September, 9. Therefore, the maximum digit sum in this form is 9+9+0+9+2+9=38.

## Background

Inspired by [a tweet by @aa42john](https://twitter.com/aa42john/status/1324405199419674624), which observes that "Sean Connery died on 31/10/20. If you add up all the numbers in the date = 007" and asks "How many other dates this year add up to 007? What about in 2021?"

There are 23 dates with digit sum 7 in 2020 and 18 dates with digit sum 7 in 2021. Charts for all non-zero digit sums in 2020 and 2021 are given as images in this repository.
