# diablo4campainmap now xp calc
i try to create a diablo 4 map with the path the campain takes marked on it

later i said fuck that, i cant do it. 

so now that season 1 is on its way i programmed a script that listens to F1 presses and uses the existing data on xp per level to calculate how fast one is going. 

to install and run the script:
1. have python installed
2. install dependencies using
    pip install keyboard
    pip install pandas
3. in the folder you downloaded the XPCalcPerF1.py file press CTRL+L and Type powershell, in powershell write: python XPCalcPerF1.py
4. enter your current level, press enter, enter your initial XP
5. then in game press F1 when you leveled up


the result looks something like this:

PS C:\Diablo-4-XP-and-gold-per-hour> python XPCalcPerF1.py

Enter initial level: 1
Enter initial XP within level: 0
Level up! New level: 2, XP rate: 3.69 XP/s, Took you 2.711 mins, 600 XP required for next level

Level up! New level: 3, XP rate: 1062.66 XP/s, Took you 0.021 mins, 1260 XP required for next level

Level up! New level: 4, XP rate: 753.87 XP/s, Took you 0.081 mins, 3465 XP required for next level

Level up! New level: 5, XP rate: 116.79 XP/s, Took you 0.901 mins, 6325 XP required for next level

Level up! New level: 6, XP rate: 52.34 XP/s, Took you 2.731 mins, 8580 XP required for next level

Level up! New level: 7, XP rate: 87.24 XP/s, Took you 2.291 mins, 12000 XP required for next level

Level up! New level: 8, XP rate: 92.76 XP/s, Took you 2.661 mins, 14820 XP required for next level

Level up! New level: 9, XP rate: 62.13 XP/s, Took you 5.181 mins, 19305 XP required for next level

Level up! New level: 10, XP rate: 193.41 XP/s, Took you 1.961 mins, 22750 XP required for next level

Level up! New level: 11, XP rate: 85.48 XP/s, Took you 5.151 mins, 26390 XP required for next level

Level up! New level: 12, XP rate: 141.01 XP/s, Took you 3.461 mins, 29250 XP required for next level

Level up! New level: 13, XP rate: 44.43 XP/s, Took you 12.091 mins, 32240 XP required for next level

Level up! New level: 14, XP rate: 123.89 XP/s, Took you 4.761 mins, 35360 XP required for next level

Level up! New level: 15, XP rate: 17252.85 XP/s, Took you 0.041 mins, 38610 XP required for next level

Level up! New level: 16, XP rate: 64.35 XP/s, Took you 10.881 mins, 41990 XP required for next level

Level up! New level: 17, XP rate: 94.97 XP/s, Took you 7.991 mins, 45500 XP required for next level

Level up! New level: 18, XP rate: 88.57 XP/s, Took you 9.251 mins, 49140 XP required for next level

Level up! New level: 19, XP rate: 96.67 XP/s, Took you 9.121 mins, 52910 XP required for next level

Level up! New level: 20, XP rate: 123.13 XP/s, Took you 7.691 mins, 56810 XP required for next level

Level up! New level: 21, XP rate: 113.10 XP/s, Took you 8.971 mins, 60840 XP required for next level

Level up! New level: 22, XP rate: 137.86 XP/s, Took you 7.861 mins, 65000 XP required for next level

Level up! New level: 23, XP rate: 55.59 XP/s, Took you 20.771 mins, 69290 XP required for next level





