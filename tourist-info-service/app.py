from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://Pariwisata_owner:EX9tbmJT2HoV@ep-sparkling-violet-a13kfh1z.ap-southeast-1.aws.neon.tech/Pariwisata?sslmode=require')
db = SQLAlchemy(app)

class TouristInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/info', methods=['GET'])
def get_info():
    infos = TouristInfo.query.all()
    return jsonify([{'id': info.id, 'name': info.name, 'description': info.description, 'location': info.location} for info in infos])

@app.route('/info', methods=['POST'])
def add_info():
    info_data = request.json
    new_info = TouristInfo(name=info_data['name'], description=info_data['description'], location=info_data['location'])
    db.session.add(new_info)
    db.session.commit()
    return jsonify({'id': new_info.id, 'name': new_info.name, 'description': new_info.description, 'location': new_info.location})

@app.route('/info/<int:id>', methods=['PUT'])
def update_info(id):
    info_data = request.json
    info = TouristInfo.query.get(id)
    if info:
        info.name = info_data['name']
        info.description = info_data['description']
        info.location = info_data['location']
        db.session.commit()
        return jsonify({'id': info.id, 'name': info.name, 'description': info.description, 'location': info.location})
    return jsonify({'error': 'Info not found'}), 404

@app.route('/info/<int:id>', methods=['DELETE'])
def delete_info(id):
    info = TouristInfo.query.get(id)
    if info:
        db.session.delete(info)
        db.session.commit()
        return jsonify({'message': 'Info deleted'})
    return jsonify({'error': 'Info not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
