def fibonacci(n)
    if n <= 1
      puts "Base case: n is #{n}"
      return n
    else
      result = fibonacci(n-1) + fibonacci(n-2)
      puts "Recursive call for n-1 and n-2: fibonacci(#{n-1}) + fibonacci(#{n-2}) = #{result}"
      return result
    end
  end
  
  puts fibonacci(10) # Output: 55
