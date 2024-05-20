import math  #math 모듈의 pi와 sqrt를 사용하기 위해 모듈 불러오기

class Line:
    __length = 1
    """
    외부에서 접근 불가능한 필드 __length가 있으며, 기본 값은 1이다.
    """
    
    def __init__(self, length):
        if ( (type(length) == int or type(length) == float) and length > 0 ):
            self.__length = length
    """
    __length 필드는 int 또는 float 타입으로만 설정될 수 있다.
    __length 필드는 0 이하의 값을 가질 수 없다.
    생성자를 통해 초기 __length의 값을 지정할 수 있다.
    """
    
    def get_length(self):
        """
        해당 필드에 접근하기 위한 메소드 get_length가 있다.
        """
        return self.__length
    
    def set_length(self, value):
         """ 
         해당 필드에 접근하기 위한 메소드 set_length가 있다.
         __length 필드는 int 또는 float 타입으로만 설정될 수 있다.
         __length 필드는 0 이하의 값을 가질 수 없다.
         """
         if ( (type(value) == int or type(value) == float) and value > 0 ):
            self.__length = value

    
def area_square(line):
    """
    Line 클래스의 객체를 매개변수로 받아, length**2의 정사각형의 넓이를 반환한다.
    __length 필드는 int 또는 float 타입으로만 설정되고 0 이하의 값을 가질 수 없다.
    위의 사항에 위배되는 값이 인자로 설정될 경우, 기본/이전 값을 유지한다.
    매개변수 타입이 Line 클래스가 아닌 경우, 숫자 0을 반환한다.
    """
    if( type(line) != Line ):
        return 0
    else:
        area = line.get_length() ** 2
        return area

def area_circle(line):
    """
    Line 클래스의 객체를 매개변수로 받아, length ** 2 * π의 원의 넓이를 반환한다.
    π는 math 모듈의 math.pi를 사용한다.
    __length 필드는 int 또는 float 타입으로만 설정되고 0 이하의 값을 가질 수 없다.
    위의 사항에 위배되는 값이 인자로 설정될 경우, 기본/이전 값을 유지한다.
    매개변수 타입이 Line 클래스가 아닌 경우, 숫자 0을 반환한다.
    """
    if( type(line) != Line ):
        return 0
    else:
        area = line.get_length() ** 2 * math.pi
        return area

def area_regular_triangle(line):
    """
    Line 클래스의 객체를 매개변수로 받아, length ** 2 * √3 / 4의 정삼각형의 넓이를 반환한다.
    루트는 math 모듈의 math.sqrt 함수를 사용한다.
    __length 필드는 int 또는 float 타입으로만 설정되고 0 이하의 값을 가질 수 없다.
    위의 사항에 위배되는 값이 인자로 설정될 경우, 기본/이전 값을 유지한다.
    매개변수 타입이 Line 클래스가 아닌 경우, 숫자 0을 반환한다.
    """
    if( type(line) != Line ):
        return 0
    else:
        area = line.get_length() ** 2 * math.sqrt(3) / 4
        return area

    
