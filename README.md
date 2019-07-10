Django Tsugi Sample Application
-------------------------------

This is a sample application written using 
https://pypi.org/project/django-tsugi/

This application is designed to be connected into a running Tsugi server, using the
<b>Admin -> External tools</b> feature.  It receives a special Tsugi-style signed
JWT launch at <b>/grade/launch</b> to provision a session on this application.
The application can send a grade back to the LMS <i>through Tsugi</i> using
an API callback.

Tsugi handles all of the LTI 1.1, LTI Advantage, or even Google Classroom mechanics
and allows this tool to be very simple.

The source code for this application is at
https://github.com/tsugiproject/djtest
and you can find a tutorial / walkthrough on how to install your own
copy of this tool at
https://www.tsugi.org/django.txt
