# socialapps


## The document will coming out 

## Using django version 2 and Python 3.6

#### The goal is to access to login social media via Oauth2 for facebook  using social-auth-app-django==3.1.0 to access the process https://python-social-auth-docs.readthedocs.io/en/latest/backends/facebook.html
#### library include all social network for more info https://python-social-auth-docs.readthedocs.io/en/latest/backends/index.html#social-backends

#### Create basic application no models required only project url to redirect the user and one application to hold\
#### The methdos login and index in this application with two templates index and login only rest of the process are 
#### Based in main project file like urls and setting which is the all process

#### To logout using views from django.contrib.auth methods

#### Using another package to show all lib package has been installed help the developer to see what else can do

#### Create one button allowed user to redirect to facebook without creating any forms for login
#### In the settings added following:

### SOCIAL_AUTH_FACEBOOK_KEY User Identification
### SOCIAL_AUTH_FACEBOOK_SECRET User secret key

#### The two line above allowed user automatcially to login in to facebook but the current user but that is not happen to be able to longin therefore the SOCIAL_AUTH_FACEBOOK_SCOPE request the email permission to be able to login however the not sent email by defaul.

#### the social apps on own account https://developers.facebook.com/tools/ when you add the above update login with
#### login button to <a href="{% url 'social:begin' 'facebook' %}" title="login">Facebook</a> redirect you to fb account user image_1 display small screen asking continue as username you will be successfully logedin

#### Create super user to access to admin page and you will see ther detail 

#### To retrieve extra setails of the facebook user need to add SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS SOCIAL_AUTH_FACEBOOK_EXTRA_DATA 

#### The requirement based on id, name, email, picture and link

### Notice there is obe small bug not sure 100% what I have missed on social_app I have created on Facebook.
## Adding SOCIAL_AUTH_FACEBOOK_SCOPE display a bug need to fixed line 119 in the settings
TypeError at /social-auth/login/facebook/
must be str, not list

#### I assume the issue related to social_app on developer.facebook.com I created.

#### Using Anaconda > Autoformat PEP8 Errors to format automatically the codes.





