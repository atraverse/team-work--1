import random


class Client:
    def __init__(self, name, age, sex, id=0):
        self.name = name
        self.age = age
        self.sex = sex

    def id_plus(self):
        """
        (self)-(str)
        Create an id of the client
        """
        self.id += 1
        return self.id

    def check(self):
        """
        (self)-(None)
        Return the error if it is in code
        """
        if self.age <= 0:
            raise ValueError("Impossible age")
        if self.sex != "F" or self.sex != "M":
            raise ValueError("Incorrect sex")

class Inputer:
    def __init__(self):
        pass
    def inp(self):
        self.inp = int(input("Please Input code of type of congratulation: "))
        return (self.inp)


class MailInfo:
    def __init__(self):
        self.number = Inputer().inp()

    def info_cel(self):
        """
        (self)-(str)
        choose the mail which to send
        """
        if self.number == 202:
            message1 = "Happy birthday"
            return message1
        elif self.number == 302:
            message2 = "Best wishes to you on your wedding day"
            return message2
        elif self.number == 402:
            message3 = "Merry Christmas"
            return message3
        elif self.number == 502:
            message4 = "Happy easter"
            return message4

class MailSender(MailInfo):
    def __init__(self):
        self.send_mail = MailInfo().info_cel()

    def send(self):
        """
        (self)-(None)
        Send the mail
        """
        return self.send_mail


class MailBox(Client, MailInfo):
    def __init__(self, name, age, sex):
        self.info_client = Client(name, age, sex).name
        self.add_mail_info = MailInfo().info_cel()

    def send_all(self):
        """
        (self)-(str)

        Return the congratulation
        """
        return "{}, {}".format(self.info_client, self.add_mail_info)


if __name__ == "__main__":
    a = MailBox("Nastia", "16", "W")
    print(a.send_all())
