# VisionTracker1.0
Real-time Directional Object Tracking in a Video Sequence

#### Use the link below to Download the Installers - Widows(.exe) and Ubuntu(.deb) 

https://drive.google.com/open?id=1J76_fbNzRC5epfLrlrlG-H_XwCqOHtyE

#### How to Use?

   1. Install the 'VisionTrackerSetup.exe' file found in Executables folder (for Ubuntu Install 'VisionTracker.deb').
   2. Open the Application and Click 'Directional Tracking' Tab.
   3. Select the Object to Track from the List of Radio Buttons.
   4. Load the MobileNet_SSD Weight file by clicking 'Load Pre-trained Weights'.
   5. Load the MobileNet_SSD Label file by clicking 'Load Pre-trained Labels'.
   6. Load or Capture Video using corresponding Push Buttons and Click 'Track'.
   7. A message will pop-up. Read the message and continue as explained.

#### To run the Source Code the following requirements must be Satisfied

  1. Python (Version==3.6.7)
  2. OpenCV (Version==3.4.2.17) (with Contib modules)
  3. PyQt5 (Version==4.19.15)
  4. NumPy (Version==1.14.2)
  5. dlib (Version==19.17.0)
  
##### # Note: Before running the source code, comment this line "from fbs_runtime.application_context import ApplicationContext". This is a Library for creating Installers.
