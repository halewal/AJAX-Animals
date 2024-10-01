from flask import Flask, render_template 
import requests 
 
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    dog_url = get_dog() 
    return render_template('index.html', url=dog_url) 
 
@app.route('/get_dog', methods=['GET']) 
def get_dog(): 
    response = requests.get('https://dog.ceo/api/breeds/image/random') 
    data = response.json() 
    dog_image_url = data['message'] 
    return dog_image_url 
 
@app.route('/get_cat', methods=['GET']) 
def get_cat(): 
    response = requests.get('https://api.thecatapi.com/v1/images/search') 
    data = response.json() 
    cat_image_url = data[0]['url'] 
    return cat_image_url 
 
if __name__ == '__main__': 
    app.run(debug=True) 
