# POMOPY

Pomopy is a Pomodoro program written in Python, simple, minimalist, and designed to be run in the terminal.

## Usage

Pomopy supports Windows, Linux, and MacOS. There are two executables available for easier opening, but you can also run the script directly or add Pomopy to your computer's PATH.

### Running the script in the terminal

To run the script in the terminal, simply open it (make sure you have the latest version of Python installed) in the folder where pomo.py is located, and execute the following command:

```
python3 pomo.py
```
### Using the executables

In the directory, you'll find the files pomopy.bat (Windows) and pomopy.sh (Linux). They are just an easier way to execute the "python3..." code. In Windows, simply run the file normally, and if you're using Linux with the terminal open in the code folder, type the following command:
```
./pomopy.sh
```
### Adding to the PATH
You can also add the code as a shortcut in your computer's PATH. Check how to do this in the operating system you're using.

#### For macOS and Linux:
Open the Terminal.
Execute the following command to open the .bashrc file in a text editor:
```bash
nano ~/.bashrc
```
Add the following line to the file:
```bash
alias pomopy='python3 /path/to/directory/pomo.py'
```
Make sure to replace "/path/to/directory" with the correct path to the directory where the pomo.py file is located.

Press Ctrl + X to exit the nano editor, then press Y to save the changes.

Execute the following command to update the terminal profile file:
```bash
source ~/.bashrc
```
Now, you can simply type `pomopy` in the terminal to run the pomo.py program using Python 3. Make sure you have correctly replaced the path to the pomo.py file directory.

<!-- Remember to replace `/path/to/directory` with the correct path to the directory where the pomo.py file is located. Restart the terminal for the changes to take effect. -->