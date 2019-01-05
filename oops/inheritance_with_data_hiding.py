class Manager:
	room_PIN = 1234
	__locker_PIN = 9900

	def open_locker(self):
		print("locker unlocked with %d and %d" % (Manager.room_PIN, Manager.__locker_PIN))	

class Employee (Manager):
	room_PIN = 1200
	def open_locker(self):
		#print("room unlocked with %d, %d and %d" % (Manager.room_PIN, Employee.room_PIN, Manager.__locker_PIN))
		print("room unlocked with %d and %d" % (Manager.room_PIN, Employee.room_PIN))


s = Employee()
s.open_locker()


s = Manager()
s.open_locker()