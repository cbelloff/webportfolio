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
                'path': self.request.path
            }
        elif self.request.path == '/blogs.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/resume.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/contactme.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogone.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogtwo.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogthree.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogfour.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogfive.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogsix.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogseven.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogeight.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blognine.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/blogten.html':
            options= {
                'path': self.request.path
            }
        elif self.request.path == '/submitted.html':
            options= {
                'path': self.request.path
            }
        else:
            return
        template = JINJA_ENVIRONMENT.get_template('templates' + self.request.path)
        self.response.write(template.render(options))

    def post(self):
        name=self.request.get('name')
        email=self.request.get('email')
        message=self.request.get('message')

        logging.info(name)
        logging.info(email)
        logging.info(message)
   
        
        template = JINJA_ENVIRONMENT.get_template('templates/submitted.html')
        options={
            'path': "/submitted.html"
        }
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



app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/index.html', MainHandler),
    ('/blogs.html', MainHandler),
    ('/resume.html', MainHandler),
    ('/contactme.html', MainHandler),
    ('/blogone.html', MainHandler),
    ('/blogtwo.html', MainHandler),
    ('/blogthree.html', MainHandler),
    ('/blogfour.html', MainHandler),
    ('/blogfive.html', MainHandler),
    ('/blogsix.html', MainHandler),
    ('/blogseven.html', MainHandler),
    ('/blogeight.html', MainHandler),
    ('/blognine.html', MainHandler),
    ('/blogten.html', MainHandler),
    ('/submitted.html', MainHandler)
], debug=True)