"""
A dictionary with name of countries and their population
"""


def main():
    country_population = {'USA': 300000000, 'Germany': 70000000, 'UK': 30000000, 'Italy': 20000000, 'Belgium': 25458346,
                          'Japan': 111200459, 'China': 1399458360, 'Vietnam': 99234567, 'Thailand': 74250765,
                          'India': 1250000000, 'Singapore': 125689, 'Vanuatu': 34567}
    while True:
        print('Enter the name of the country, hit 0 to exit')
        country = input('Name of country: ')
        if country == '0':
            break
        elif country not in country_population:
            print('\nThe population of the country is not known')
            print('Please add to the dictionary the new country with its population')
            new_country = input('Name of the new country: ')
            new_population = int(input("The new country's population: "))
            print(country_population.update({new_country: new_population}))
        else:
            print(country_population.get(country))

    #  Display the final dict once the user exits the loop
    #  Display format: Country 1 has population X
    for country, population in country_population.items():
        print('Country',country,'has a population',population)

    # Sorted by country
    print("Part b but sorted by country")
    sorted_country = sorted(country_population.items())
    for country, population in sorted_country:
        print('Country',country,'has a population',population)

    print('\nCountry with population greater than 1 billion: ')
    super_country = {country: population for country, population in country_population.items() if
                     population >= 1000000000}
    print(super_country)


if __name__ == '__main__':
    main()