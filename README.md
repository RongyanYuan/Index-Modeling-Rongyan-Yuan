# This is the Assessment Index Modelling by Rongyan Yuan
Dear recruiter,
Here is the index modeling assessment project, and again, thank you so much for this opportunity!

# Packages used
There are two external packages used in this project: ```pandas``` and ```numpy```, which have been already announced in the ```requirement.txt``` file.

# Algorithm
## Import and export of data
+ ```pd.read_csv``` and ```df.to_csv``` in pandas are used for reading and writing data

## Index Calculation
+ Select stocks by simply comparing their stock prices on the last day of a month, since they all have the same outstanding shares

+ Calculate total return rate of stocks selected by: R = $\frac{P_t - P_0}{P_0}$, such that R: return rate, $P_t$: current stock price, $P_0$: stock price on the first day of a month

+ Assign weight to each stock: $R_t$ = 0.5 * $R_h$ + 0.25 * $R_s$ + 0.25 * $R_t$, such that $R_h$: return rate of stock with highest cap, $R_s$ and $R_t$: return rate of stocks with second and third cap

+ Index calculation: $Index_t$ = ( $R_t$ + 1 ) * $Index_0$, such that: $Index_0$: index of the first day of the month, $Index_t$: current index level

# Result
The file "export.csv" is the result index after running ```__main__.py```.

# Contact
If there is anything you need, please contact me via my [email](mailto:adrianrongyanyun@gmail.com).
