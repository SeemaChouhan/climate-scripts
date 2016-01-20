import numpy
from matplotlib import pyplot
import seaborn
import subprocess
seaborn.set_style("white")

def make_video(x, y, fps=15):
  for j in range(len(x)):
    pyplot.figure(figsize=(20,8))
    pyplot.plot(x[:j],y[:j])
    pyplot.xlim([min(x), max(x)])
    pyplot.ylim([min(y), max(y)])
    pyplot.savefig("figures/timeseries_%02i.jpeg" % j)
    pyplot.close()

  vidargs = ["ffmpeg", "-framerate", " %i" % fps, 
      "-i",  "figures/timeseries_%02d.jpeg", "-c:v", "libx264", "-r",  "30", 
      "-pix_fmt", "yuv420p", "timeseries.mp4"]
  subprocess.check_call(vidargs)

if __name__ == "__main__":
  n = 100
  m = 0.5 
  rand = numpy.random.normal(0,2, size=n)
  x = numpy.arange(n)
  y = m*x + rand
  make_video(x, y)
