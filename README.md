# StopWatch

This is my first foray into GUI programming since undergrad. I needed a simple, straightforward stop watch utility for timing my tasks, as well as a reason to finally do what I've wanted to do for a long time: GUI programming. 

The application is the simplest possible thing: three buttons with a stopwatch functionality. All written in Python. It was so simple that a Model-Control-View breakdown would've been overkill. Overtime, I hope to add to it but for now, here's a simple code, doing a simple thing!

## Code Requirements
See `requirements.txt` for the list of required packages. I used a virtual environment of `Python3.9.5`.

## Conversion to an application
I used `pyinstaller` in order to convert the python code into an app and avoid having to call it from a command line everytime. The steps to do this were
1. Install `pyinstaller` via `pip install pyinstaller` inside the virtual environment.
2. Set the shell variable by running `env PYTHON_CONFIGURE_OPTS="--enable-shared" pyevn install 3.9.15`. For some reason the next step would not work without running this first.
3. Finally, run `pyinstaller --onefile --clean  --noconsole -i /PATH_TO_ICON/icon_2.jpeg -n MyTimerApp src/main.py`.
