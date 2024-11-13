import threading
import random
import time 

def selection_sort(arr):
    start_time = time.time()
    n = len(arr)

    for i in range(n):
        min_element = arr[i]
        min_index = i
        for j in range(i+1,n):
            if min_element > arr[j]:
                min_element = arr[j]
                min_index = j

        arr[i],arr[min_index] = arr[min_index] ,arr[i]
    
    end_time = time.time()
    print(f"Selection sort completed in {end_time - start_time:.2f} seconds.")
    return (arr)

def bubble_sort(arr):
    start_time = time.time()
    n = len(arr)
    
    unsorted = True
    while unsorted:
        swap_count = 0
        for i in range(n):
            if i+1 == n:
                break
            
            temp = 0
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap_count += 1
        
        if swap_count > 0:
            continue
        else:
            break

    end_time = time.time()
    print(f"Bubble sort completed in {end_time - start_time:.2f} seconds.")
    return (arr)

random.seed(345)
arr = [random.randint(1,1000) for _ in range(5000)]
arr_copy = arr.copy() 
arr_copy2 = arr.copy() 

thread1 = threading.Thread(target=bubble_sort, args=(arr_copy,))
thread2 = threading.Thread(target=selection_sort, args=(arr_copy2,))

start_time = time.time()

thread1.start()
thread2.start()

while thread1.is_alive() or thread2.is_alive():
    if thread1.is_alive():
        print("Bubble Sorting is still ongoing...")
    if thread2.is_alive():
        print("Selection Sorting is still ongoing...")
    time.sleep(1)

thread1.join()
thread2.join()
end_time = time.time()

print("Both threads have finished execution.")
print(f"Total time taken: {end_time - start_time:.2f} seconds")