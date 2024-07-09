from flask import render_template

class renderer:
    def __init__(self):
        pass
    
    def render(self, data):
        return render_template('index.html', data=data)