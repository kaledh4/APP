import subprocess

# Define the command to run each Streamlit app
command_app1 = "streamlit run the_viewer.py"
command_app2 = "streamlit run fofo.py"

# Start each app in a separate terminal window
subprocess.Popen(command_app1, shell=True)
subprocess.Popen(command_app2, shell=True)
