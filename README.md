# whois_python
Face Recognition Program built using python

# If getting error
If your error is: [CRITICAL          ] [App         ] Unable to get a Window, abort.
In cmd go to Python34 and then to Scripts and install the following:

pip install --upgrade pip wheel setuptools

pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

pip install kivy.deps.gstreamer

pip install kivy.deps.angle

pip install kivy

For the people that run into any other problem like: the pip install pypiwin32 can give an error because pywin32 is possibly already installed and cannot be uninstalled. For me it worked when i ran the items in the second line via a seperate pip install and ignore the pypiwin32 install error.
