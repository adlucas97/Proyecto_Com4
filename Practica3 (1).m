%Francisco Javier Hernández Azurdia - 201709158
%Adrian Antonio Lucas Guamuche - 201700600
%Laboratorio Comunicaciones 4 - Sección B
clc; clear all;
pkg load signal;

%---------------------------- Práctcia No. 3 -----------------------------------

%---------------------------- Problema No. 1 -----------------------------------
L = 35;
h = ones(L);
N = round((L-1)/2);
n = -N:N;
w1 = linspace(-pi, pi, L);
tftd = (exp(-i*w1)).^n;
figure;
subplot(2,1,1);
stem(n,h);
subplot(2,1,2);
plot(n,tftd);

%---------------------------- Problema No. 2 -----------------------------------

Fs = 1000; %Frecuencia de muestreo
T  = 1/Fs; %Periodo de muestreo
L = 1500; %Largo de la señal
t = (0:L-1)*T; %Vector de tiempo

f1 = 100;
f2 = 300;
w1 = 2*pi*f1*t;
w2 = 2*pi*f2*t;

func_2 = sin(w1) + 0.8*sin(w2);
func_2_ruido = func_2 + rand(size(func_2));
func_fft = fft(func_2_ruido);
figure;
subplot(2,1,1);
plot(func_2_ruido(1:50),'-r');
title("Señal con ruido");

P2 = abs(func_fft/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(2,1,2);
plot(f,P1,'-b');
title("Señal FFT");

%---------------------------- Problema No. 3 -----------------------------------

Fs = 1000; %Frecuencia de muestreo
T  = 1/Fs; %Periodo de muestreo
L = 100; %Largo de la señal
t = (0:L-1)*T; %Vector de tiempo

w1 = 2*pi*f1*t;

func_3_1 = sin(w1);
func_ac_1 = xcorr(func_3_1, 'coeff');
coef_1 = max(func_ac_1)
figure;
subplot(2,2,1);
stem(func_ac_1);
title(['Autocorrelación de señal sinusoidal con una señal de 100 Hz' ; 'Coeficiente máximo = ', num2str(coef_1)]);

f2 = 105;
w2 = 2*pi*f2*t;
func_3_2 = 1.25*sin(w2);
func_ac_2 = xcorr(func_3_1,func_3_2, 'coeff');
coef_2 = max(func_ac_2)
subplot(2,2,2);
stem(func_ac_2);
title(['Autocorrelación de señal sinusoidal con una señal de 200 Hz' ; 'Coeficiente máximo = ', num2str(coef_2)]);

f3 = 300;
w3 = 2*pi*f3*t;
func_3_3 = sin(w3);
func_ac_3 = xcorr(func_3_1,func_3_3, 'coeff');
coef_3 = max(func_ac_3)
subplot(2,2,3);
stem(func_ac_3);
title(['Autocorrelación de señal sinusoidal con una señal de 300 Hz' ; 'Coeficiente máximo = ', num2str(coef_3)]);

f4 = 400;
w4 = 2*pi*f4*t;
func_3_4 = sin(w4);
func_ac_4 = xcorr(func_3_1,func_3_4, 'coeff');
coef_4 = max(func_ac_4)
subplot(2,2,4);
stem(func_ac_4);
title(['Autocorrelación de señal sinusoidal con una señal de 400 Hz' ; 'Coeficiente máximo = ', num2str(coef_4)]);
