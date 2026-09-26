class Student:
	def __init__(
		self,
		date_of_birth=None,
		age=None,
		gender=None,
		mobile_number=None,
		email_address=None,
		preferred_language=None,
		school_college_name=None,
		class_grade=None,
		board_curriculum=None,
		academic_year=None,
		subjects=None,
		subject_levels=None,
		help_topics=None,
		guardian_name=None,
		guardian_relationship=None,
		guardian_mobile_number=None,
		guardian_email_address=None,
		guardian_preferred_communication_method=None,
	):
		self.date_of_birth = date_of_birth
		self.age = age
		self.gender = gender
		self.mobile_number = mobile_number
		self.email_address = email_address
		self.preferred_language = preferred_language
		self.school_college_name = school_college_name
		self.class_grade = class_grade
		self.board_curriculum = board_curriculum
		self.academic_year = academic_year
		self.subjects = [] if subjects is None else subjects
		self.subject_levels = {} if subject_levels is None else subject_levels
		self.help_topics = [] if help_topics is None else help_topics
		self.guardian_name = guardian_name
		self.guardian_relationship = guardian_relationship
		self.guardian_mobile_number = guardian_mobile_number
		self.guardian_email_address = guardian_email_address
		self.guardian_preferred_communication_method = (
			guardian_preferred_communication_method
		)
