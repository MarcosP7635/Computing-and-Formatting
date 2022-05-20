#print the nth fibonacci number
function nth_fib(n)
    if n == 0
        return 0
    elseif n == 1
        return 1
    else
        return nth_fib(n-1) + nth_fib(n-2)
    end
end

#time how fast a function runs
function time_function(f, input)
    start = time()
    #concatenate f and input as strings to print the function name, input, and output
    string_output = (String(Symbol(f))*'('* String(Symbol(input))*") = "*String(Symbol(f(input))))
    stop = time()
    string_output *= " ran in "*String(Symbol(stop-start))*" seconds"
    return string_output
end

print(time_function(nth_fib, 100))
