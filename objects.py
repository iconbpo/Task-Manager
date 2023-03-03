class Admin:
    def __init__(self, first_name, last_name, date, gender, nickname, password ,typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.typeUser = typeUser


class Worker:
    def __init__(self, first_name, last_name, date, gender, nickname, password, manager_name, typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.manager_name = manager_name
        self.typeUser = typeUser


class Task:
    def __init__(self, worker_nickname, timein, timeout, date, outofdate, details, estado, manager_name ,note):
        self.worker_nickname = worker_nickname
        self.timein = timein
        self.timeout = timeout
        self.date = date
        self.outofdate = outofdate
        self.details = details
        self.estado = estado
        self.manager_name = manager_name
        self.note = note


class Manager:
    def __init__(self, first_name, last_name, date, gender, nickname, password, manager_name,typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.manager_name = manager_name
        self.typeUser = typeUser

class CEO:
    def __init__(self, first_name, last_name, date, gender, nickname, password, typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.typeUser = typeUser