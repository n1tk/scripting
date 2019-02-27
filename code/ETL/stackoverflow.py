import pandas as pd

raw_data = {'ID':['101','101','101','102','102','102','102','103','103','103','103'],
            'Week':['08-02-2000','09-02-2000','11-02-2000','10-02-2000','09-02-2000','08-02-2000','07-02-2000','01-02-2000',
               '02-02-2000','03-02-2000','04-02-2000'],
            'Quarter':['2000q1','2000q2','2000q3','2000q4','2000q1','2000q2','2000q3','2000q4','2000q1','2000q2','2000q3'],
            'GDP in 2000 dollars':[15,15,10,15,15,5,10,10,15,20,11]}


def get_GDP_df():
    GDP_df = pd.DataFrame(raw_data).set_index('ID')
    print(GDP_df) # for reference to see how the data is indexed, printing out to the screen
    GDP_df = GDP_df.query("Quarter >= '2000q1'").reset_index(drop=True) #performing the query() + reindexing the dataframe
    GDP_df["Growth"] = (GDP_df["GDP in 2000 dollars"]
        .pct_change()
        .apply(lambda x: f"{round((x * 100), 2)}%"))
    return GDP_df

get_GDP_df()


import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2
nse3 = np.random.randn(len(t))                 # white noise 3
nse4 = np.random.randn(len(t))                 # white noise 3

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2
s3 = np.sin(2 * np.pi * 10 * t) + nse3
s4 = np.sin(2 * np.pi * 10 * t) + nse4

fig, axs = plt.subplots(2, 2)
axs[0].plot(t, s1, t, s2, t, s3, t, s4)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)



fig.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import chirp, spectrogram

np.random.seed(19680801)

# Generate some test data
x = np.random.weibull(1.25, size=1000)
y = np.random.weibull(2.25, size=1000)

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
# ax1.plot(x, y)
ax1.fill_between(x, y)
ax1.set_title('Sample subplots')
# ax2.scatter(x, y)
ax2.fill_between(x, y)
ax3.scatter(x, 2 * y ** 2 - 1, color='r')
ax4.plot(x, 2 * y ** 2 - 1, color='r')

# %%
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
l, = plt.plot([], [], 'k-o')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()