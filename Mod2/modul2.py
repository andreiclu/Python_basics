# Import module
import modul1

print(modul1.test)
courses = ["Gym", "History", "Mathematic"]
index = modul1.find_index(courses, "Gym")
print(index)  # Return 0

#   # Import whole module as m_a
#     import modul_a as m_a
#
#     print(m_a.test)
#     courses = ["Gym", "History", "Mathematic"]
#     index = m_a.find_index(courses, "Gym")
#     print(index)  # Return 0

# Import only the find_index function

    # from modul_a import test, find_index
    #
    # courses = ["Gym", "History", "Mathematic"]
    # index = find_index(courses, "Gym")
    # print(index)  # Return 0

# Import all variables and functions
# from modul_a import *
#
# print(test)
# courses = ["Gym", "History", "Mathematic"]
# index = find_index(courses, "Gym")
# print(index)  # Return 0

