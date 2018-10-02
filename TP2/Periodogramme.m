sigma =0.1;
n = 1024;
m = 2*n;
a = 0.5;
b = 0.5;
nu0 = 0.3;
nbRepet = 100000;

Variances = zeros(1, 11);
for poi=0:nbRepet
    for n=[2 4 8 16 32 64 128 256 512 1024 2048]
        X = sigma.*randn(1,n); % bruit de variance sigma**2

        MOYENNE = 0;
        for i =1:n
            MOYENNE = MOYENNE + X(i)/n;
        end

        % Question 2
        TFD = fft(X, m);
        IX = (1/n)*abs(TFD).^2 ; 

        Variance = var(IX);

        Variances(log2(n)) = Variances(log2(n)) + Variance/nbRepet;

        % Question 3

        RXX = ifft(IX, m);


        %plot(1:m, rxx(X));

    end
end
plot(1:11,Variances)
