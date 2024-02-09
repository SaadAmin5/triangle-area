#finding area of a triangle

def area_triangle(base, height):
    area=0.5*(base*height)
    return area


b=int(input('Enter \'Base\' of triangle: '))
h=int(input('Enter \'Height\' of traingle: '))

a=area_triangle(base=b, height=h)

print('\n')
print('Area of the Triangle is: ', a)