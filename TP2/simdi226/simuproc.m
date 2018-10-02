% simuproc.m                                                %
% r�alisation d'un processus, moyennes, covariances,        %
% on realise asymptotiquement l'esperance mathematique      %
% moyennant sur les realisations, pour un grand nombre      %
% de tirages                                                 %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;close all;

Nit = 10000; % nbr de trajectoires
H = 10; % nbre de points de la covariance
n = 2*H-1; % nbre de points du processus
sigma = 0.5; % Variance du bruit blanc
a = 0.5; % Coefficient du filtre
b = 0.5; % Amplitude du cos
nu0 = 0.3; % compris entre 0 et 0.5
% init
EX = zeros(1,n);
gamma = zeros(1,2*H-1);tc = -(H-1):(H-1);

t = 0:n-1;

% gestion de l'arret du programme
cont =1;
hstop = uicontrol(gcf,'style','pushbutton','string','stop');
set(hstop,'position',[0 0 40 30],'backgroundcolor','r')
set(hstop,'callback','cont=0;');

for k=1:Nit
    % ki�me tirage du processus; 
    % partie �  modifier selon le processus
    
    %X = randn(1,n); % ex du bruit blanc
    %X = sigma.*randn(1,n); % bruit de variance sigma**2
    
    %W = sigma.*randn(1,n); % bruit de variance sigma**2

    %X = zeros(1, n);
    %X(1) = W(1);
    
    % Application du filtre
    %for i=2:n
        %X(i) = W(i) + a*X(i-1);
    %end
        
    W = sigma.*randn(1,n); % bruit de variance sigma**2
    X = zeros(1,n);
    
    for i=1:n
        delta = rand(1)*2*pi;
        X(i) = b*cos(2*pi*nu0*i+ delta) + W(i);
    end
    
    
    % calcul des moyennes
    EX = EX+X;
     
    % calcul des covariances
    for h=0:(H-1) % calcul pour d�calage h >= 0
       XX = X(1+h:h+n-H).*conj(X(1:n-H)); % produit X(t+h)X(t)* 
       EXX = sum(XX)/(n-H);    % tient compte de la stationarit� pour
                                % estimer gamma(h) 
       gamma(h+H) = gamma(h+H)+EXX; % gamma(0) = gamma(H)
       gamma(H-h) = conj(gamma(h+H)); % tient comte de la sym�trie hermitienne
    end

    % mise a jour de l'affichage
    subplot(211)
    pointer = plot(t,EX / k,'o');
    title('moyennes E(X(t))');
    ylim([-1,1])
    grid;
    subplot(212)
    pointer2 = plot(tc,gamma / k,'o');
    axis([-H,H,-1.5,1.5])
    title('covariances gamma(h)')
    xlabel('h')
    grid

    pause(.001); % pour provoquer l'affichage
    
    if ~cont,break,end;
end

