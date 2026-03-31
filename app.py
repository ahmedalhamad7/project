from flask import Flask, render_template, request, jsonify

from database import get_db
from datetime import datetime

app = Flask(__name__)


@app.route('/api/incidents', methods=['GET'])
def list_incidents():
    db = get_db()
    rows = db.execute('SELECT * FROM incidents').fetchall()
    incidents = [dict(row) for row in rows]
    return jsonify(incidents)


@app.route('/api/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()

    title = data.get('title')
    description = data.get('description')
    severity = data.get('severity')
    status = data.get('status', 'open')
    created_at = datetime.now(datetime.timezone.utc)
    resolved_at = None

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO incidents (title, description, severity, status, created_at, resolved_at) VALUES (?, ?, ?, ?, ?, ?)',
        (title, description, severity, status, created_at, resolved_at)
    )
    db.commit()
    return jsonify({'id': cursor.lastrowid, 'title': title, 'description': description, 'severity': severity, 'status': status, 'created_at': created_at, 'resolved_at': resolved_at}), 201



@app.route('/api/incidents/<int:id>/status', methods=['PUT'])
def update_incident_status(id):
    data = request.get_json()
    new_status = data.get('status')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('UPDATE incidents SET status = ? WHERE id = ?', (new_status, id))
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({'error': 'Incident not found'}), 404

    return jsonify({'message': 'Incident status updated successfully'}), 200

"""
○ GET /api/incidents/active - Get all unresolved incidents (status != ;resolved) 
○ POST /api/incidents/{id}/updates - Add a status update to an incident 
"""