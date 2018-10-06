function[phi, sig]=Estimate(X, p)

    Autocov = acovb(X);
    R = toeplitz(Autocov(1:p+1));
    R = inv(R);
    V = [1 zeros(1, p)].';
    C = R*V;
    
    phi = zeros(1,p);
    sig = (1/C(1));
    
    for i=1:p
       phi(i) = -C(i+1)*sig; 
    end

end
