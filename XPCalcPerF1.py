import keyboard
import time
from datetime import datetime
import pandas as pd

# Define experience per level (shortened for brevity)
xp_per_level = {
0:  0, 
1	:600,
2	:1860,
3	:5325,
4	:11650,
5	:20230,
6	:	32230,
7	:	47050,
8	:	66355,
9	:	89105,
10	:	115495,
11	:	144745,
12	:	176985,
13	:	212345,
14	:	250955,
15	:	292945,
16	:	338445,
17	:	387585,
18	:	440495,
19	:	497305,
20	:	558145,
21	:	623145,
22	:	692435,
23	:	766145,
24	:	844405,
25	:	927345,
26	:	1021845,
27	:	1121665,
28	:1226945,
29	:1337825,
30	:1462775,
31	:1594025,
32	:1731725,
33	:1876025,
34	:2027075,
35	:2185025,
36	:2350025,
37	:2522225,
38	:2701775,
39	:2888825,
40	:3087950,
41	:3313550,
42	:3567615,
43	:3852195,
44	:4169400,
45	:4574200,
46	:5021579,
47	:5514170,
48	:6101676,
49	:6791400,
50	:	8362530,
51	:	10028880,
52	:	11792520,
53	:	13655520,
54	:	15619950,
55	:	17687880,
56	:	19861380,
57	:	22142520,
58	:	24533370,
59	:	27036000,
60	:	30088560,
61	:	33276360,
62	:	36601816,
63	:	40067342,
64	:	43675352,
65	:	47428262,
66	:	51328488,
67	:	55378444,
68	:	59580544,
69	:	63937204,
70	:	71736274,
71	:	79871374,
72	:	88348024,
73	:	97171744,
74	:	106348054,
75	:	115882474,
76	:	125780524,
77	:	136047724,
78	:	146689594,
79	:	157711654,
80	:	169187734,
81	:	181124734,
82	:	193529554,
83	:	206409094,
84	:	219770254,
85	:	233619934,
86	:	247965034,
87	:	262812454,
88	:	278169094,
89	:	294041854,
90	:	310512844,
91	:	327590344,
92	:	345282634,
93	:	363597994,
94	:	382544704,
95	:	402131044,
96	:	422365294,
97	:	443255734,
98	:	464810644,
99	:	487038304,
}


# Initialize data storage
df = pd.DataFrame(columns=['level', 'timestamp', 'xp_rate'])

# Ask user for initial level and XP
initial_level = int(input('Enter initial level: '))
initial_xp = int(input('Enter initial XP within level: '))

prev_level = initial_level
prev_xp = initial_xp
prev_time = datetime.now()

def level_up(e):
    global prev_level, prev_xp, prev_time, df

    # Calculate elapsed time and XP rate
    now = datetime.now()
    elapsed_time = (now - prev_time).total_seconds()
    xpReqForCurrentLevel = xp_per_level[prev_level]- xp_per_level[prev_level-1]
    xp_gained = xpReqForCurrentLevel - prev_xp
    xp_rate = xp_gained / elapsed_time
    xp_ratePerMin = xp_rate / 60

    print(f'Level up! New level: {prev_level+1}, XP rate: {xp_rate:.2f} XP/s, Took you {elapsed_time/60:.2f}1 mins, {xpReqForCurrentLevel} XP required for next level')

    # Store data
    df = df.append({'level': prev_level+1, 'timestamp': now, 'xp_rate': xp_rate}, ignore_index=True)
    df.to_csv('dataframe.csv', sep=',', index=False, encoding='utf-8')

    # Reset for next level
    prev_level += 1
    prev_xp = 0
    prev_time = now

# Listen for F1 keypress
keyboard.on_press_key('f1', level_up)

# Keep the script running
while True:
    time.sleep(1)
