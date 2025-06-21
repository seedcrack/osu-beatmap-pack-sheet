from ossapi import Ossapi
print('Hello! please enter your Client ID and Client secret')
client_id = input('Client ID : ')
client_secret = input('Client Secret : ')
try:
    api = Ossapi(client_id, client_secret)
except Exception as e:
    print(f'Error : {e}')

has_30_days = [4,6,9,11]
has_31_days = [1,3,5,7,8,10,12]
result = []

print('''\nThis code gather all beatmapsets between specified months and year
If you want to search across 2 years, please run this code twice and combine the results
Running this will overwrite the old output, so please finish up your current one first\n''')

print('''-1 : all gamemode
0 : std
1 : Taiko
2 : ctb
3 : Mania''')
gamemode = int(input('gamemode : '))
year = input('year to search : ')
start_month = int(input('starting month (put a number) : '))
end_month = int(input('ending month (put a number) : '))
# sry can't do start and end date, too much of a headache

for i in range(start_month,end_month+1):
    if i in has_30_days:
        day_in_month = 30
    if i in has_31_days:
        day_in_month = 31
    if i == 2:
        if i % 4 == 0: # not gonna be a problem until 2100
            day_in_month = 29
        else:
            day_in_month = 28
    print(f'searching month {i}')

    for j in range(1,day_in_month+1):
        search_prompt = f'ranked={year}-{i}-{j}'
        search_result = api.search_beatmapsets(query=search_prompt, mode=gamemode, category='ranked', explicit_content='show', sort="ranked_asc")
        total_check = search_result.total
        if total_check > 50:
            print(f"{search_prompt} will have missing maps {total_check}")
        for k in search_result.beatmapsets:
                result.append(k.id)

with open('search_result.txt', 'w') as f:
    print(result, file=f)
    
print('done, please check search_result.txt')