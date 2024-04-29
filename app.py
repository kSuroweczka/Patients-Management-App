from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients
                 (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, pesel TEXT, street TEXT, city TEXT, zip TEXT, url TEXT)''')
    conn.commit()
    conn.close()

def add_patient (firstname, lastname, pesel, street, city, zip_code, url):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("INSERT INTO patients (firstname, lastname, pesel, street, city, zip, url) VALUES (?, ?, ?, ?, ?, ?, ?)", (firstname, lastname, pesel, street, city, zip_code, url))
    conn.commit()
    conn.close()

def update_patient(patient_id, firstname, lastname, pesel, street, city, zip_code, url):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("UPDATE patients SET firstname=?, lastname=?, pesel=?, street=?, city=?, zip=?, url=? WHERE id=?", (firstname, lastname, pesel, street, city, zip_code, url, patient_id))
    conn.commit()
    conn.close()

def delete_patient(patient_id):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()

def get_patient(patient_id):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    patient = c.fetchone()
    conn.close()
    return patient

def get_patients():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patients")
    patients = c.fetchall()
    conn.close()
    return patients

def search_patients(query, sort_by=None, sort_order=None):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    order_by_clause = ""
    if sort_by == 'firstname':
        order_by_clause = "ORDER BY firstname"
    elif sort_by == 'lastname':
        order_by_clause = "ORDER BY lastname"
    
    if sort_order == 'desc':
        order_by_clause += " DESC"
    
    c.execute("SELECT * FROM patients WHERE firstname LIKE ? OR lastname LIKE ? OR city LIKE ? " + order_by_clause, ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
    patients = c.fetchall()
    conn.close()
    return patients

@app.route('/', methods=['GET', 'POST'])
def index():
    create_database()
    query = request.form.get('search', '')
    sort_by = request.form.get('sort_by', None)
    sort_order = request.form.get('sort_order', None)
    
    if request.method == 'POST':
        patients = search_patients(query, sort_by, sort_order)
    else:
        patients = get_patients()
    
    return render_template('patients.html', patients=patients)

@app.route('/patient/<int:id>')
def patient(id):
    patient = get_patient(id)
    return render_template('patient.html', patient=patient)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient_page():
    if request.method == 'GET':
        return render_template('add_patient.html')
    elif request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        pesel = request.form['pesel']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        url = request.form['url']
        add_patient(firstname, lastname, pesel, street, city, zip_code, url)
        return redirect(url_for('index'))

@app.route('/update_patient/<int:patient_id>', methods=['GET', 'POST'])
def update_patient_page(patient_id):
    if request.method == 'GET':
        patient = get_patient(patient_id)
        return render_template('update_patient.html', patient=patient)
    elif request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        pesel = request.form['pesel']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        url = request.form['url']
        update_patient(patient_id, firstname, lastname, pesel, street, city, zip_code, url)
        return redirect(url_for('index'))

@app.route('/delete_patient/<int:patient_id>', methods=['POST'])
def delete_patient_route(patient_id):
    delete_patient(patient_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
