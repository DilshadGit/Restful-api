from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]

LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


UNI_DEPARTMENT = (
		('BFS', 'Biomedical and Forensic Sciences'),
		('EBE', 'Engineering and the Built Environment'),
		('CTG', 'Computing and Technology'),
		('LS', 'Life Sciences'),
		('PS', 'Psychology'),
	)