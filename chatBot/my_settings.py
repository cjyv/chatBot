

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'practice', #2
        'USER': 'root', #3                      
        'PASSWORD': 'cc1029',  #4              
        'HOST': 'localhost',   #5                
        'PORT': '3306', #6
    }
}

SECRET_KEY = 'django-insecure-&&im%*7vvf$w#0q78trwfm955!$9f=z8(6v65fihl#%*kcrp=2'  #기존 settings.py에 있던 시크릿키를 붙여넣는다