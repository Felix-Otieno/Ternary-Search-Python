""" 
Defined a function to find the position of the element in the ternary search and passed parameters inside it respectively.
Parameters: low, the left end point of the sorted array(first index)
            high, the right end point of the sorted array(last index)
            sortArray, the list of sorted element
            element, the vlaue to be search thus find its position in the sorted array
"""
def ternary_search(low, high, sortArray, element):

    # Element not present in the search range
    if low > high:
        return "Element not found" 
    
    # Calculate the 2 middle point to divide the sorted array into three parts
    middle1 = low + (high - low) // 3 
    middle2 = high - (high - low) // 3

    # Check if element is at any middle point
    if sortArray[middle1] == element:
        return f"Element found at index {middle1}"
    if sortArray[middle2] == element:
        return f"Element found at index {middle2}"
    
    # Check in which position is the element found
    # Element is in the low third of the sorted array
    if element < sortArray[middle1]: 
        return ternary_search(low, middle1 - 1, sortArray, element)
    
    # Element is in the high third of the sorted array
    elif element > sortArray[middle2]: 
        return ternary_search(middle2 + 1, high, sortArray, element)
    
    # Element in the middle third of the sorted array
    else: 
        return ternary_search(middle1 + 1, middle2 - 1, sortArray, element)

    # Define variable to store the sorted array
sortArray = [10, 20, 40, 60, 70, 90, 120, 150] 
 
    # Output the result of the position of the element
print(ternary_search(0, len(sortArray) - 1, sortArray, 60)) 
