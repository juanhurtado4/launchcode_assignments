def sort_contacts(original):
    li = list()
    for name in original:
        join = tuple([name] + list(original[name]))
        li.append(join)
    li.sort()
    return li

def main():
    original = {'zod jose': ('789', 'zodjose@gmail.com'), 'atler mike': ('123', 'atlermike@gmail.com'), 'brandon juan':('456','juanhurtado2@outlook.com')}
    text = input('Enter a dictionary or : ')
    if text == 'original':
        print(sort_contacts(text))
    else:
        print(sort_contacts(text))

if __name__=='__main__':
    main()