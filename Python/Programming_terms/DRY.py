# Don't repeat yourself

# a principle of software development aimed at repetition of information
# of any kind.

################################################
'''Bad code example'''

def homePage():
    print('<div class="header">')
    print('<a href="#>Home</a>')
    print('<a href="#>About</a>')
    print('<a href="#>Contact</a>')
    print('</div>')

    print('<p>Welcome to our home page</p>')

    print('<div class="footer>')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')

def aboutPage():
    print('<div class="header">')
    print('<a href="#>Home</a>')
    print('<a href="#>About</a>')
    print('<a href="#>Contact</a>')
    print('</div>')

    print('<p>Welcome to our About page</p>')

    print('<div class="footer>')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')

def contactPage():
    print('<div class="header">')
    print('<a href="#>Home</a>')
    print('<a href="#>About</a>')
    print('<a href="#>Contact</a>')
    print('</div>')

    print('<p>Welcome to our contact page</p>')

    print('<div class="footer>')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')

homePage()
aboutPage()
contactPage()


################################################
'''Good example'''

def header():
    print('<div class="header">')
    print('<a href="#>Home</a>')
    print('<a href="#>About</a>')
    print('<a href="#>Contact</a>')
    print('</div>')

def footer():
    print('<div class="footer>')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')

def homePage():
    header()
    print('<p>Welcome to our home page</p>')
    footer()

def aboutPage():
    header()
    print('<p>Welcome to our about page</p>')
    footer()

def contactPage():
    header()
    print('<p>Welcome to our contact page</p>')
    footer()


################################################
'''Another example'''

