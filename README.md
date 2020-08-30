# Traffy, An IBM Watson Assistant
These files include the basic framework for a IBM Watson Assistant API integration with python3.
[Documentation](https://cloud.ibm.com/apidocs/assistant/assistant-v2)

**Note:** There is a limit to the number of users and calls on the IBM Cloud. If the script returns an error, it is most likely that this limit has been exceeded.

### API Calls
- A weather API from weatherbit.io could be called for current or forecasted weather in the US.
- A IP address API from ipdata.co is used to find the current location and/or timezone.

### In The Works
- An organization of individual API calls into separate functions without any significant specialized code in traffy.py...
- Separate the skills in IBM Watson Assistant to specifice categories (Ex: General Chat, Weather, etc.)...
- An API call that connects people with organizations in the US using charitynatvigator.org...
- An implementation of Traffy into a GUI using Kivy...
- An update to the range of responses to the user...

### Usage Instructions
**Downloading**
1) Download and unzip all the files into one folder
4) Move all the images in the Icons folder into the main folder
5) Delete the empty Icons folder

**Running**
1) Open the terminal
2) Go to the folder with all the files using the *cd [folder]* command
-
  - **Note:** This command is necessary for every directory level.

  - *Example:* If my folder is named "Traffy" and is in the "Documents" folder, I run *cd Documents* then *cd Traffy*.

  - If the current directory is unknown run *ls* to get a list of folders.

3) Run *python3 traffy.py*
