p = 4;
N = 128;
a = [0.1 0.2 0.3 0.4];

X = genAR(p,N,a);

Autocov = rxx(X);
%disp(Autocov);

plot(1:2*N, Autocov);

R = zeros(p+1, p +1);

for i=1:p+1
    for j=1:p+1
        R(i,j) = Autocov(int32(N*(j-i)/5 + N));
        
    end 
end

R = inv(R);

V = [1 0 0 0 0].';

C = R*V;

disp(C);

