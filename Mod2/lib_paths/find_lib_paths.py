# sys lib ne ajuta sa vedem path-urile unde python-ul cauta pachetele de importat
import sys
print(sys.path)

# avem 2 modalitati de a extinde aceasta lista cu path-uri
# 1. adaugam variabila PYTHONPATH in System Enviroment variables cu path-uri aditionale
# 2. extindem sys.path la executia fisierului nostru si apoi putem importa module
sys.path.append("D:\\SDA\\python technology\\RO22\\pack1")
import module_a_pack as m_a_p
print(m_a_p.test)

# mai indicat este sa ne folosim de path-uri relative fata de file-ul nostru
sys.path.append("..\\pack1")
import module_a_pack as m_a_p_rel
print(m_a_p_rel.test)

# daca vrem ca un folder care contine mai multe module/fisiere sa devina pachet si sa poate fi importat oriunde
# ar trebui adaugata path-ul pana la parintele lui in variabila PYTHONPATH

from RO22.pack1.module_a_pack import test
from RO22 import module_b
print(test)
print(module_b.my_list)
