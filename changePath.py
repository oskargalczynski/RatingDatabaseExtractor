import os
dir_path = os.path.dirname(os.path.realpath(__file__))
a_file = open("docker-compose.yml", "r")

list_of_lines = a_file.readlines()

for i in range(len(list_of_lines)):
    if "#absolute path to repository#" in list_of_lines[i]:
        list_of_lines[i] = list_of_lines[i].split('#')
        list_of_lines[i][1]=dir_path
        list_of_lines[i]=list_of_lines[i][0]+list_of_lines[i][1]+list_of_lines[i][2]
        print(list_of_lines[i])

a_file = open("docker-compose.yml", "w", 1, "utf-8")
print(list_of_lines)
a_file.writelines(list_of_lines)
a_file.close()