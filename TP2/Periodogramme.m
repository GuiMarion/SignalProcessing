sigma =0.1;
n = 1024;
m = 2*n;
a = 0.5;
b = 0.5;
nu0 = 0.3;

W = sigma.*randn(1,n); % bruit de variance sigma**2
X = zeros(1,n);

for i=1:n
    delta = rand(1)*2*pi;
    X(i) = b*cos(2*pi*nu0*i+ delta) + W(i);
end


MOYENNE = 0;
for i =1:n
    MOYENNE = MOYENNE + X(i)/n;
end

% Question 2
TFD = fft(X, m);
IX = (1/n)*abs(TFD).^2 ; 

%plot(1:m,IX)


% Question 3

RXX = ifft(IX, m);


plot(1:m, rxx(X));


