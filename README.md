# flaskrepo_v2

The readMe is under progress...The complete development is yet to be completed or atlaeast has to be brought to a sensible state. 

This is a Flask Sample repository. 

Use this for your learning purpose. 

Follow the steps to run this application:
1. Fork the application from my github repository
2. Install Python. 
3. Download and install Pip tools
4. Install the libraries/APIs in the requirements.txt
5. run the new_app.py to start the server. 

DB Requirements- 
1. Download and install MongoDB for local/server. 
2. user db and collections creation will be done from within the application. 
3. make sure your mongo instance is up and running for the working of the application. 

DB Name : APP_USERS
Collection Used:    userlogindata
                    usersessiondata 
                    
For the AI based application, run the redirect_app.py. For the first run, uncomment the line #19. 
This will download the NLTK library which will be used there on for the language processing parts of the program. 
The download and installation process takes around 20-30 mins, once this is done, comment the line #19. This will prevent the application to unnecessarily download the NLTK library every time the application is run. 

Also, install a solr box on your server/local machine. This is where the application knowledge base will be indexed and later searched for user response. 

Other db collection will be automatically created on the first run of the application. Just make sure the mongo instance is up and running. 

Do not make any changes in the db collections manually. This will impact the data consistency for the application. If you are very well aware of the db scripts used along the application, then you may proceed at caution.   
           
                

