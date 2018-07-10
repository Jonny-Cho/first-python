class School:
    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address


# 클래스를 활성화 할 때, 위의 3가지 데이터를 반드시 입력하도록 처리해 봅시다. (클래스 2편 참고)
# 클래스를 활성화 한다는 게 무슨 의미인지 이해를 못했다.
# --> 인스턴스를 만든다(변수에 클래스를 할당하는 작업) e.g. brunch_article = BrunchArticle("개발", "개발은 쉬워요")
# 3가지 데이터를 반드시 입력하도록??
# --> __init__ 함수 사용하기

sch1 = School("Sydney", "1890", "515 Kent st")

print(sch1.name)