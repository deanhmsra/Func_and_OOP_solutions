

def flatten_and_sort(lst):
    out = []
    for item in lst: 
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)

    return sorted(out)

nested = [0, -2, 5, 4, [5, 344, 3, 19], [215, 8585965]]

out = flatten_and_sort(nested)
print(out)
print(nested)

"""
How does this solution ensure data immutability?
Answer: The purpose of this code is not to change any numbers, but the order that they are in. The array within the function was what was being ordered, which can be applied 
to whatever variable with an arrary is presented.

Is this solution a pure function? Why or why not?
Answer: Yes, this is a pure function since the function has everything it needs within its function. The array (input) is only changed according to what the code dictates 
within the function, and does not utilize any outer functions. 

Is this solution a higher order function? Why or why not?
Answer: This is not a higher order function since no functions are passed as arguements. List is only there as a parameter. 

Would it have been easier to solve this problem using a different programming style?
Answer: The code is pretty direct and is limited to doing only what was requested. Other programming styles might have taken more outer help rather than being able to do it 
within its own function.

Why in particular is functional programming a helpful paradigm when solving this problem?
Answer: Some problems may not be resolved by a one-fit-all solution, and trying to do so will only make things more complicated. Functional programming is suitable for
individual unique problems and don't require it to be repeated.
"""