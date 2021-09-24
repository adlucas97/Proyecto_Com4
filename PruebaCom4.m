clc; clear all;
pkg load signal;

#----------------------- Correlación Cruzada de Muestras -----------------------

#Muestras "Primera"
x1 = [37,247,301,266,233,198,299,469,514,605,597,671,540,165,377,370,181,147,47];
x2 = [93,263,86,213,250,338,284,145,168,12,474,491,468,588,535,509,243,181,258,28,77,36];
x3 = [184,40,209,366,388,231,140,106,61,450,474,434,472,400,270,28,56,169,63,42];
#Muestras"Segunda"
y1 = [45,187,219,149,59,225,458,234,179,233,80,161,271,223,364,279,274,206,23];
y2 = [6,1,4,119,159,68,97,160,65,37,151,162,8,221,335,234,158,160,61];
y3 = [39,183,228,142,1,60,178,14,95,263,388,314,90,67,430,380,287,284,63];


#Correlación cruzada x1 & x2
corr_x1_x2 = xcorr(x1(1:19),x2(1:19), 'coeff');
coef_x1_x2 = max(corr_x1_x2);

#Correlación cruzada x1 & x3
corr_x1_x3 = xcorr(x1(1:19),x3(1:19), 'coeff');
coef_x1_x3 = max(corr_x1_x3)

#Correlación cruzada x2 & x3
corr_x2_x3 = xcorr(x2(1:19),x3(1:19), 'coeff');
coef_x2_x3 = max(corr_x2_x3)

#Correlación cruzada y1 & y2
corr_y1_y2 = xcorr(y1(1:19),y2(1:19), 'coeff');
coef_y1_y2 = max(corr_y1_y2)

#Correlación cruzada y1 & y3
corr_y1_y3 = xcorr(y1(1:19),y3(1:19), 'coeff');
coef_y1_y3 = max(corr_y1_y3)

#Correlación cruzada y2 & y3
corr_y2_y3 = xcorr(y2(1:19),y3(1:19), 'coeff');
coef_y2_y3 = max(corr_y2_y3)

#Correlación cruzada x1 & y1
corr_x1_y1 = xcorr(x1(1:19),y1(1:19), 'coeff');
coef_x1_y1 = max(corr_x1_y1)

#Correlación cruzada x2 & y2
corr_x2_y2 = xcorr(x2(1:19),y2(1:19), 'coeff');
coef_x2_y2 = max(corr_x2_y2)

#Correlación cruzada x3 & y3
corr_x3_y3 = xcorr(x3(1:19),y3(1:19), 'coeff');
coef_x3_y3 = max(corr_x3_y3)

#------------------------Transformada Rápida de Muestras -----------------------

Fs = 100; %Frecuencia de muestreo
T  = 1/Fs; %Periodo de muestreo
L = 19; %Largo de la señal
t = (0:L-1)*T; %Vector de tiempo

#Comparación de las señales x1, x2 & x3
x1_fft = fft(x1);
P2 = abs(x1_fft/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
figure
subplot(3,1,1);
plot(f,P1,'-r');
title("Transformada rápida de Fourier Prueba 1 - Primera");
grid on

x2_fft = fft(x2);
P2 = abs(x2_fft/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(3,1,2);
plot(f,P1,'-b');
title("Transformada rápida de Fourier Prueba 2 - Primera");
grid on

x3_fft = fft(x3);
P2 = abs(x3_fft/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(3,1,3);
plot(f,P1,'-g');
title("Transformada rápida de Fourier Prueba 3 - Primera");
grid on

#Comparación de las señales y1, y2 & y3
y1_fft = fft(y1);
P2 = abs(y1_fft/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
figure
subplot(3,1,1);
plot(f,P1,'-r');
title("Transformada rápida de Fourier Prueba 1 - Segunda");
grid on

y2_fft = fft(y2);
P2 = abs(y2_fft/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(3,1,2);
plot(f,P1,'-b');
title("Transformada rápida de Fourier Prueba 2 - Segunda");
grid on

y3_fft = fft(y3);
P2 = abs(y3_fft/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(3,1,3)
plot(f,P1,'-g');
title("Transformada rápida de Fourier Prueba 3 - Sagunda");
grid on