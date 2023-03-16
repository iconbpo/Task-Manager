import csv
import objects
from xhtml2pdf import pisa
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Flask, render_template
app = Flask(__name__)
CORS(app)


managers = []
workers = []
admins = []
tasks = []
ceos = []



# type user 1 Worker , Type user 2 Manager ,  TypeUser 3 Admin , Type User 4 CEO

@app.route('/')
def index():
    return render_template('index.html')



@app.route("/backup")
def tasks_backup():
    fields = 'Worker Nickname ,Time In, Time Out,Date, Out Of Date, Details,Status, Manager Name, Note\n'
    with open('./static/backupTasks.csv', 'w') as f:
        f.write(fields)
        for task in tasks:
            f.write(f'{task.worker_nickname},{task.timein},{task.timeout},{task.date},{task.outofdate},{task.details},{task.estado},{task.manager_name},{task.note } \n')
    return app.send_static_file("backupTasks.csv")


@app.route("/reports/task")
def tasks_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Tasks:</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>Nickname</th><th>Time In</th><th>Time Out</th><th>Date</th><th>Out Of Date</th><th>Details</th><th>Status</th><th>Manager Name</th><th>Note</th></tr>'
    for task in tasks:
        html += "<tr>"
        html += "<td>" + task.worker_nickname + "</td>"
        html += "<td>" + task.timein + "</td>"
        html += "<td>" + task.timeout + "</td>"
        html += "<td>" + task.date + "</td>"
        html += "<td>" + task.outofdate + "</td>"
        html += "<td>" + task.details + "</td>"
        html += "<td>" + task.estado + "</td>"
        html += "<td>" + task.manager_name + "</td>"
        html += "<td>" + task.note + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/tasks.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("tasks.pdf")


@app.route("/reports/worker")
def workers_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Workers:</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>First Name</th><th>Last Name</th><th>Date of Birth</th><th>Gender</th><th>Nickname</th><th>Password</th><th>Manager Name</th></tr>'
    for worker in workers:
        html += "<tr>"
        html += "<td>" + worker.first_name + "</td>"
        html += "<td>" + worker.last_name + "</td>"
        html += "<td>" + worker.date + "</td>"
        html += "<td>" + worker.gender + "</td>"
        html += "<td>" + worker.nickname + "</td>"
        html += "<td>" + worker.password + "</td>"
        html += "<td>" + worker.manager_name + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/workers.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("workers.pdf")


@app.route("/reports/manager")
def managers_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Managers</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>First Name</th><th>Last Name</th><th>Date of Birth</th><th>Gender</th><th>Nickname</th><th>Password</th><th>Manager Name</th></tr>'
    for manager in managers:
        html += "<tr>"
        html += "<td>" + manager.first_name + "</td>"
        html += "<td>" + manager.last_name + "</td>"
        html += "<td>" + manager.date + "</td>"
        html += "<td>" + manager.gender + "</td>"
        html += "<td>" + manager.nickname + "</td>"
        html += "<td>" + manager.password + "</td>"
        html += "<td>" + manager.manager_name + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/managers.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("managers.pdf")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data["nickname"]
    password = data["password"]
    for worker in workers:
        if worker.nickname == nickname:
            if worker.password == password:
                return jsonify({
                    "first_name": worker.first_name,
                    "last_name": worker.last_name,
                    "date": worker.date,
                    "gender": worker.gender,
                    "nickname": worker.nickname,
                    "password": worker.password,
                    "manager_name": worker.manager_name,
                    "typeUser": worker.typeUser
                    }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    for manager in managers:
        if manager.nickname == nickname:
            if manager.password == password:
                return jsonify({
                    "first_name": manager.first_name,
                    "last_name": manager.last_name,
                    "date": manager.date,
                    "gender": manager.gender,
                    "nickname": manager.nickname,
                    "password": manager.password,
                    "manager_name": manager.manager_name,
                    "typeUser": manager.typeUser
                    }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    for ceo in ceos:
        if ceo.nickname == nickname:
            if ceo.password == password:
                return jsonify({
                    "first_name": ceo.first_name,
                    "last_name": ceo.last_name,
                    "date": ceo.date,
                    "gender": ceo.gender,
                    "nickname": ceo.nickname,
                    "password": ceo.password,
                    "typeUser": ceo.typeUser
                    }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    if nickname == "admin":
        if password == "ALL3V14T3!7410":
            return jsonify({
                    "first_name":"TECH",
                    "last_name":"ADMIN",
                    "date":"01/12/1996",
                    "gender":"m",
                    "nickname":"admin",
                    "password":"ALL3V14T3!7410",
                    "typeUser": 3
                    }), 200
        else:
            return jsonify({"message": "bad credentials"}), 400


@app.route("/manager", methods=["GET", "POST", "PUT", "DELETE"])
def manager():
    if request.method == "GET":
        tmp = []
        for manager in managers:
            tmp.append({"first_name": manager.first_name, "last_name": manager.last_name,
                       "date": manager.date, "gender": manager.gender,
                       "nickname": manager.nickname, "password": manager.password,
                       "manager_name": manager.manager_name, "typeUser": manager.typeUser})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        manager_name = data["manager_name"]                 
        typeUser = data["typeUser"]                 
        valid_manager = True
        for manager in managers:
            if manager.nickname == nickname:
                valid_manager = False
        if valid_manager:
            managers.append(objects.Manager(first_name, last_name, date, gender, nickname, password, manager_name, typeUser))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "manager Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        manager_name = data["manager_name"]
        typeUser = data["typeUser"]      
        for manager in managers:
            if manager.nickname == nickname:
                manager.first_name = first_name
                manager.last_name = last_name
                manager.date = date
                manager.gender = gender
                manager.password = password
                manager.manager_name = manager_name
                manager.typeUser = typeUser
        return jsonify({"message": "manager edited"}), 200
    elif request.method == "DELETE":
        nickname = request.args.get("nickname")
        for manager in managers:
            if manager.nickname == nickname:
                managers.remove(manager)
        return jsonify({"message": "manager Eliminado"}), 200


@app.route("/ceo", methods=["GET", "POST", "PUT", "DELETE"])
def ceo():
    if request.method == "GET":
        tmp = []
        for ceo in ceos:
            tmp.append({"first_name": ceo.first_name, "last_name": ceo.last_name,
                       "date": ceo.date, "gender": ceo.gender,
                       "nickname": ceo.nickname, "password": ceo.password,
                       "typeUser": ceo.typeUser})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        typeUser = data["typeUser"]                 
        valid_ceo = True
        for ceo in ceos:
            if ceo.nickname == nickname:
                valid_ceo = False
        if valid_ceo:
            ceos.append(objects.CEO(first_name, last_name, date, gender, nickname, password, typeUser))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "ceo Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        typeUser = data["typeUser"]      
        for ceo in ceos:
            if ceo.nickname == nickname:
                ceo.first_name = first_name
                ceo.last_name = last_name
                ceo.date = date
                ceo.gender = gender
                ceo.password = password
                ceo.typeUser = typeUser
        return jsonify({"message": "ceo edited"}), 200
    elif request.method == "DELETE":
        nickname = request.args.get("nickname")
        for ceo in ceos:
            if ceo.nickname == nickname:
                ceos.remove(ceo)
        return jsonify({"message": "ceo Eliminado"}), 200



@app.route("/worker", methods=["GET", "POST", "PUT", "DELETE"])
def worker():
    if request.method == "GET":
        tmp = []
        for worker in workers:
            tmp.append({"first_name": worker.first_name, "last_name": worker.last_name,
                       "date": worker.date, "gender": worker.gender,
                       "nickname": worker.nickname, "password": worker.password,
                       "manager_name": worker.manager_name, "typeUser": worker.typeUser})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        manager_name = data["manager_name"]
        typeUser = data["typeUser"]                
        valid_worker = True
        for worker in workers:
            if worker.nickname == nickname:
                valid_worker = False
        if valid_worker:
            workers.append(objects.Worker(first_name, last_name, date, gender, nickname, password, manager_name, typeUser))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "worker Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        manager_name = data["manager_name"]      
        typeUser = data["typeUser"]                
        for worker in workers:
            if worker.nickname == nickname:
                worker.first_name = first_name
                worker.last_name = last_name
                worker.date = date
                worker.gender = gender
                worker.password = password
                worker.manager_name = manager_name
                worker.typeUser = typeUser
        return jsonify({"message": "worker edited"}), 200
    elif request.method == "DELETE":
        nickname = request.args.get("nickname")
        for worker in workers:
            if worker.nickname == nickname:
                workers.remove(worker)
        return jsonify({"message": "worker Eliminada"}), 200


@app.route("/task", methods=["GET", "POST", "PUT", "DELETE"])
def task():
    if request.method == "GET":
        tmp = []
        for task in tasks:
            tmp.append({"worker_nickname": task.worker_nickname, "timein": task.timein,"timeout": task.timeout,
                       "date": task.date, "outofdate": task.outofdate ,"details": task.details,
                       "estado": task.estado, "manager_name": task.manager_name, "note": task.note})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        worker_nickname = data["worker_nickname"]
        timein = data["timein"]
        timeout = data["timeout"]
        date = data["date"]
        outofdate = data["outofdate"]
        details = data["details"]
        estado = data["estado"]
        manager_name = data["manager_name"]      
        note = data["note"]        
        valid_task = True
        for task in tasks:
            if task.details == details and task.date == date and task.worker_nickname == worker_nickname: #Comparamos detalles y fecha entre todos nuestros task para verificar si alguno se repite con el mismo username
                valid_task = False
        if valid_task:
            tasks.append(objects.Task(worker_nickname, timein, timeout, date, outofdate, details, estado, manager_name, note))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "task Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        worker_nickname = data["worker_nickname"]
        timein = data["timein"]
        timeout = data["timeout"]
        date = data["date"]
        outofdate = data["outofdate"]
        details = data["details"]
        estado = data["estado"]
        manager_name = data["manager_name"]   
        note = data["note"]            
        for task in tasks:
            if task.details == details and task.date == date and task.worker_nickname == worker_nickname: #Comparamos detalles y fecha entre todos nuestros task para verificar si alguno se repite con el mismo username
                task.worker_nickname = worker_nickname
                task.timein = timein
                task.timeout = timeout
                task.date = date
                task.outofdate = outofdate
                task.details = details
                task.estado = estado
                task.manager_name = manager_name 
                task.note = note               
        return jsonify({"message": "task Editada"}), 200
    elif request.method == "DELETE":
        details = request.args.get("details")
        for task in tasks:
            if task.details == details:
                tasks.remove(task)
        return jsonify({"message": "task Eliminada"}), 200


if __name__ == '__main__':
    app.run(host='localhost', port=3000 , ssl_context='adhoc')