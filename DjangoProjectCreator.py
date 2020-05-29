import os
print("You have to manually add templates folder in settings.py > dir = os.path.join(BASE_DIR , 'templates')")
projectName = input('Enter the project  name:- ')
appName =input('Enter the app name:- ')
pathName = input('Enter the path name:- ')

os.chdir(pathName)
try:
    os.mkdir(projectName)
except Exception as e:
    print(e)


os.chdir(os.path.join(pathName , projectName))
mainDir = os.path.join(pathName , projectName)

os.system('django-admin startproject '+ projectName)
os.chdir(os.path.join(mainDir , projectName))
os.mkdir('templates')
os.mkdir('static')
task = ['python manage.py startapp ' + appName]
line = "\nSTATICFILES_DIRS = [os.path.join(BASE_DIR , 'static')]"
byte = bytes(line , 'utf-8')
for i in task:
    os.system(i)
os.chdir(projectName)
print(os.getcwd())
file = open('settings.py' , 'ab')
file.write(byte)
os.chdir(os.path.join(mainDir , projectName))
file.close()
# urls
os.chdir(os.path.join(mainDir , projectName , appName))


urlFile = open('urls.py' , 'ab')
urlList = ["from . import views\nfrom django.urls import path\n", "urlpatterns = []"]
for i in urlList:
    add = bytes(i , 'utf-8')
    urlFile.write(add)
urlFile.close()

#urlProjectUpdate
os.remove(os.path.join(mainDir , projectName , projectName  ,'urls.py'))
os.chdir(os.path.join(mainDir , projectName , projectName))
urlproject = [ "from django.contrib import admin\n", "from django.urls import path , include\n", "urlpatterns = [ path('admin/', admin.site.urls),\n\tpath('' , include('"+appName+".urls'))]"]
urlprojectFile = open('urls.py' , 'wb')
for i in urlproject :
    add= bytes(i , 'utf-8')
    print(add)
    urlprojectFile.write(add)
urlprojectFile.close()

#openPycharm
#os.chdir(mainDir)
#os.system('pycharm ' + projectName)




