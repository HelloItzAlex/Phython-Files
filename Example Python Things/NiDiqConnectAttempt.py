import nidaqmx
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

def readdaq():
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("USBDaq/ai0")
    task.start()
    value = task.read()
    task.close()
    return value

def writefiledata(t,x):
    file = open("tempdata.csv","a")
    time = str(t)
    value = str(x)
    file.write(time + "\t" + value)
    file.write("\n")
    file.close()

Ts = 1
N = 100
k = 1
x_len = N
Vmin = 0; Vmax = 10
y_range = [Vmin,Vmax]
data = []

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = list(range(0,N))
ys = [0] * x_len
ax.set_ylim(y_range)

line, = ax.plot(xs,ys)

plt.title("Voltage ")
plt.xlabel("time")
plt.ylabel("Voltage")
plt.grid()

def logging(i,ys):
    value = readdaq()
    print("V = ", value)
    data.append(value)
    time.sleep(Ts)
    global k 
    k = k + 1 
    writefiledata(k*Ts, value)

    ys.append(value)

    ys = ys[-x_len:]

    line.set_ydata(ys)
    return line,
ani = animation.FuncAnimation(fig,
                              logging,
                              fargs=(ys,),
                              interval = 100,
                              blit = True)

plt.show()