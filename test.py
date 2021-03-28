from pprint import pprint
class Person:
    def __init__(self, фамилия, возраст, дата_рождения, пол):
        self.фамилия, self.возраст, self.дата_рождения, self.пол = фамилия, возраст, дата_рождения, пол
        self.key = (фамилия, дата_рождения)
    def __repr__(self):
        return "Person('%s',%s,'%s','%s')" % (self.фамилия, self.возраст, self.дата_рождения, self.пол)
    
Маслов=Person('Маслов', 33, '30.3.1988', 'муж.')
Радок=Person('Радок', 19, '31.7.2001', 'муж.')
Воронова=Person('Воронова', 35, '5.11.1985', 'жен.')
Жаков=Person('Жаков', 17, '4.11.2003', 'муж.')
люди=[
    [Маслов.key,Маслов],
    [Радок.key,Радок],
    [Воронова.key,Воронова],
    [Жаков.key,Жаков],
    ]

pprint(люди)
pprint(люди[2][1])
