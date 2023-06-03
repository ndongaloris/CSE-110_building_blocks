print()
i = 0
overall_max_expectancy = 0
overall_min_expectancy = 1000

selected_year = 0
selected_country  = ''

max_expectancy = 0
min_expectancy = 1000

year_average = 0
country_average = 0
average = 0

number_of_year = 0
number_of_country = 0

interest = ''
while True:
    try:
        interest = input("Are you interested to know about the life expectancy of a specific 'COUNTRY' or a 'YEAR': ").lower()
        if interest == "country":
            selected_country = input('\nEnter the country of interest: ').lower()
        elif interest == 'year':
            selected_year = int(input('\nEnter the year of interest:'))
        else:
            print("\nInvalid input, please read properly and enter the right input, Thanks.\n")
            continue

        with open("life-expectancy.csv") as dataset:
            for data in dataset:
                parts = data.split(",")
                i += 1
                if i > 1:
                    country = parts[0]
                    code = parts[1]
                    year = int(parts[2])
                    life_expectancy = float(parts[3])
                    if overall_min_expectancy > life_expectancy:
                        overall_min_expectancy = life_expectancy
                        min_country = country
                        min_year = year
                    if overall_max_expectancy < life_expectancy:
                        overall_max_expectancy = life_expectancy
                        max_country = country
                        max_year = year
                    if selected_year == year:
                        number_of_year += 1
                        year_average += life_expectancy
                        if max_expectancy < life_expectancy:
                            max_expectancy = life_expectancy
                            max_choice_country = country
                        elif min_expectancy > life_expectancy:
                            min_expectancy = life_expectancy
                            min_choice_country = country
                        average = year_average / number_of_year
                    elif  selected_country.lower() == country.lower():
                        number_of_country += 1
                        country_average += life_expectancy
                        if max_expectancy < life_expectancy:
                            max_expectancy = life_expectancy
                            given_max_year = year
                        if min_expectancy > life_expectancy:
                            min_expectancy = life_expectancy
                            given_min_year = year
                            average = country_average / number_of_country 
                   
        print(f"\nThe overall max life expectancy is: {overall_max_expectancy} from {max_country} in {max_year}")
        print(f"The overall max life expectancy is: {overall_min_expectancy} from {min_country} in {min_year}")

        if interest == "country":
            print(f'\nFor the {selected_country.capitalize()}:')
            print(f"The average life expectancy was: {average:.2f}")
            print(f"The max life expectancy in {given_max_year} with {max_expectancy}")
            print(f"The min life expectancy in {given_min_year} with {min_expectancy}\n")
        elif interest == 'year':
            print(f'\nFor the year {selected_year}:')
            print(f"The average life expectancy across all countries was: {average:.2f}")
            print(f"The max life expectancy was in {max_choice_country} was {max_expectancy}")
            print(f"The min life expectancy was in {min_choice_country} was {min_expectancy}\n")
           
    except ValueError:
        print("\nInvalid input, please read properly and enter the right input, Thanks.\n")
        continue
    break