if __name__ == '__main__':
    dic_result ={}
    names= ['Nova', 'Pixel', 'Rex']
    colors = ['white', 'gray', None]
    ages = [4,2,3]
    breeds = [None, 'Kyi-leo', None]

    for ind, name in enumerate(names):
        dic_result[name] = {}
        if colors[ind] is not None:
            dic_result[name]['color'] = colors[ind]
        if ages[ind] is not None:
            dic_result[name]['age'] = ages[ind]
        if breeds[ind] is not None:
            dic_result[name]['breed'] = breeds[ind]

    print(dic_result)

