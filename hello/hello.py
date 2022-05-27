import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('hello dhariya and pragati')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)