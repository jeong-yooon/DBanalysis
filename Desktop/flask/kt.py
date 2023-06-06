from flask import *
import pymongo, os

app = Flask(__name__)
app.secret_key = os.urandom(24)
client = pymongo.MongoClient('mongodb://kt:ktpw@3.34.138.63:27017')

def is_login():
    try:
        session['id']
        return True
    except:
        return False

@app.route('/')
def index():
    user = {}
    if is_login():
        user['name'] = session['id']
    return render_template('index.html', user=user)

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/api/join', methods=['POST'])
def apt_join():
    account = dict(request.values)
    print('account : ', account)
    
    # connect collection
    collection = client.mongo.users
    
    result = {}
    # check account
    document = collection.find_one({'id': account['id']})
    if document: # already has account
        result['msg'] = 'Already has acount.'
        
    else: # save account
        save_result = collection.insert_one(account)
        result['inserted_id'] = save_result.inserted_id
        result['msg'] = 'Joined account.'
    
    return jsonify(result), 200    
    
    # result = {'code' : 201}
    # return jsonify(result), 200

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    account = dict(request.values)
    
    # check account on database
    collection = client.mongo.users
    document = collection.find_one({'id': account['id'], 'pw': account['pw']})

    result = {}
    if document:
        session['id'] = account['id']
        result['msg'] = 'logined'
    else:
        result['msg'] = 'no account'
    return jsonify(result)


@app.route('/contents')
def contents():
    return render_template('contents.html')

# debug : 개발자모드 : 코드수정하면 바로 서버재시작해서 적용
app.run(debug=True)