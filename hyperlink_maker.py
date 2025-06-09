import ast

with open("search_result.txt", 'r') as file:
    file_content = file.read()
    result = ast.literal_eval(file_content)
    
n = 0
nest = []
nested_list = []
for i in result:
    n += 1
    hyperlink = f'=HYPERLINK("https://osu.ppy.sh/s/{i}",Image("https://b.ppy.sh/thumb/{i}l.jpg", 2))'
    nest.append(hyperlink)
    if n == 20:
        nested_list.append(nest)
        nest = []
        n = 0
nested_list.append(nest)
        
with open("hyperlinks.txt", "w") as f:
    for i in nested_list:
        print(';'.join(i), file=f)
    