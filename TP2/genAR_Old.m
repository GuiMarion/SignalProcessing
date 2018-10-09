function[R] = genAR(p, N, a)

    R = zeros(1, N);
    
    sigma = 1;
    
    W =  sigma.*randn(1,N);
    for n=1:N
       
        for i=1:min(n-1,p)
            R(n) = R(n) + a(i)*R(n-i);
            
        end
        
        R(n) = R(n) + W(n);
        
    end

end