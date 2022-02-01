# importam module_a cu totul sub alt nume/alias
import module_a as m_a

# mai departe o sa folosim aliasul ca sa accesam variabile/functii din acel modul
print(m_a.test)
my_list = [1, "txt", 19.2, "placeholder"]

print(m_a.find_index(my_list, "txt"))
