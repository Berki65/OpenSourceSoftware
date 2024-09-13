"""
Assignment from Berkay Bentetik - 24170078
Python Lab 01 - COVID-19 Statistics
"""


def normalize_data(n_cases, n_people, scale):
    # Calculate the number of cases per its population
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm_cases.append((n / n_people[idx]) * scale)  # Scale could be 1000000 but its better this way
    return norm_cases


regions = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk',
           'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227, 13530519, 3359527, 3322373, 2938429, 2630254, 2393626, 2118183, 1838353, 1792476, 1597179, 1536270,
            1454679, 1441970, 1124459, 675883, 365309]  # 2021-08
n_covid = [644, 529, 38, 29, 148, 28, 41, 62, 23, 27, 27, 33, 16, 40, 20, 5, 4]  # 2021-09-21

sum_people = sum(n_people)  # The total number of people
sum_covid = sum(n_covid)  # The total number of new cases
norm_covid = normalize_data(n_covid, n_people, 1000000)  # Normalize Data Function

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print()  # Print an empty line
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')

for idx, pop in enumerate(n_people):
    ratio = (pop / sum_people) * 1000000  # The ratio of new cases to the total
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))

print()
print('----------------------------------------------------------')
print()

# Print COVID-19 new cases by region
print('### Korean COVID-19 New Cases by Region')
print('* Total new cases:', sum_covid)
print()
print('| Region | New Cases | Ratio (%) | New Cases per / 1M |')

for idx, n in enumerate(n_covid):
    ratio = (n / sum_covid) * 100  #Ratio like above in population by region
    print('| %s | %d | %.1f | %.1f |' % (regions[idx], n, ratio, norm_covid[idx]))
