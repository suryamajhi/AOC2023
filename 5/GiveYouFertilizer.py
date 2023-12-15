import re

re_seed = re.compile(r'seeds:\s(?P<seeds>.*)')
re_seed_to_soil = re.compile(r'seed-to-soil map:(.*\n)+?(?!\w)', re.M)
re_soil_to_fertilizer = re.compile(r'soil-to-fertilizer map:(.*\n)+?(?!\w)', re.M)
re_fertilizer_to_water = re.compile(r'fertilizer-to-water map:(.*\n)+?(?!\w)', re.M)
re_water_to_light = re.compile('water-to-light map:(.*\n)+?(?!\w)', re.M)
re_light_to_temperature = re.compile(r'light-to-temperature map:(.*\n)+?(?!\w)', re.M)
re_temperature_to_humidity = re.compile(r'temperature-to-humidity map:(.*\n)+?(?!\w)', re.M)
re_humidity_to_location = re.compile(r'humidity-to-location map:(\n.*)+', re.M)

seed_list = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


def parse_data_to_list(re_required, file_str, list_to_append):
    sts = re_required.search(file_str)
    if not sts:
        print(re_required)
    sts = sts.group(0)
    for i, l in enumerate(sts.split('\n')):
        if i == 0 or not l:
            continue
        list_to_append.append([int(x) for x in l.split(' ')])


with open('1.txt', 'r') as file:
    file_str = file.read()
    s = re_seed.search(file_str)
    seeds = s.group('seeds')
    seed_list.extend([int(x) for x in seeds.split(' ')])

    parse_data_to_list(re_seed_to_soil, file_str, seed_to_soil)
    parse_data_to_list(re_soil_to_fertilizer, file_str, soil_to_fertilizer)
    parse_data_to_list(re_fertilizer_to_water, file_str, fertilizer_to_water)
    parse_data_to_list(re_water_to_light, file_str, water_to_light)
    parse_data_to_list(re_light_to_temperature, file_str, light_to_temperature)
    parse_data_to_list(re_temperature_to_humidity, file_str, temperature_to_humidity)
    parse_data_to_list(re_humidity_to_location, file_str, humidity_to_location)



result_list = []
for seed in seed_list:

    chosen = seed
    for ar in seed_to_soil:
        if ar[1] <= chosen < ar[1] + ar[2]:
            chosen = ar[0] + chosen - ar[1]
            break
    for ar in soil_to_fertilizer:
        if ar[1] <= chosen < ar[1] + ar[2]:
            chosen = ar[0] + chosen - ar[1]
            break
    for ar in fertilizer_to_water:
        if ar[1] <= chosen < ar[1] + ar[2]:
            chosen = ar[0] + chosen - ar[1]
            break
    for ar in water_to_light:
        if ar[1] <= chosen < ar[1] + ar[2]:
            chosen = ar[0] + chosen - ar[1]
            break
    for ar in light_to_temperature:
        if ar[1] <= chosen < ar[1] + ar[2]:
            chosen = ar[0] + chosen - ar[1]
            break
    for ar in temperature_to_humidity:
        if ar[1] <= chosen < ar[1] + ar[2]:
            chosen = ar[0] + chosen - ar[1]
            break
    for ar in humidity_to_location:
        if ar[1] <= chosen < ar[1] + ar[2]:
            chosen = ar[0] + chosen - ar[1]
            break

    result_list.append(chosen)

print(result_list)
print(min(result_list))
