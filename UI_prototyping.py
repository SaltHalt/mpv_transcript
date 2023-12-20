import os

subtitle_list = ["sometimes called a wall clock. And this is meant to be reflecting the actual normal time",
"that we use and measure events in. On the other hand, we have logical clocks that are",
"based just upon events. So, in a distributed system that would often be events like messages",
"being sent. So, an individual node may have a logical clock that ticks up each time a",
"message is sent or a message is received. So, each time something significant occurs",
"in the interaction between that node and the rest of the system, it's logical clock increments.",
"And in other settings we see different uses of logical clocks. It's common in implementing",
"a programming language runtime system to use the actual amount of memory allocation that's",
"been used as a clock. You sometimes hear this called an allocation clock and people",
"looking at the design of garbage collectors kind of look at its performance measured over",
"an allocation based clock. That's just another form of logical clock. I should emphasize",
"the use of the word clock here is a bit different to the use in digital electronics. Now, here",
"we're talking about clocks as a source of timestamps, whether that's actual time values",
"in seconds or counts of events. We're not talking about them in the digital electronic",
"sense of an oscillator generating a series of pulses at a regular interval. But if we're",
"building a physical clock, then of course we do underlying that need some time source,",
"some way of mapping from that kind of digital electronics view of clocks to a value in seconds.",
"And typically that would be built over a quartz oscillator. So, with a crystal that's trimmed",
"to a size so that it resonates at a frequency that can be mapped into time. And then counting",
"the number of cycles coming from that in order to get a measure of elapsed time. And",
"the issue here is that the quartz oscillator is not going to be perfect. So, it's relying",
"on this underlying physical process and mechanical tuning of the crystals to target a given",
"frequency. And that frequency will depend on the quality of that tuning process and",
"it's going to vary based on the environment in which the oscillator is running. So, the",
"example here is looking at the accuracy of the frequency over temperature. And we typically",
"have the oscillator tuned to run as close as we can to the target frequency at a range",
"around room temperature. And then it will degrade increasingly rapidly as we move away",
"from that. So, if we measure the performance in terms of parts per million accuracy, then"]


output = ""
WINDOW_WIDTH = os.get_terminal_size().columns
TIMESTAMP_WIDTH = 9 #0:00:00| 
# os.system("COLOR F0")
import colorama
colorama.init()
import termcolor
from colored import stylize, fore, back

for j in range(0, len(subtitle_list)):
    sub_text = subtitle_list[j]
    line     = f"0:12:41| {sub_text}"
    format_current = lambda text : stylize(text.ljust(WINDOW_WIDTH, " "), fore('grey_3')+back(255))
    format_other = lambda text : stylize(text.ljust(WINDOW_WIDTH, " "), fore('grey_3')+back('white'))
    format = format_current if j==12 else format_other
    # inner-lines = textwrap.wrap(line, width = WINDOW_WIDTH)
    output += format(line) + "\n"

print(output[:-1], end = "")

