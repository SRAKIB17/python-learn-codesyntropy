class cseDepartment(object):
    def __init__(self, room_no, total_student):
        self.room_no = room_no
        self.total_student = total_student

    def show_room_no(self):
        return self.room_no

    def show_total_student(self):
        return self.total_student


room_301 = cseDepartment(301, 55)
room_302 = cseDepartment(302, 45)

print(room_301.show_room_no())
print(room_302.show_room_no())
