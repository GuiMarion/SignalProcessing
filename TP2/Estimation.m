p = 4;
N = 1000000;
NbRepet = 1000;
mean_squaredError = 0;
for poi=1:NbRepet
    [X, phi] = genAR(p,N);

    Autocov = acovb(X);
    %disp(Autocov);

    R = toeplitz(Autocov(1:p+1));

    R = inv(R);

    V = [1 zeros(1, p)].';

    C = R*V;

    squaredError = 0;

    for i=1:p
        squaredError = squaredError + (phi(i) + C(i+1)/C(1)); 
    end

    mean_squaredError = mean_squaredError + squaredError/NbRepet;
    
end

disp(mean_squaredError/p)
