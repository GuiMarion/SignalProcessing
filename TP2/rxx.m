function[R] = rxx(X)
[sdfh,n] = size(X);

m = 2*n;

MOYENNE = 0;
for i =1:n
    MOYENNE = MOYENNE - X(i)/n;
end

X = X - MOYENNE;


TFD = fft(X, m);
IX = (1/n)*abs(TFD).^2 ; 

RXX = ifft(IX, m);

R = RXX;

end