from flask import Flask, render_template 

app = Flask(__name__)


# Datos dinamicos 
projects = [
    {"title":"proyecto1", "Descripcion": " Un proyecto de transistores", "link":"#"},
    {"title":"proyecto2", "Descripcion": " Un proyecto de transistores", "link":"#"}
]

technologies =  ["Python", "C/C++", "Rust", "Pandas"]

@app.route('/')
def home():
    return render_template(
        'index.html',
        projects=projects, 
        technologies=technologies
    )
    
    
if __name__ == '__main__':
    app.run(debug=True)
    