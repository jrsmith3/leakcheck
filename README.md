leakcheck - minimal python script for vacuum leak testing with SRS RGA


Disclaimer
----------
The author of this software takes no responsibility for the correctness of this code and offers no warranty for the user's equipment. Improper use may damage or destroy your RGA. Please read the instrument's manual and consult with the manufacturer if you have any questions.


Install
-------
Copy this script into a directory on the computer that will run the RGA.


Start
-----
1. Make sure the RGA head is properly powered and connected to the computer. I used a USB to RS232 adapter based on the Prolific 2303 chipset on Mac OS 10.8 -- the driver can currently be found at http://plugable.com/drivers/prolific.

2. Install pyserial and matplotlib.

3. Fire up a terminal and execute

$ python leakcheck.py


Documentation
-------------
The code is straightforward and is liberally documented. Also see the manual for the SRS RGA series, currently located at http://www.thinksrs.com/downloads/PDFs/Manuals/RGAm.pdf.
