class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

        @staticmethod
        def days_to_weeks(days):
            return (days + 6) // 7

        @classmethod
        def from_dict(cls, course_dict):
            name = course_dict["name"]
            description = course_dict["description"]
            days = course_dict["days"]
            weeks = cls.days_to_weeks(days)
            return cls(name, description, weeks)
