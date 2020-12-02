year = int(input('Enter year of Ferrari 250 GTO: \n'))

if year < 1962: 
    print('Car did not exist.')

elif 1964 >= year >= 1962:
    print('$ 18500')
elif 1968 >= year >= 1965:
    print('$ 6000')
elif 1971 >= year >= 1969:
    print('$ 12000')
elif 1975 >= year >= 1972:
    print('$ 48000')
elif 1980 >= year >= 1976:
    print('$ 200000')
elif 1985 >= year >= 1981:
    print('$ 650000')
elif 2012 >= year >= 1986:
    print('$ 35000000')
elif 2014 >= year >= 2013:
    print('$ 52000000')
else:
    print('No data')