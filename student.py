from datetime import date, timedelta
from dateutil.relativedelta import relativedelta  # Importera dateutil för skottår

class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
        self.project_scores = {}  # Lägg till projektbetyg

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date = self.end_date + relativedelta(days=days)  # Ta hänsyn till skottår

    def course_schedule(self):
        # Lämnas som det är

    def get_start_date(self):
        return self._start_date  # Lägg till metod för att hämta startdatum

    @property
    def has_extension(self):
        return self.end_date > date.today() + timedelta(days=365)  # Lägg till egenskap för förlängning

    def add_project_score(self, project_name, score):
        self.project_scores[project_name] = score  # Lägg till projektbetyg

    def get_project_score(self, project_name):
        return self.project_scores.get(project_name, None)  # Hämta projektbetyg

# Nu har du lagt till kommentarer för att förklara de olika ändringarna.
