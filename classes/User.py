class User(object):
    id = ''
    name = ''
    surname = ''
    patronymic = ''

    # def __init__(self, ids, name, surname, patronymic):
    #     self.id = ids
    #     self.name = name
    #     self.surname = surname
    #     self.patronymic = patronymic

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def from_dict(self, data):
        for field in ['id', 'name', 'surname', 'patronymic']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
        }
        return data
