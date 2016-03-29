#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	if self.request.path == '/index.html':
            options= {
                'Title': "CarlyBelloff",
                'header': "Home",
                'path': self.request.path
            }
        elif self.request.path == '/pictures.html':
            options= {
                'Title': "Family",
                'header': "My Family",
                'path': self.request.path
            }
        elif self.request.path == '/blogs.html':
            options= {
                'Title': "Food",
                'header': "Favorite Foods",
                'path': self.request.path
            }
        elif self.request.path == '/contactme.html':
            options= {
                'Title': "Food",
                'header': "Favorite Foods",
                'path': self.request.path
            }
        else:
            return
        template = JINJA_ENVIRONMENT.get_template('templates' + self.request.path)
        self.response.write(template.render(options))

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.path == '/':
                options= {
                    'Title': "CarlyBelloff",
                    'header': "Home",
                    'path': "/index.html"
                }
                template = JINJA_ENVIRONMENT.get_template('templates' + '/index.html')
                self.response.write(template.render(options))

class LoginHandler(webapp2.RequestHandler): 
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates' + '/login.html')
        options={
                    'Title': "Login",
                    'header': "Login",
                    'path': self.request.path
                }
        self.response.write(template.render(options))

    def post(self):
        username=self.request.get('username')
        password=self.request.get('password')
        if username == 'Colleen':
            if password == 'pass':
                template = JINJA_ENVIRONMENT.get_template('templates' + '/loggedin.html')
                options= {
                    'Title': "Loggedin",
                    'header': "Logged in...",
                    'path': self.request.path
                    }
        else:
            template = JINJA_ENVIRONMENT.get_template('templates' + '/login.html')  
            options= {
                    'Title': "Login",
                    'header': "Login",
                    'message': "Bad credentials. Try again.",
                    'path': self.request.path
                }
            logging.info('username = ' + username)
            logging.info ('password = ' + password)
        self.response.write(template.render(options))

app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/index.html', MainHandler),
    ('/pictures.html', MainHandler),
    ('/blogs.html', MainHandler),
    ('/contactme.html', MainHandler),
    ('/login.html', LoginHandler),
    ('/loggedin.html', LoginHandler)
], debug=True)