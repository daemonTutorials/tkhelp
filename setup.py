from distutils.core import setup

setup(
    name = "tkhelp",
    version = "2.1.1",
    author = "Maik Wöhl",
    author_email = "maik.woehl@web.de",
    url = "http://www.daemon-tuts.de/blog",
    description = "tkhelp is a german help program. Is implemented a GUI with many Tk-Widgets and a Webinterface, that is easy to update.",
    long_description = "The GUI is a small collection of Tk-Widget descriptions. In the Webinterface you can see many examples and a great description, because the GUI is only updated in the stable releases(1.0,1.5,2.0,2.5,...).",
    data_files = ['test.gif', 'CHANGELOG', 'README', 'TODO'],
    py_modules = ['tkhelp', 'tkh_splash3', 'tkhelp_lang_de', 'dt_tkobjects', 'config']
    
)
