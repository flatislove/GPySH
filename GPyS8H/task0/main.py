import model.database_operation as db
import controller
import service

#Создать информационную систему позволяющую работать с 
# сотрудниками некой компании
# несколько таблиц
# импорт/экпорт(различные виды экспорта(по запросам)
#фио, телефон, должность

db.add_tables()
controller.menu()