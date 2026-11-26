import re
from text_preprocessor import normalize_text

SKILL_ALIASES = {
    "Java": ["java"],
    "Python": ["python"],
    "JavaScript": ["javascript", "js"],
    "Spring Boot": ["spring boot", "springboot"],
    "React": ["react", "reactjs"],
    "Machine Learning": ["machine learning", "ml"],
    "Artificial Intelligence": ["artificial intelligence", "ai"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MySQL": ["mysql"],
    "HTML": ["html"],
    "CSS": ["css"],
    "Node.js": ["node.js", "nodejs"],
    "C++": ["c++"],
    "C": ["c"],
    "Docker": ["docker"],
    "Git": ["git"],
    "AWS": ["aws", "amazon web services"],
    "SQL": ["sql"],
    "Kotlin": ["kotlin"],
    "PHP": ["php"],
    "Angular": ["angular"],
    "Vue.js": ["vue.js", "vuejs", "vue"],
    "MongoDB": ["mongodb", "mongo"],
    "Redis": ["redis"],
    "Flask": ["flask"],
    "Django": ["django"],
    "TensorFlow": ["tensorflow", "tf"],
    "PyTorch": ["pytorch", "torch"]
}




def extract_skills(text: str):

    extracted_skills = []
    text = normalize_text(text)

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            if alias == "c":
                pattern = r"(?<!\w)c(?![\w+#])"
            else:
                pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(pattern, text):
                extracted_skills.append(skill)
                break

    return extracted_skills


# Skill Categories
SKILL_CATEGORIES = {
    "Programming": [
        "Java", "Python", "JavaScript", "C++", "Kotlin", "PHP"
    ],
    "Frontend": [
        "HTML", "CSS", "React", "Angular", "Vue.js"
    ],
    "Backend": [
        "Spring Boot", "Node.js", "Flask", "Django"
    ],
    "Database": [
        "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis"
    ],
    "AI/ML": [
        "Machine Learning", "TensorFlow", "PyTorch"
    ]
}


def categorize_skills(skills):
    result = {}

    for category, category_skills in SKILL_CATEGORIES.items():
        matched = [
            skill for skill in skills
            if skill in category_skills
        ]

        if matched:
            result[category] = matched

    return result
