import streamlit as st
import time # used for time.sleep(seconds) to pause between countdown updates

st.title("Pomodoro Timer")

work_time = st.slider("Work Time (minutes)", 1, 90, 25)   #start, stop, default
break_time = st.slider("Break Time (minutes)", 1, 30, 5)

def timer(work_time, break_time):
    # Convert minutes -> seconds, sleep() runs in seconds.
    work_in_sec = work_time * 60
    break_in_sec = break_time * 60  

    #dyanmic container i.e. placeholder to update repeatedly so that break and work gets updated in the same space
    #without making new line
    work_placeholder = st.empty() 
    break_placeholder = st.empty()

    work_placeholder
    for i in range(0, work_in_sec + 1):
        time.sleep(1) #pausing execution for 1 second before updating time left (will change..)
        work_placeholder.write(f"{work_in_sec - i} seconds left!")
        if (work_in_sec - i) == 0:
            work_placeholder.write(f"Study time is over!, take a break!")

    break_placeholder
    for i in range(0, break_in_sec + 1):
        time.sleep(1) 
        break_placeholder.write(f"{break_in_sec - i} seconds left!")
        if (break_in_sec - i) == 0:
            break_placeholder.write(f"Break time is over!, back to work!")


if st.button("Start Timer!"):
    timer(work_time, break_time)

# version blocks while counting down, streamlit can't take inputs mid execution.
# use session_state, rerun to implement stop and pause

























