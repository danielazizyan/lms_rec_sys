import csv
import random
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define the list of course subjects
subjects = [
    "Programming",
    "Data Science",
    "Web Development",
    "Digital Marketing",
    "Graphic Design",
    "Business",
    "Computer Science"
]

# Define number of users
num_users = 500

users = []
for _ in range(num_users):
  user_id = len(users) + 1  # Assign unique user ID
  user = {
      "id": user_id,
      "name": fake.name(),
      "email": fake.email(),
      "user_preference": random.choice(subjects)
  }
  users.append(user)

courses = [
  {
        "course_id": 1,
        "name": "Accounting Fundamentals",
        "level": "Beginner",
        "subject": "Business",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 2,
        "name": "Marketing Fundamentals",
        "level": "Beginner",
        "subject": "Business",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 3,
        "name": "Project Management Essentials",
        "level": "Intermediate",
        "subject": "Business",
        "quiz_complexity": "Medium",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 4,
        "name": "Business Communication Skills",
        "level": "Intermediate",
        "subject": "Business",
        "quiz_complexity": "Medium",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 5,
        "name": "Introduction to Entrepreneurship",
        "level": "Intermediate",
        "subject": "Business",
        "quiz_complexity": "Medium",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 6,
        "name": "Financial Management for Businesses",
        "level": "Advanced",
        "subject": "Business",
        "quiz_complexity": "High",
        "prerequisites": ["Accounting Fundamentals"]
    },
    {
        "course_id": 7,
        "name": "Business Analytics with Excel",
        "level": "Advanced",
        "subject": "Business",
        "quiz_complexity": "High",
        "prerequisites": ["Accounting Fundamentals", "Marketing Fundamentals"]
    },
    {
        "course_id": 8,
        "name": "Human Resources Management Essentials",
        "level": "Intermediate",
        "subject": "Business",
        "quiz_complexity": "Medium",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 9,
        "name": "Operations Management Fundamentals",
        "level": "Intermediate",
        "subject": "Business",
        "quiz_complexity": "Medium",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 10,
        "name": "Introduction to Business Law",
        "level": "Intermediate",
        "subject": "Business",
        "quiz_complexity": "Medium",
        "prerequisites": []
    },
    {
        "course_id": 11,
        "name": "Business Ethics and Social Responsibility",
        "level": "Intermediate",
        "subject": "Business",
        "quiz_complexity": "Medium",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 12,
        "name": "Marketing Strategy for Growth",
        "level": "Advanced",
        "subject": "Business",
        "quiz_complexity": "High",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 13,
        "name": "Sales Management Techniques",
        "level": "Advanced",
        "subject": "Business",
        "quiz_complexity": "High",
        "prerequisites": ["Marketing Fundamentals"]
    },
    {
        "course_id": 14,
        "name": "Financial Markets and Investments",
        "level": "Advanced",
        "subject": "Business",
        "quiz_complexity": "High",
        "prerequisites": ["Accounting Fundamentals"]
    },
    {
        "course_id": 15,
        "name": "Business Negotiations and Communication",
        "level": "Advanced",
        "subject": "Business",
        "quiz_complexity": "High",
        "prerequisites": ["Business Communication Skills"]
    },
    {
        "course_id": 16,
        "name": "Introduction to Graphic Design Principles",
        "level": "Beginner",
        "subject": "Graphic Design",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 17,
        "name": "Design Software Fundamentals (Adobe Photoshop)",
        "level": "Beginner",
        "subject": "Graphic Design",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 18,
        "name": "Typography for Designers",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles"]
    },
    {
        "course_id": 19,
        "name": "Logo Design Fundamentals",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles"]
    },
    {
        "course_id": 20,
        "name": "Vector Graphics with Adobe Illustrator",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Design Software Fundamentals (Adobe Photoshop)"]
    },
    {
        "course_id": 21,
        "name": "User Interface (UI) Design Principles",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles"]
    },
    {
        "course_id": 22,
        "name": "Introduction to User Experience (UX) Design",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles"]
    },
    {
        "course_id": 23,
        "name": "Color Theory for Graphic Design",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles"]
    },
    {
        "course_id": 24,
        "name": "Advanced Adobe Photoshop Techniques",
        "level": "Advanced",
        "subject": "Graphic Design",
        "quiz_complexity": "High",
        "prerequisites": ["Design Software Fundamentals (Adobe Photoshop)"]
    },
    {
        "course_id": 25,
        "name": "Advanced Vector Graphics with Adobe Illustrator",
        "level": "Advanced",
        "subject": "Graphic Design",
        "quiz_complexity": "High",
        "prerequisites": ["Vector Graphics with Adobe Illustrator"]
    },
    {
        "course_id": 26,
        "name": "Branding and Identity Design",
        "level": "Advanced",
        "subject": "Graphic Design",
        "quiz_complexity": "High",
        "prerequisites": ["Logo Design Fundamentals", "Typography for Designers"]
    },
    {
        "course_id": 27,
        "name": "Mobile App Design for Beginners",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles", "UI Design Principles"]
    },
    {
        "course_id": 28,
        "name": "Web Design Fundamentals for Graphic Designers",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles"]
    },
    {
        "course_id": 29,
        "name": "Motion Graphics for Beginners",
        "level": "Intermediate",
        "subject": "Graphic Design",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Graphic Design Principles"]
    },
    {
        "course_id": 30,
        "name": "Design Portfolio Development",
        "level": "Advanced",
        "subject": "Graphic Design",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to Graphic Design Principles", "Logo Design Fundamentals", "User Interface (UI) Design Principles"]
    },
    {
        "course_id": 31,
        "name": "Search Engine Optimization (SEO) Fundamentals",
        "level": "Beginner",
        "subject": "Digital Marketing",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 32,
        "name": "Social Media Marketing Strategies",
        "level": "Intermediate",
        "subject": "Digital Marketing",
        "quiz_complexity": "Medium",
        "prerequisites": ["Search Engine Optimization (SEO) Fundamentals"]
    },
    {
        "course_id": 33,
        "name": "Content Marketing for Beginners",
        "level": "Beginner",
        "subject": "Digital Marketing",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 34,
        "name": "Email Marketing Essentials",
        "level": "Intermediate",
        "subject": "Digital Marketing",
        "quiz_complexity": "Medium",
        "prerequisites": ["Content Marketing for Beginners"]
    },
    {
        "course_id": 35,
        "name": "Pay-Per-Click (PPC) Advertising with Google Ads",
        "level": "Intermediate",
        "subject": "Digital Marketing",
        "quiz_complexity": "Medium",
        "prerequisites": ["Search Engine Optimization (SEO) Fundamentals"]
    },
    {
        "course_id": 36,
        "name": "Social Media Advertising Strategies",
        "level": "Advanced",
        "subject": "Digital Marketing",
        "quiz_complexity": "High",
        "prerequisites": ["Social Media Marketing Strategies"]
    },
    {
        "course_id": 37,
        "name": "Content Marketing Strategy and Planning",
        "level": "Advanced",
        "subject": "Digital Marketing",
        "quiz_complexity": "High",
        "prerequisites": ["Content Marketing for Beginners"]
    },
    {
        "course_id": 38,
        "name": "Email Marketing Automation",
        "level": "Advanced",
        "subject": "Digital Marketing",
        "quiz_complexity": "High",
        "prerequisites": ["Email Marketing Essentials"]
    },
    {
        "course_id": 39,
        "name": "Conversion Rate Optimization (CRO)",
        "level": "Advanced",
        "subject": "Digital Marketing",
        "quiz_complexity": "High",
        "prerequisites": ["Search Engine Optimization (SEO) Fundamentals"]
    },
    {
        "course_id": 40,
        "name": "Marketing Analytics with Google Analytics",
        "level": "Advanced",
        "subject": "Digital Marketing",
        "quiz_complexity": "High",
        "prerequisites": ["Search Engine Optimization (SEO) Fundamentals"]
    },
    {
        "course_id": 41,
        "name": "Social Media Community Management",
        "level": "Intermediate",
        "subject": "Digital Marketing",
        "quiz_complexity": "Medium",
        "prerequisites": ["Social Media Marketing Strategies"]
    },
    {
        "course_id": 42,
        "name": "Influencer Marketing Strategies",
        "level": "Intermediate",
        "subject": "Digital Marketing",
        "quiz_complexity": "Medium",
        "prerequisites": ["Social Media Marketing Strategies"]
    },
    {
        "course_id": 43,
        "name": "Search Engine Marketing (SEM) for Beginners",
        "level": "Beginner",
        "subject": "Digital Marketing",
        "quiz_complexity": "Low",
        "prerequisites": ["Search Engine Optimization (SEO) Fundamentals"]
    },
    {
        "course_id": 44,
        "name": "Ecommerce Marketing Strategies",
        "level": "Intermediate",
        "subject": "Digital Marketing",
        "quiz_complexity": "Medium",
        "prerequisites": ["Search Engine Optimization (SEO) Fundamentals"]
    },
    {
        "course_id": 45,
        "name": "Digital Marketing for Any Business",
        "level": "Intermediate",
        "subject": "Digital Marketing",
        "quiz_complexity": "Medium",
        "prerequisites": ["Search Engine Optimization (SEO) Fundamentals", "Content Marketing for Beginners"]
    },
    {
        "course_id": 46,
        "name": "Introduction to HTML & CSS Fundamentals",
        "level": "Beginner",
        "subject": "Web Development",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 47,
        "name": "Introduction to JavaScript",
        "level": "Beginner",
        "subject": "Web Development",
        "quiz_complexity": "Low",
        "prerequisites": ["Introduction to HTML & CSS Fundamentals"]
    },
    {
        "course_id": 48,
        "name": "Responsive Web Design with Bootstrap",
        "level": "Intermediate",
        "subject": "Web Development",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to HTML & CSS Fundamentals"]
    },
    {
        "course_id": 49,
        "name": "JavaScript for Web Applications",
        "level": "Intermediate",
        "subject": "Web Development",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to JavaScript"]
    },
    {
        "course_id": 50,
        "name": "Introduction to Back-End Development with Python",
        "level": "Intermediate",
        "subject": "Web Development",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to HTML & CSS Fundamentals"]
    },
    {
        "course_id": 51,
        "name": "Web Design Principles for Developers",
        "level": "Intermediate",
        "subject": "Web Development",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to HTML & CSS Fundamentals"]
    },
    {
        "course_id": 52,
        "name": "Introduction to Web Accessibility",
        "level": "Intermediate",
        "subject": "Web Development",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to HTML & CSS Fundamentals"]
    },
    {
        "course_id": 53,
        "name": "Advanced JavaScript: Frameworks and Libraries (React)",
        "level": "Advanced",
        "subject": "Web Development",
        "quiz_complexity": "High",
        "prerequisites": ["JavaScript for Web Applications"]
    },
    {
        "course_id": 54,
        "name": "Server-Side Development with Node.js and Express",
        "level": "Advanced",
        "subject": "Web Development",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to Back-End Development with Python"]
    },
    {
        "course_id": 55,
        "name": "Database Management for Web Applications (MySQL)",
        "level": "Advanced",
        "subject": "Web Development",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to Back-End Development with Python"]
    },
    {
        "course_id": 56,
        "name": "Web Security Fundamentals",
        "level": "Advanced",
        "subject": "Web Development",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to HTML & CSS Fundamentals"]
    },
    {
        "course_id": 57,
        "name": "API Development with Django (Python Framework)",
        "level": "Advanced",
        "subject": "Web Development",
        "quiz_complexity": "High",
        "prerequisites": ["Server-Side Development with Node.js and Express"]
    },
    {
        "course_id": 58,
        "name": "Front-End Development with a JavaScript Framework (Vue.js)",
        "level": "Advanced",
        "subject": "Web Development",
        "quiz_complexity": "High",
        "prerequisites": ["Advanced JavaScript: Frameworks and Libraries (React)"]
    },
    {
        "course_id": 59,
        "name": "Version Control with Git",
        "level": "Intermediate",
        "subject": "Web Development",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to HTML & CSS Fundamentals"]
},
{
        "course_id": 60,
        "name": "Deployment Strategies for Web Applications",
        "level": "Advanced",
        "subject": "Web Development",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to Back-End Development with Python", "Version Control with Git"]
},
{
        "course_id": 61,
        "name": "Introduction to Programming with Python",
        "level": "Beginner",
        "subject": "Programming",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 62,
        "name": "Programming Fundamentals with JavaScript",
        "level": "Beginner",
        "subject": "Programming",
        "quiz_complexity": "Low",
        "prerequisites": []
    },
    {
        "course_id": 63,
        "name": "Object-Oriented Programming (OOP) Concepts with Python",
        "level": "Intermediate",
        "subject": "Programming",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Programming with Python"]
    },
    {
        "course_id": 64,
        "name": "Data Structures and Algorithms Fundamentals",
        "level": "Intermediate",
        "subject": "Programming",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Programming with Python"]
    },
    {
        "course_id": 66,
        "name": "Advanced Python Programming",
        "level": "Advanced",
        "subject": "Programming",
        "quiz_complexity": "High",
        "prerequisites": ["Object-Oriented Programming (OOP) Concepts with Python"]
    },
    {
        "course_id": 67,
        "name": "Desktop Application Development with PyQt (Python GUI Framework)",
        "level": "Advanced",
        "subject": "Programming",
        "quiz_complexity": "High",
        "prerequisites": ["Advanced Python Programming"]
    },
    {
        "course_id": 68,
        "name": "Introduction to Java Programming",
        "level": "Intermediate",
        "subject": "Programming",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Programming with Python" or "Programming Fundamentals with JavaScript"]  # Basic programming understanding is helpful
    },
    {
        "course_id": 69,
        "name": "Introduction to Game Development with Pygame (Python Library)",
        "level": "Advanced",
        "subject": "Programming",
        "quiz_complexity": "High",
        "prerequisites": ["Advanced Python Programming"]
    },
    {
        "course_id": 71,
        "name": "Introduction to C Programming",
        "level": "Intermediate",
        "subject": "Programming",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Programming with Python" or "Programming Fundamentals with JavaScript"]  # Basic programming understanding is helpful
    },
    {
        "course_id": 72,
        "name": "Introduction to Computer Architecture",
        "level": "Intermediate",
        "subject": "Computer Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Programming with Python"]  # Basic programming knowledge helpful
    },
    {
        "course_id": 73,
        "name": "Introduction to Automata Theory",
        "level": "Advanced",
        "subject": "Computer Science",
        "quiz_complexity": "High",
        "prerequisites": ["Data Structures and Algorithms Fundamentals"]
    },
    {
        "course_id": 74,
        "name": "Introduction to Operating Systems",
        "level": "Advanced",
        "subject": "Computer Science",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to Computer Architecture"]
    },
    {
        "course_id": 75,
        "name": "Programming Languages: Paradigms and Design",
        "level": "Advanced",
        "subject": "Computer Science",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to Programming with Python"]
    },
    {
        "course_id": 76,
        "name": "Compiler Design and Construction",
        "level": "Advanced",
        "subject": "Computer Science",
        "quiz_complexity": "High",
        "prerequisites": ["Data Structures and Algorithms Fundamentals", "Introduction to Automata Theory"]
    },
    {
        "course_id": 77,
        "name": "Introduction to Data Science",
        "level": "Beginner",
        "subject": "Data Science",
        "quiz_complexity": "Low",
        "prerequisites": ["Introduction to Programming with Python"] 
    },
    {
        "course_id": 78,
        "name": "Data Analysis with Pandas (Python Library)",
        "level": "Intermediate",
        "subject": "Data Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Data Science"]
    },
    {
        "course_id": 79,
        "name": "Data Visualization with Matplotlib (Python Library)",
        "level": "Intermediate",
        "subject": "Data Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Data Science"]
    },
    {
        "course_id": 80,
        "name": "Introduction to Statistics for Data Science",
        "level": "Intermediate",
        "subject": "Data Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Data Science"]  # Basic understanding of data analysis concepts is helpful
    },
    {
        "course_id": 81,
        "name": "Machine Learning Fundamentals with Scikit-learn (Python Library)",
        "level": "Intermediate",
        "subject": "Data Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Data Analysis with Pandas (Python Library)"]
    },
    {
        "course_id": 82,
        "name": "Introduction to SQL for Data Science",
        "level": "Intermediate",
        "subject": "Data Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Data Science"]  # Basic understanding of data management is helpful
    },
    {
        "course_id": 83,
        "name": "Data Wrangling with Python Libraries (Pandas, NumPy)",
        "level": "Intermediate",
        "subject": "Data Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Data Analysis with Pandas (Python Library)"]
    },
    {
        "course_id": 84,
        "name": "Introduction to Deep Learning with TensorFlow (Python Library)",
        "level": "Advanced",
        "subject": "Data Science",
        "quiz_complexity": "High",
        "prerequisites": ["Machine Learning Fundamentals with Scikit-learn"]
    },
    {
        "course_id": 85,
        "name": "Natural Language Processing (NLP) Fundamentals",
        "level": "Advanced",
        "subject": "Data Science",
        "quiz_complexity": "High",
        "prerequisites": ["Machine Learning Fundamentals with Scikit-learn"]
    },
    {
        "course_id": 86,
        "name": "Time Series Analysis and Forecasting",
        "level": "Advanced",
        "subject": "Data Science",
        "quiz_complexity": "High",
        "prerequisites": ["Data Analysis with Pandas (Python Library)", "Introduction to Statistics for Data Science"]
    },
    {
        "course_id": 87,
        "name": "Big Data Processing with Apache Spark",
        "level": "Advanced",
        "subject": "Data Science",
        "quiz_complexity": "High",
        "prerequisites": ["Data Analysis with Pandas (Python Library)"]  # Familiarity with distributed computing concepts is helpful
    },
    {
        "course_id": 88,
        "name": "Data Science Capstone Project",
        "level": "Advanced",
        "subject": "Data Science",
        "quiz_complexity": "High",
        "prerequisites": [
            "Machine Learning Fundamentals with Scikit-learn",
            "Data Visualization with Matplotlib (Python Library)",
            "Introduction to SQL for Data Science"  # Completion of core data science courses is recommended
        ]
    },
    {
        "course_id": 89,
        "name": "Introduction to Exploratory Data Analysis (EDA)",
        "level": "Intermediate",
        "subject": "Data Science",
        "quiz_complexity": "Medium",
        "prerequisites": ["Introduction to Data Science"]
    },
{
        "course_id": 90,
        "name": "Data Ethics and Responsible AI",
        "level": "Advanced",
        "subject": "Data Science",
        "quiz_complexity": "High",
        "prerequisites": ["Introduction to Machine Learning"]  # General understanding of machine learning concepts is helpful
    }
]

user_interactions = []
for user in users:
  for course in courses:
    # Check user preference and course prerequisites
    if user["user_preference"] == course["subject"] and all(prerequisite in user_interactions for prerequisite in course.get("prerequisites", [])):
      # All prerequisites completed, proceed with course assignment logic
      completed = random.choice([True, False])
      score = None
      if completed:
        # Assign score based on complexity
        if course["quiz_complexity"] == "Low":
          score = random.randint(70, 90)
        elif course["quiz_complexity"] == "Medium":
          score = random.randint(50, 80)
      user_interactions.append({
          "user_id": user["id"],
          "course": course["name"],
          "completed": completed,
          "score": score
      })

# print("Sample User Data:")
# print(users[:2])  # Print the first two users for reference

# print("\nSample User Interactions:")
# print(user_interactions[:2])  # Print the first two interactions for reference





# complete_data = []

# # Add user data
# for user in users:
#   complete_data.append({
#       "user_id": user["id"],
#       "name": user["name"],
#       "email": user["email"],
#       "user_preference": user["user_preference"],
#   })

# # Add course data
# for course in courses:
#   complete_data.append({
#       "course_id": course["course_id"],
#       "name": course["name"],
#       "level": course["level"],
#       "subject": course["subject"],
#       "quiz_complexity": course["quiz_complexity"],
#       "prerequisites": course["prerequisites"],
#   })

# # Add user interactions
# for interaction in user_interactions:
#   complete_data.append({
#       "user_id": interaction["user_id"],
#       "course": interaction["course"],  # Assuming 'course' field holds course name
#       "completed": interaction["completed"],
#       "score": interaction["score"],
#   })


# with open('course_recommendation_data.csv', 'w', newline='') as csvfile:
#   writer = csv.writer(csvfile)

#   # Write the header row
#   header = [
#       'user_id', 'name', 'email', 'user_preference',
#       'course_id', 'course_name', 'level', 'subject', 'quiz_complexity', 'prerequisites',
#       'completed', 'score'
#   ]
#   writer.writerow(header)

#   # Write each data point as a row
#   for item in complete_data:
#     # Try-except block to handle missing 'user_id' key gracefully
#     try:
#       user_id = item['user_id']
#       name = item['name']
#       email = item['email']
#       user_preference = item['user_preference']
#       course_id = None
#       course_name = None
#       level = None
#       subject = None
#       quiz_complexity = None
#       prerequisites = None
#     except KeyError:
#       try:
#           course_name = item['course']
#       except KeyError:
#           course_name = None  # Handle cases where 'course' key is also missing
#       user_id = None
#       name = None
#       email = None
#       user_preference = None
#       course_id = item.get('course_id')
#       level = item.get('level')
#       subject = item.get('subject')
#       quiz_complexity = item.get('quiz_complexity')
#       prerequisites = item.get('prerequisites')

#     # Write the row with appropriate values based on data type
#     writer.writerow([
#         user_id, name, email, user_preference,
#         course_id, course_name, level, subject, quiz_complexity, prerequisites,
#         completed if 'completed' in item else None,  # Check if 'completed' exists
#         score if 'score' in item else None           # Check if 'score' exists
#     ])


with open('users.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # Write the header row
  header = ['user_id', 'name', 'email', 'user_preference']
  writer.writerow(header)

  # Write each user data as a row
  for user in users:
    writer.writerow([user['id'], user['name'], user['email'], user['user_preference']])




with open('courses.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # Write the header row
  header = ['course_id', 'name', 'level', 'subject', 'quiz_complexity', 'prerequisites']
  writer.writerow(header)

  # Write each course data as a row
  for course in courses:
    writer.writerow([
        course['course_id'], course['name'], course['level'],
        course['subject'], course['quiz_complexity'], course['prerequisites']
    ])






with open('user_interactions.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # Write the header row
  header = ['user_id', 'course', 'completed', 'score']
  writer.writerow(header)

  # Write each user interaction data as a row
  for interaction in user_interactions:
    writer.writerow([interaction['user_id'], interaction['course'], interaction['completed'], interaction['score']])