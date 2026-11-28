def generate_learning_roadmap(missing_skills):

    if not missing_skills:
        return {
            "message": "You already have all the required skills!",
            "total_skills_to_learn": 0,
            "learning_roadmap": []
        }

    learning_roadmap = []

    learning_resources = {
        "java": "Learn Java fundamentals, OOP and collections.",
        "spring boot": "Learn Spring Boot, REST APIs and dependency injection.",
        "python": "Learn Python fundamentals, functions and OOP.",
        "react": "Learn React components, hooks and state management.",
        "sql": "Learn SQL queries, joins and database relationships.",
        "postgresql": "Learn PostgreSQL, queries and database management.",
        "machine learning": "Learn ML fundamentals, regression and classification.",
        "tensorflow": "Learn TensorFlow and neural network fundamentals.",
        "pytorch": "Learn PyTorch and deep learning basics.",
        "docker": "Learn Docker containers and image management."
    }

    for skill in missing_skills:

        skill_lower = skill.lower()

        recommendation = learning_resources.get(
            skill_lower,
            f"Start learning {skill} fundamentals and build a small project."
        )

        learning_roadmap.append({
            "skill": skill,
            "recommendation": recommendation
        })

    return {
        "message": "Personalized learning roadmap generated successfully",
        "total_skills_to_learn": len(learning_roadmap),
        "learning_roadmap": learning_roadmap
    }