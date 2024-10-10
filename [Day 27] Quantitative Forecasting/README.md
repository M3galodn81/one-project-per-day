# Quantitative Forecasting

## Description

This python console app will forecast the demand(actual data) using quantitative forecasting methods (simple moving average, weighted moving average and exponential smoothing)

### Simple Moving Average
This method will get the average of the most recent *n* periods to forecast the next period.

$$
\frac{\displaystyle\sum_{t=1}^{n} t_i}{n}   
$$

### Weighted Moving Average
This method will get the sum of the most recent *n* periods multiplied with their corresponding weight to forecast the next period. All weights must be equal to 1

$$
\sum_{t=1}^{n} t_iw_i
$$

### Exponential Smoothing
This method will get the average of the most recent *n* periods to forecast the next period.

$$
F_{t+1} = F_t +\alpha(A_t-F_t)
$$
where $\alpha$ = smoothing factor, 
$A_t$ = actual data on the previous period, $F_t$ = forecasted period on the previous period

If the exponential smoothing has no forecast in the first period, then we will use the actual data of the first period.