
class cse_department_room:
    def __init__(self, total_table, total_chair) -> None:
        self.table = total_table
        self.chair = total_chair
        pass


# 401 no room
room_401 = cse_department_room(total_table=4, total_chair=3)

room_402 = cse_department_room(total_table=0, total_chair=2)
room_403 = cse_department_room(total_table=0, total_chair=2)
