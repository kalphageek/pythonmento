import pymysql


# 전체 조회용 함수
def select_all_books():
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()                             # 커서 확보

        cur.execute('SELECT * FROM books')       # 조회용 SQL 실행

        print('[1] 전체 데이터 출력하기')
        books = cur.fetchall()                          # 조회한 데이터 불러오기

        for book in books:                              # 데이터 출력하기
            print(book)

    finally:
        conn.close()                                    # 커넥션 닫기

# 일부 조회용 함수
def select_some_books(number):
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()                             # 커서 확보

        cur.execute('SELECT * FROM books')       # 조회용 SQL 실행

        print('[2] 데이터 일부 출력하기')
        books = cur.fetchmany(number)                   # 조회한 데이터 일부 불러오기

        for book in books:                             # 데이터 출력하기
            print(book)

    finally:
        conn.close()                                    # 커넥션 닫기

# 1개 조회용 함수
def select_one_book():
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()                            # 커서 확보

        cur.execute('SELECT * FROM books')      # 조회용 SQL 실행

        print('[3] 1개 데이터 출력하기')
        print(cur.fetchone())                          # 데이터 한개 출력하기

    finally:
        conn.close()                                   # 커넥션 닫기


# 1개 조회용 함수
def select_title_book(title):
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()                            # 커서 확보

        cur.execute('SELECT * FROM books where title = %s', title)      # 조회용 SQL 실행

        print('[3] 특정 title  데이터 출력하기')
        print(cur.fetchall())                          # 데이터 한개 출력하기

    finally:
        conn.close()                                   # 커넥션 닫기

# 쪽수 많은 책 조회용 함수
def find_big_books():
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()                             # 커서 확보

        # 조회용 SQL 실행 (300 쪽이 넘는 책의 제목과 쪽수를 출력하라)
        cur.execute('SELECT title, pages FROM books WHERE pages > 300')

        print('[4] 페이지 많은 책 출력하기')
        books = cur.fetchall()                          # 조회한 데이터 불러오기

        for book in books:                              # 데이터 출력하기
            print(book)

    finally:
        conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_title_book('개발자의 코드')
    print('=============================================')