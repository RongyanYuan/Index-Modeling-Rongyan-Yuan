# This is the assessment Index Modelling by Rongyan Yuan
Dear recuriter,
Here is the index modeling assessment project, and again, thank you so much for this opportunity!

# Packages used
There are two external packages used in this project: pandas and numpy, which have been already announced in the requirement.txt file.

# Algorithm
## Calculation
+ Select stocks by simply comparing their stock prices on the last day of a month, since they all have the same outstanding shares
+ Calculate total return rate of stocks seleced by: 
<center>R = ${$P_t$ - $P_0$}\over{P_0}$, such that R: return rate, $P_t$: current stock price, $P_0$: stock price on the first day of a month</center>
+ Assign weight to each stock:
<center> $R_toal$ = 0.5*$R_h$ + 0.25*$R_s$ + 0.25*$R_t$, such that $R_h$: return rate of stock with highest cap </center>
+ Index calculation:
<center> $Index_t$ = ($R_toal$ + 1)*$Index_i0$, such that  $Index_i0$: index of the first day of the month</center>

# Result
The file "export.csv" is the result index after running _main_.py.

# Contact
If there is anything you need, please contact me via my email: adrianrongyanyun@gmail.com.
