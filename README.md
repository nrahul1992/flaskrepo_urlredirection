# flaskrepo_v2
# Author/Contributor - Rahul

The readMe is under progress...The complete development is yet to be completed or at least has to be brought to a sensible state. 

This is a Flask Sample repository. 

Use this for your learning purpose. 

Follow the steps to run this application:
1. Fork the application from my github repository
2. Install Python. - Any version from 3.x 
3. Download and install Pip tools - https://pypi.org/project/pip-tools/. Use the following URL to download the tool from
    the parent site. This comes standard with python 3.3 installation. To verify the installation of pip tool, go to the
    command/shell prompt and type "pip --version". This will show you the current version of the pip tool.  
4. Install the libraries/APIs in the requirements.txt. Path for the file is _<rootpath>\f\flaskr\requirements.txt_
5. run the redirect_app.py to start the server. 

DB Requirements- 
1. Download and install MongoDB for local/server. Follow the directions in the URL https://www.mongodb.com/download-center 
    Once you have the setup ready, open mongo in a shell/command prompt. You may use HUI tools like robomongo to interface with MongoDB. 
2. User db and collections creation will be done from within the application. Mongo db, being a schemaless db, doesn't 
    need the tables to have been created from begining. The collections can be created during the runtime of the 
    application where and when needed. Once the collections are created, the same will be used over throughout the 
    application proceedings.
3. Make sure your mongo instance is up and running for the working of the application. 
    To verify, open http://127.0.0.1:27017/. This will show you a message that
     _It looks like you are trying to access MongoDB over HTTP on the native driver port._
     Upon seeing the message you can be sure your instance is running. Also, I would recommend the command line based 
     interface for better grip and learning. 

DB Name : APP_USERS
Collection Used:    userlogindata
                    usersessiondata 
                    
For the AI based application, run the redirect_app.py. For the first run, uncomment the line #19. 
This will download the NLTK library which will be used there on for the language processing parts of the program. 
The download and installation process takes around 20-30 mins, once this is done, comment the line #19. This will 
prevent the application to unnecessarily download the NLTK library every time the application is run. 

After the download is complete and the NLTK is set up, close the connection/scocket opened after running redirect_app.py. 
Run chat_app.py for working with the AI based application. 

Also, install a solr box on your server/local machine. This is where the application knowledge base will be indexed and 
later searched for user response. 

Other db collection will be automatically created on the first run of the application. Just make sure the mongo instance
is up and running. 

Do not make any changes in the db collections manually. This will impact the data consistency for the application. If 
you are very well aware of the db scripts used along the application, then you may proceed at caution.   
           
Note to the collaborators: Please take the work ahead on solr indexing of the knowledge base so that it can be indexed 
and searched for user input.                  


