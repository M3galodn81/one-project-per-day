# insert actual data\
while True:
    try:
        data = input("Enter the actual data (the data must be separated with commas) {ex: 123,124,237,421,125} : ")
        for x in data.split(","):
            if x in [None,""]:
                print("The data has a null element.")
                continue
            if int(x) < 0:
                print("The data has a negative value.")
                continue
        data = [int(x) for x in data.split(",")]
        break
    except ValueError:
        print("An element has a character")

# user input the (n)
while True:
    try:
        n = int(input("Enter the number of periods you wish to average: "))
        if n < 1:
            print("The number must be greater than 1")
            continue
        if n > len(data) -1:
            print("n must be lower than the number of elements in the data. ")
        break
    except ValueError:
        print("The input must be a number.")

# user input the weights
while True:
    weights = []
    try:
        for i in range(n):
            weight_input = float(input(f"Enter the weight {i+1}: "))
            if weight_input >= 1:
                print("The weight must be less than 1")
                break

            weights.append(weight_input)

        if len(weights) == n:
            if sum(weights) == 1:
                break
        
        continue

    except:
        print("The input must be a number")

# user input the alpha
while True:
    try:
        alpha = float(input("Enter the alpha for the exponential smoothing: "))
        if alpha > 1:
            print("The number must be less than 1")
            continue
        if alpha < 0:
            print("The number must be greater than 0")
            continue
        break
    except ValueError:
        print("The input must be a number.")

# simple moving average
sma_forecast_result = ["N/A" for x in range(0,n)] 
queue = []

for i,actual_data in enumerate(data):
    if i+1 <= n:
        queue.append(actual_data)
    else:
        sma_forecast_result.append(round(sum(queue)/n , 2))
        queue.pop(0)
        queue.append(actual_data)
sma_forecast_result.append(round(sum(queue)/n , 2))

# weighted moving average
wma_forecast_result = ["N/A" for x in range(0,n)]
queue = []

for i,actual_data in enumerate(data):
    if i+1 <= n:
        queue.append(actual_data)
    else:
        result = 0
        for j,queue_data in enumerate(queue):
            result += queue_data * weights[j]

        wma_forecast_result.append(round(result , 2))
        queue.pop(0)
        queue.append(actual_data)
wma_forecast_result.append(round(result , 2))

data.append("-")

# exponential smoothing
es_forecast_result = [data[0]] # uses naive forecasting for the first element
for i,actual_data in enumerate(data):
    if i == 0: continue
    t = i-1
    es_forecast_result.append(round(es_forecast_result[t] + alpha * (data[t] -es_forecast_result[t]),2))


print(f"|===== {"Result":^60} =====|")
print(f"="*74)
print(f"| Data | Simple Moving Avg | Weighted Moving Avg | Exponential Smoothing |")
for i in range(len(data)):
    print(f"| {data[i]:^4} | {sma_forecast_result[i]:^17} | {sma_forecast_result[i]:^19} | {es_forecast_result[i]:^20}  |")