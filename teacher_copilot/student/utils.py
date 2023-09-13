import datetime


class DatesHandler:
    @staticmethod
    def calculate_age(birthday):
        today = datetime.date.today()
        age = (
            today.year
            - birthday.year
            - ((today.month, today.day) < (birthday.month, birthday.day))
        )

        return age
