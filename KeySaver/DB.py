from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class DB:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('keys.db')

        self.query = QSqlQuery()

    def init(self) -> bool:
        if not self.db.open():
            return False

        self.query.exec_("CREATE TABLE IF NOT EXISTS `Auth`("
                    "`name` VARCHAR(255) NOT NULL,"
                    "`login` VARCHAR(255) NOT NULL,"
                    "`password` VARCHAR(255) NOT NULL);")

        return True

    def addRecord(self, name: str, login: str, password: str) -> bool:
        print(name)

        self.query.exec_(f"INSERT INTO Auth VALUES ('{name}', '{login}', '{password}')")

        if self.query.lastError():
            return False

        return True

    def updateRecord(self, id: int, newName: str, newLogin: str, newPassword: str) -> bool:
        self.query.exec_(f"UPDATE Auth SET name = '{newName}', login = '{newLogin}', "
                         f"password = '{newPassword}' WHERE rowid = {id}")

        if self.query.lastError():
            return False

        return True

    def deleteRecord(self, id: int) -> bool:
        self.query.exec_(f"DELETE FROM Auth WHERE rowid = {id}")

        if self.query.lastError():
            return False

        return True

    def getCount(self):
        self.query.exec_(f"SELECT COUNT(*) FROM Auth")

        self.query.first()
        return self.query.value(0)

    def filter(self, search: str):
        self.query.exec_(f"SELECT rowid, * FROM Auth WHERE name LIKE '%{search}%'")

        resultList = []

        while self.query.next():
            row = {
                'id': self.query.value(0),
                'name': self.query.value(1),
                'login': self.query.value(2),
                'password': self.query.value(3)
            }

            resultList.append(row)

        return resultList

    def clear(self):
        self.query.exec_("DELETE FROM Auth")

    def close(self):
        self.db.close()
