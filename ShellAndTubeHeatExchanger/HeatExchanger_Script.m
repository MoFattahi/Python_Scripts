clc; clear data; clear;
%% Heat_Exchanger Project
% Student: Mohammad Fattahi
% Winter 2021

%% First Part: Detemining the Exchanger Type
% first, we should determine wich type of heat exchanger we want to design.

disp('Select the Exchanger-Type from the list bellow: ');
disp('1.Fixed Head      2.Kettle Reboiler      3.U-Tube');
a = input(': ');
while 1>0
    if a==1
        break;
    end
    if a==2
        break;
    end
    if a==3
        break;
    end
    a = input('ERROR! Please enter 1, 2, or 3: ');
end
%% Second Part: Selecting Cold & Hot Fluids Type

disp('Select the cold fluid from the list bellow (tube-side): ');
disp('1.Treatd Water          2.Untreated Water          3.Sea Water          4.Air');
b = input(': ');
% determining the constant due to the water kind.
while 1>0
    if b==1
        Cpc = 4182;
        Miu_T = 0.001;
        K_for_t = 0.6;
        HDI = 0.001;
        break;
    end
    if b==2
        Cpc = 4182;
        Miu_T = 0.001;
        K_for_t = 0.6;
        HDI = 0.003;
        break;
    end
    if b==3
        Cpc = 3930;
        Miu_T = 0.001;
        K_for_t = 0.6;
        HDI = 0.0005;
        break;
    end
    if b==4
        Cpc = 1003.5;
        Miu_T = 0.000018;
        K_for_t = 0.025;
        HDI = 0.0000001;
        break;
    end
    b = input('ERROR! Chosen type is invalid. Please enter a valid number: ');
end
disp('Select the hot fluid (shell-side): ');
disp('1. Treated Water                2.Water Vapor');
c = input(': ');
while 1>0
    if c==1
        Cph = 4182;
        miu_s = 0.001;
        K_s = 0.6;
        HDO = 0.001;
        break;
    end
    if c==2
        Cph = 1996;
        miu_s = 0.00001827;
        K_s = 0.2;
        HDO = 0.0000001;
        break;
    end
    c = input('ERROR! Please enter a valid number: ');
end
%% Pressure
P = input('Enter the pressure in kPag: ');
while 1>0
    if P>=700 && P<2100
        break;
    end
    if P>=2100 && P<4200
        break;
    end
    if P>=4200 && P<6200
        break;
    end
    P = input('ERROR! The Valid range for pressure is between 700 and 6200 kPag. Enter a pressure value in the given range: ');
end
%% Selecting Material
disp('Select one of these materials: ');
disp('1.SS304                        2.Incoloy 825              3.Nickel 200');
disp('4.SS347                        5.Inconel 600              6.Monel 400');
disp('7.SS316                        8.Titanium                 9.Hastelloy');
m = input(':');
while 1>0

    if m==1
        kw = 16.2;
        break;
    end
    if m==2
        kw = 12.4;
        break;
    end
    if m==3
        kw = 70.2;
        break;
    end
    if m==4
        kw = 16.3;
        break;
    end
    if m==5
        kw = 14.9;
        break;
    end
    if m==6
        kw = 21.8;
        break;
    end
    if m==7
        kw = 16.2;
        break;
    end
    if m==8
        kw = 16;
        break;
    end
    if m==9
        kw = 6.1;
        break;
    end
    m = input('ERROR! Please enter a valid number (1 to 9): ');
end
%% Inputs
MC = input('Mass flow rate in tube side (cold flow) (kg/s) = '); 
MH = input('Mass flow rate in shell side (hot flow) (kg/s) = ');
Temp_Cold_1 = input('Inlet temp. tube side (cold flow) = ');
Temp_Hot_1 = input('Inlet temp. shell side (hot flow) = ');
z = input('which side temp. do you want to enter? 1.tube(cold)    or    2.shell(hot) side? ');
while 1>0
    if z==1
        Temp_Cold_2 = input('Outlet temp tube side (cold flow) = ');
        Temp_Hot_2 = Temp_Hot_1 - MC*Cpc*(Temp_Cold_2 - Temp_Cold_1)/(MH*Cph);
        break;
    end
    if z==2
        Temp_Hot_2 = input('Outlet temp shell side (hot flow) = ');
        Temp_Cold_2 = MH*Cph*(Temp_Hot_1 - Temp_Hot_2)/(MC*Cpc) + Temp_Cold_1;
        break;
    end
    z = input('ERROR! Accurate Numbers = {1,2}. Please reselect the outlet Temperature Type: ');
end
Qduty = MC*Cpc*(Temp_Cold_2 - Temp_Cold_1);
w = input('Your flow is:   1.Co-current                 2.Counter-current: ');
while 1>0
    if w==1
        LMTD = ( (Temp_Hot_1 - Temp_Cold_1) - (Temp_Hot_2 - Temp_Cold_2) )/( log( (Temp_Hot_1 - Temp_Cold_1) / (Temp_Hot_2 - Temp_Cold_2) ) );
        break;
    end
    if w==2
        LMTD = ( (Temp_Hot_1 - Temp_Cold_2) - (Temp_Hot_2 - Temp_Cold_1) )/( log( (Temp_Hot_1 - Temp_Cold_2) / (Temp_Hot_2 - Temp_Cold_1) ) );
        break;
    end
    w = input('ERROR! Accurate Numbers = {1,2}. Please reselect the flow Type: ');
end
while 1>0
    Nu_pass = input('Enter the number of passes: ');
    if Nu_pass==1 || Nu_pass==2 || Nu_pass==4 || Nu_pass==6 || Nu_pass==8
        break;
    end
    Nu_pass = input('ERROR! Number of passes is an even Number. Please reenter the Number of Passes: ');
end
%% Solving
R = (Temp_Hot_1 - Temp_Hot_2) / (Temp_Cold_2 - Temp_Cold_1);
if R==1
    R = 0.9999;
end
S = (Temp_Cold_2 - Temp_Cold_1) / (Temp_Hot_1 - Temp_Cold_1);
Ft = ( ((R^2 +1)^(0.5)) * log( (1-S)/(1-R*S) ) ) / ( (R-1) * log( (2 - S*(R + 1 - (R^2 + 1)^(0.5))) / (2 - S*(R + 1 + (R^2 + 1)^(0.5))) ) );
DTm = Ft*LMTD;
do = input('Please enter the out diameter of tubes (mm): ');
pt = 1.25*do;
thickness = input('Please enter the thickness of tubes (mm): ');
while thickness>=do
    thickness = input('ERROR! Thickness must be lower than the out diameter: ');
end
di = do - (2*thickness);
L = input('Please enter the Length of the heat exchanger(mm): ');
Tube_Pattern = input('What is the tube pattern?    1.Triangular            2.Square: ');
while 1>0
    if Tube_Pattern==1
        de = 1.1*(pt^2 - 0.917*(do^2))/do;
        if Nu_pass==1
            K1 = 0.319;
            n1 = 2.142;
        end
        if Nu_pass==2
            K1 = 0.249;
            n1 = 2.207;
        end
        if Nu_pass==4
            K1 = 0.175;
            n1 = 2.285;
        end
        if Nu_pass==6
            K1 = 0.0743;
            n1 = 2.499;
        end
        if Nu_pass==8
            K1 = 0.0365;
            n1 = 2.675;
        end
        break;
    end

    if Tube_Pattern==2
        de = 1.27*(pt^2 - 0.785*(do^2))/do;
        if Nu_pass==1
            K1 = 0.215;
            n1 = 2.207;
        end
        if Nu_pass==2
            K1 = 0.156;
            n1 = 2.291;
        end
        if Nu_pass==4
            K1 = 0.158;
            n1 = 2.263;
        end
        if Nu_pass==6
            K1 = 0.0402;
            n1 = 2.617;
        end
        if Nu_pass==8
            K1 = 0.0331;
            n1 = 2.643;
        end
        break;
    end

    Tube_Pattern = input('ERROR! Please enter a number between 1 and 2: ');
end

U = 800;

while 1>0
    A = Qduty / (U*DTm);
    Nt =  fix(A / (pi*(do*0.001)*(L*0.001))) ;
    Db = do*( (Nt/K1)^(1/n1) );
    BDC = 8 + 10*(Db*0.001);
    Ds = Db + BDC;
    Bs = 0.4*Ds;
    As = ((pt - do)*0.001)*(Ds*0.001)*(Bs*0.001)/(pt*0.001);
    Gs = MH/As;
    Re_s = Gs*(de*0.001)/miu_s;
    Pr_s = miu_s*Cph/K_s;
    Ntpp = Nt/Nu_pass;
    At = Ntpp*pi*((di*0.001)^2)*0.25;
    Gm = MC/At;
    Re_t = Gm*(di*0.001)/Miu_T;
    Pr_t = Miu_T*Cpc/K_for_t;
    if Re_t<2100
        hi = 1.86*(K_for_t/(di*0.001))*( (Re_t*Pr_t)^0.33 )*( (di/L)^0.33 );
    end
    if Re_t>=2100
        hi = 0.023*(K_for_t/(di*0.001))*(Re_t^0.8)*(Pr_t^0.33)*(1 + (di/L)^0.7);
    end
    if Re_s<2100
        ho = 1.86*(K_s/(di*0.001))*( (Re_s*Pr_s)^0.33 )*( (de/L)^0.33 );
    end
    if Re_s>=2100
        ho = 0.023*(K_s/(di*0.001))*(Re_s^0.8)*(Pr_s^0.33)*(1 + (de/L)^0.7);
    end
    Ai = Nt*pi*(di*0.001)*(L*0.001);
    Ui = 1/( (1/hi) + (1/HDI) + ( di*log(do/di)/(2*kw) ) + (di/(do*HDO)) + (di/(do*ho)) );
    u = Ui*Ai*(10^8)/A;
    if abs(U - u)<1
        break;
    end
    U = u;
end

if a==1
    FD = exp(-0.9003 + 0.0906*log(A)); 
end
if a==2
    FD = 1.35;
end
if a==3
    FD = exp(-0.7844 + 0.083*log(A));
end

if m==1
    FM = 1.4144 + 0.23296*log(A);
end
if m==2
    FM = 1.1991 + 0.15984*log(A);
end
if m==3
    FM = 1.1388 + 0.22186*log(A);
end
if m==4
    FM = 2.9553 + 0.30859*log(A);
end
if m==5
    FM = 2.3296 + 0.433377*log(A);
end
if m==6
    FM = 2.4103 + 0.50764*log(A);
end
if m==7
    FM = 2.3665 + 0.49706*log(A);
end
if m==8
    FM = 2.5617 + 0.42913*log(A);
end
if m==9
    FM = 3.7614 + 1.51774*log(A);

end

if P>=700 && P<2100
    FP = 0.8955 + 0.04981*log(A);
end
if P>=2100 && P<4200
    FP = 1.2002 + 0.0714*log(A);
end
if P>=4200 && P<6200
    FP = 1.4272 + 0.12088*log(A);
end

CB = exp(8.202 + 0.01506*log(A) + 0.06811*log(A)*log(A));
final_cost = CB*FP*FD*FM;
%% Displaying
disp('A:');
disp(A);
disp('The overall heat transfer coefficient: ');
disp(u);
disp('Shell diameter: ');
disp(Ds);
disp('The final cost: ');
disp(final_cost);
disp('Number of tubes: ');
disp(Nt);